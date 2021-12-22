"""Google Analytics Driver."""
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from google.oauth2 import service_account
from apiclient.discovery import build

from naas_drivers.driver import InDriver, OutDriver


class GoogleAnalytics(InDriver, OutDriver):
    """
    Google Analytics driver.
    """
    def __init__(self) -> None:
        self.views = Views(self)

    def connect(self, json_path: str):
        credentials = service_account.Credentials.from_service_account_file(
            json_path,
            scopes = ['https://www.googleapis.com/auth/analytics.readonly'])
        self.service = build('analyticsreporting', 'v4', credentials=credentials)
        return self
    

class Views():
    def __init__(self, parent) -> None:
        self.parent = parent

    @staticmethod
    def _get_body(view_id: str,
                  start_date: str,
                  end_date: str,
                  metrics: str,
                  pivots_dimensions: str,
                  dimensions: str='ga:yearMonth') -> dict:
        """
        Create the body of the request to Google Analytics Reporting API V4.

        Args:
            view_id: your access point for reports; a defined view of data from a property.
            date_ranges: e.g. [{"startDates": "2020-01-01", "endDates": "2020-12-31"}]
            metrics: e.g. [{'expression': 'ga:users'}, {"expression": "ga:bounceRate"}]
            pivot_dimension: e.g. [{"name": "ga:channelGrouping"}]
            dimensions: e.g. [{'name': 'ga:yearMonth'}]

        Returns response in JSON format.
        """
        return {'reportRequests': [{'viewId': view_id,
                            'dateRanges': {"startDate": start_date, "endDate": end_date},
                            'metrics': [{"expression": metrics}],
                            'dimensions': {"name": dimensions},
                            "pivots": [{"dimensions": {"name": pivots_dimensions},
                                        "metrics": [{"expression": metrics}]
                                       }]
                          }]}

    def get_data(self,
                 view_id: str,
                 metrics: str,
                 pivots_dimensions: str,
                 dimensions: str='ga:yearMonth',
                 start_date: str=None,
                 end_date: str=None,
                 format_type: str="summary") -> pd.DataFrame:
        """
        Get data from Google Analytics Reporting API V4.
        """
        if format_type not in ("summary", "pivot"):
            raise ValueError(
                f"format_type must be either <summary> or <pivot> but is: {format_type}")
        # Default date values
        start_date = start_date if start_date else (
            datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
        end_date = end_date if end_date else datetime.today().strftime("%Y-%m-%d")
        # Create body
        body = self._get_body(view_id, start_date, end_date,
                              metrics, pivots_dimensions, dimensions)
        # Fetch Data
        try:
            response = self.parent.service.reports().batchGet(body=body).execute()
        except Exception as error:
            print(f'❌ An error occured while fetching data.')
            raise error
        # JSON to Pandas DataFrame
        if format_type == "summary":
            return self.format_summary(response)
        return self.format_pivot(response)

    def get_unique_visitors(self, view_id: str, start_date: str=None, end_date: str=None) -> pd.DataFrame:
        """
        Get the number of unique visitors.
        """
        unique_visitors = self.get_data(view_id, metrics="ga:users",
                                        pivots_dimensions="ga:channelGrouping",
                                        dimensions="ga:yearMonth", start_date=start_date,
                                        end_date=end_date, format_type="summary")
        # Format Output
        unique_visitors.reset_index(inplace=True)
        unique_visitors.rename(
            columns={"ga:yearMonth": "year_month", "ga:users": "unique_visitors"}, inplace=True)
        return unique_visitors

    def get_bounce_rate(
            self, view_id=str, start_date: str=None, end_date: str=None) -> pd.DataFrame:
        """
        Get the number of unique visitors.
        """
        bounce_rate = self.get_data(view_id, metrics="ga:bounceRate",
                                    pivots_dimensions="ga:channelGrouping",
                                    dimensions="ga:yearMonth", start_date=start_date,
                                    end_date=end_date, format_type="summary")
        bounce_rate['ga:bounceRate'] /= 100
        bounce_rate.reset_index(inplace=True)
        bounce_rate.rename(
            columns={"ga:yearMonth": "year_month", "ga:bounceRate": "bounce_rate"}, inplace=True)
        return bounce_rate

    def get_time_landing(self,
                         view_id: str,
                         landing_path: str="/",
                         start_date: str=None,
                         end_date: str=None) -> pd.DataFrame:
        """
        Get the average time on landing page.
        """
        avg_time_landing = self.get_data(view_id, metrics="ga:avgTimeOnPage",
                                         pivots_dimensions="ga:landingPagePath",
                                         dimensions="ga:yearMonth", start_date=start_date,
                                         end_date=end_date, format_type="pivot")
        if landing_path in avg_time_landing.columns:
            avg_time_landing = avg_time_landing.loc[:, landing_path]
        else:
            raise KeyError(f"Landing Path ({landing_path}) is not an available url pattern.")
        avg_time_landing.index.rename("year_month", inplace=True)
        avg_time_landing.rename(columns={"ga:avgTimeOnPage": "avg_time_landing"}, inplace=True)
        return avg_time_landing

    def get_pageview(self, view_id: str, start_date: str=None, end_date: str=None) -> pd.DataFrame:
        """
        Get the views of pages.
        """
        pageview = self.get_data(view_id, metrics="ga:pageviews",
                                         pivots_dimensions="ga:pagePath",
                                         dimensions="ga:year", start_date=start_date,
                                         end_date=end_date, format_type="pivot")
        pageview.columns = [page[0] for page in pageview.columns]
        pageview = pageview.head(1).T
        pageview.reset_index(inplace=True)
        pageview.columns = ['pages', 'pageview']
        return pageview

    def get_country(self, view_id: str, metrics: str="ga:sessions",
                    start_date: str=None, end_date: str=None):
        """
        Get sessions per country.
        """
        country = self.get_data(view_id, metrics=metrics,
                                         pivots_dimensions="ga:country",
                                         dimensions="ga:year", start_date=start_date,
                                         end_date=end_date, format_type="pivot")
        country.columns = [c[0] for c in country.columns]
        country = country.T
        country.reset_index(inplace=True)
        country.columns = ["country", metrics.split(":")[-1]]
        return country

    @staticmethod
    def format_summary(response):
        """
        Format summary table.
        """
        row_index_names = response['reports'][0]['columnHeader']['dimensions']
        row_index = [element['dimensions'] for element in response['reports'][0]['data']['rows']]
        row_index_named = pd.MultiIndex.from_arrays(np.transpose(np.array(row_index)),
                                                    names = np.array(row_index_names))
        # extract column names
        summary_column_names = [item['name'] for item in response['reports'][0]
                                ['columnHeader']['metricHeader']['metricHeaderEntries']]
        # extract table values
        summary_values = [element['metrics'][0]['values']
                          for element in response['reports'][0]['data']['rows']]
        return pd.DataFrame(data = np.array(summary_values),
                        index = row_index_named,
                        columns = summary_column_names).astype('float')

    @staticmethod
    def format_pivot(response):
        """
        Creates the final dataframe.
        """
        # extract table values
        pivot_values = [item['metrics'][0]['pivotValueRegions'][0]['values']
                        for item in response['reports'][0]['data']['rows']]
        # create column index
        top_header = [item['dimensionValues'] for item in response['reports'][0]
                    ['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
        column_metrics = [item['metric']['name'] for item in response['reports'][0]
                        ['columnHeader']['metricHeader']['pivotHeaders'][0]['pivotHeaderEntries']]
        array = np.concatenate((np.array(top_header),
                                np.array(column_metrics).reshape((len(column_metrics),1))),
                            axis = 1)
        column_index = pd.MultiIndex.from_arrays(np.transpose(array))
        # create row index
        row_index_names = response['reports'][0]['columnHeader']['dimensions']
        row_index = [ element['dimensions'] for element in response['reports'][0]['data']['rows']]
        row_index_named = pd.MultiIndex.from_arrays(np.transpose(np.array(row_index)),
                                                    names = np.array(row_index_names))
        # combine into a dataframe
        return pd.DataFrame(data = np.array(pivot_values),
                        index = row_index_named,
                        columns = column_index).astype('float')
