from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import logging


class BigQueryConnector:
    def __init__(self, service_account_file, project_id):
        self.service_account_file = service_account_file
        self.project_id = project_id

        self.connection = self.get_connection()

    @property
    def _logger(self):
        return logging.getLogger(__name__)

    def get_connection(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(self.service_account_file)
            ctx = bigquery.Client(credentials=credentials, project=self.project_id)
            self._logger.info("Connection established")
            return ctx
        except Exception as e:
            self._logger.error(e)

    def execute_query(self, query):
        try:
            df = self.connection.query(query).to_dataframe()

            if not df.empty:
                return df
            else:
                return True
        except Exception as e:
            self._logger.error(e)
            return False

    def load_data_from_csv(self, dataset, table, csv_file):
        df = pd.read_csv(csv_file)

        dataset_ref = self.connection.dataset(dataset)
        table_ref = dataset_ref.table(table)

        self.connection.load_table_from_dataframe(df, table_ref).result()