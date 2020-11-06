

import lxml
from lxml import html
import requests
import pandas as pd


class ScrapData(object):
    """docstring for ScrapData"""
    def __init__(self):
        self.df = pd.DataFrame(columns=['COMPANY', 'FINANCIALS', 'LABEL',"VALUE", "DATE","SOURCE"])
        self.i = 0
        
    def get_page(self,url):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Pragma': 'no-cache',
            'Referrer': 'https://google.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }

        return requests.get(url, headers=headers)

    def parse_rows(self,table_rows):
        parsed_rows = []

        for table_row in table_rows:
            parsed_row = []
            el = table_row.xpath("./div")

            none_count = 0

            for rs in el:
                try:
                    (text,) = rs.xpath('.//span/text()[1]')
                    parsed_row.append(text)
                except ValueError:
                    parsed_row.append("")
                    none_count += 1

            if (none_count < 4):
                parsed_rows.append(parsed_row)

        pd.DataFrame(parsed_rows)
        return parsed_rows
   

    def scrape_table(self,url):
        page = self.get_page(url);
        tree = html.fromstring(page.content)
        table_rows = tree.xpath("//div[contains(@class, 'D(tbr)')]")
        assert len(table_rows) > 0
        df = self.parse_rows(table_rows)
        return df
    
    def get_cash_flow(self):
        url = "https://finance.yahoo.com/quote/{tiker}/cash-flow?p={tiker}"
        url  = url.format(tiker=self.tiker)
        return self.scrape_table(url), url
        
     
    def get_balance_sheet(self):
        url = "https://finance.yahoo.com/quote/{tiker}/balance-sheet?p={tiker}"
        url  = url.format(tiker=self.tiker)
        return self.scrape_table(url), url
    
    def get_financial(self):
        url = "https://finance.yahoo.com/quote/{tiker}/financials?p={tiker}"
        url  = url.format(tiker=self.tiker)
        return self.scrape_table(url), url
        
        
    def scrap(self,tiker):
        self.tiker = tiker
        df = self.df
        i = self.i
        result = {}
        result["cash"], url = self.get_cash_flow()
        result["balance"], url = self.get_balance_sheet()
        result["finance"], url = self.get_financial()
        cash = "Cashflow Statement"
        balance = "Balance Sheet"
        finance = "Income Statement"
        for row in result["cash"][1:]:
            for j in range(2,6):
                try:
                    df.loc[i] = [tiker,cash,row[0],row[j], result["cash"][0][j],url]
                    i = i+1
                except:
                    pass
        for row in result["balance"][1:]:
            for j in range(1,5):
                try:
                    df.loc[i] = [tiker,balance,row[0],row[j], result["balance"][0][j],url]
                    i = i+1
                except:
                    pass
        for row in result["finance"][1:]:
            for j in range(2,6):
                try:
                    df.loc[i] = [tiker,finance,row[0],row[j], result["finance"][0][j],url]
                    i = i+1
                except:
                    pass
        self.i = i
        return df
        



        

def main(symbol):
    scraper = ScrapData()
    print("please wait...")
    if type(symbol) is list:
        name = 'Bulk-financials.xlsx'
        writer = pd.ExcelWriter(name)
        for tiker in symbol:
            print("getting "+ tiker)
            result = scraper.scrap(tiker)
            #print(result)
            result.to_excel(writer,'FINANCIALS_DB')
        writer.save()
        print("file " + name + ' created')
    else:
        result = scraper.scrap(symbol)
        writer = pd.ExcelWriter(symbol + '-'+ '-financials.xlsx')
        result.to_excel(writer,'FINANCIALS_DB')
        writer.save()
        name = symbol +'-financials.xlsx'
        print("file "+ symbol +'-financials.xlsx created')
    return name


if __name__ == '__main__':
    #main("EDF.PA")
    main(["EDF.PA","TSLA"])