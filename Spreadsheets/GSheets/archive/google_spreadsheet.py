from __future__ import print_function
import pickle
import os.path
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request



class GoogleSpreadsheet:

    def __init__(self,spreadsheet_id=None,sheet_name=None,credentials_json_path=None):
        """ Scopes are various types of access(read,write,readonly etc.) specified to the Google API
            Incase of scope modification, delete the file token.pickle
        """
        try:
        	assert spreadsheet_id is not None,"Please provide a spreadsheet id"
        	assert sheet_name is not None,"Please provide a sheet name "
        	assert credentials_json_path is not None,"Please provide credentials JSON file path"
        except AssertionError:
        	print("Mising one or more arguments.Please provide all arguments")
        	return
        if not os.path.exists(credentials_json_path):
        	print("Invalid path to credentials JSON file")
        	return

        # SpreadsheetID
        self.SPREADSHEET_ID = spreadsheet_id
        # Spreadsheet Name
        self.SHEET_NAME = sheet_name
        # Goodle drive credentials JSON file
        self.credentials_json = credentials_json_path

        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        # Establish connection to google sheet's API
        connection = self.get_connection()
        #Check if connection is established
        if(connection):
            """ If connection is positive
                Get data from spreadsheet
            """
            if(not self.get_data(connection)):
                print("Failed to get data from sheet")
        else:
            print("Failed to connect to Google Spreadsheet")


    def get_connection(self):
        try:
            """ This Method uses the credentials.json file to establish connection with 
                google spreadsheet API.
            """
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_json, self.SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            return sheet

        except Exception as e:
            return False

    def get_data(self,sheet):
        try:
            result = sheet.values().get(spreadsheetId=self.SPREADSHEET_ID,
                                range=self.SHEET_NAME).execute()
            # values = result.get('values', [])

            header = result.get('values', [])[0]   # Assumes first line is header!
            values = result.get('values', [])[1:]  # Everything else is data.
            if not values:
                print('No data found.')
            else:
                all_data = []
                for col_id, col_name in enumerate(header):
                    column_data = []
                    for row in values:
                        column_data.append(row[col_id])
                    ds = pd.Series(data=column_data, name=col_name)
                    all_data.append(ds)
                df = pd.concat(all_data, axis=1)
                print("Dataframe:\n",df)
                return True
        except Exception as e:
            return False

if __name__ == '__main__':
    instance = GoogleSpreadsheet(spreadsheet_id='1KOIw9H_FdN81iJw8ENeXm3aFt_R77N2DnJBwx_lWUiU',sheet_name='companylist',credentials_json_path='client_secret.json')
    