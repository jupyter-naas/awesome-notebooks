from __future__ import print_function
import pickle
import os.path
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import yahoo_financials

class GoogleSheet():
    
    def __init__(self,key, sheet_name):
        self.sata = []
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
        client = gspread.authorize(creds)
        self.book = client.open_by_key(key)
        sheets = self.book.worksheets()
        for sheet in sheets:
            if sheet.title == sheet_name:
                self.data =  sheet.get_all_records()
        
    def get_yahoo_symbols(self):
        symbols = []
        for row in self.data:
            if "YAHOO_SYMBOL" in row and row['YAHOO_SYMBOL']:
                symbols.append(row['YAHOO_SYMBOL'])
        return symbols
    def create_sheet(self,df,name):
        df.fillna('', inplace=True)
       
        shape = df.shape
        sheets = self.book.worksheets()
        worksheet = None
        for sheet in sheets:
            if sheet.title == name:
                worksheet = sheet  
        if not worksheet:
            print("creating ", name)
            worksheet = self.book.add_worksheet(title=name,rows=shape[0], cols=shape[1])
        worksheet.update([df.columns.values.tolist()[1:]] + [row[1:] for row in  df.values.tolist()])
def main(sheet_id,input_sheet_name, out_sheet_name):
    sheet_obj = GoogleSheet(sheet_id,input_sheet_name)
    symbols = sheet_obj.get_yahoo_symbols()
    exported_name = yahoo_financials.main(symbols)
    df = pd.read_excel(exported_name) 
    sheet_obj.create_sheet(df, out_sheet_name) 
    print("created data in google sheet")
    os.remove(exported_name)
if __name__ == '__main__':
    out_sheet_name = "COMPANIES_FINANCIALS"
    sheet_id = "10bmjq_bxj03WcQ11QPkE15HRQWZgWgz99mZSEIL5Hq0"
    input_sheet_name =  "TARGET_COMPANIES"
    main(sheet_id,input_sheet_name, out_sheet_name)  