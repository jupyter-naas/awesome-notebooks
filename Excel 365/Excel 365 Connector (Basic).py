import os

import sharepy
import pandas as pd

class SharepointConnector:
    def __init__(self, username, password, domain):
        self.domain = domain
        self.sharepoint = sharepy.connect(self.domain, username=username, password=password)
 
    def get_df(self, path, sheet, export):
        out_dir = "../data_output"
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)
        out_file = out_dir+'/tmp.xlsx'
        api_path  =  "/".join(path.split("/")[0:5])
        file_path = "/".join(path.split("/")[3:])
        api_url_tpl = "{api_path}/_api/web/GetFileByServerRelativeUrl('/{file_path}')/$value"
        api_url = api_url_tpl.format(api_path=api_path, file_path=file_path)
        self.sharepoint.getfile(api_url, filename = out_file)
        df = pd.read_excel(out_file, sheet)
        os.remove(out_file)
        name = path.split("/")[-1].split(".")[0]
        if export in ["xls", "xlsx"]:
            df.to_excel(out_dir+"/"+name+".xlsx")
        elif export == "csv":
            df.to_csv(out_dir+"/"+name+".csv")
        return df




def connect(username,password,domain,path, sheet, export = False):
    try:
        sharepoint_obj = SharepointConnector(username,password,domain)
    except:
        print("authentication failed . please check username and password")
        return ""
    try:
        df =  sharepoint_obj.get_df(path, sheet,export)
        print("data frame generated")
        return df
    except :
        print("did not get dataframe from given path. please check the path")

if __name__ == '__main__':
    password="9aXgzH2DRqKCCU8z"
    username="jeremy.ravenel@cashstory.com"
    domain = "cashstory.sharepoint.com"
    sheet = "Forecast"
    path = "https://cashstory.sharepoint.com/sites/cashstory-external/Documents%20partages/CashStory%20Forecasting%20Module/Forecast.xlsx"
    df = connect(username,password,domain, path,sheet)
    df = connect(username,password,domain, path,sheet,"xlsx")
    df = connect(username,password,domain, path,sheet,"csv")
    print(df)