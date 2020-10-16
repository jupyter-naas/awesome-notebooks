# Google Spreadsheet

### Google API's:

- Google drive API
- Google sheets API

### Google API credentials JSON:

- Step 1: Login to Google developers console
- Step 2: Enable Google Drive API and Google Sheets API
- Step 3: Create credentials for Google Drive API and download as JSON

Note: This credentials json file is passed as a parameter to the python class "GoogleSpreadsheet" 

### Install PIP package inside virtual environment
```sh
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
### Executing Google Spreadsheet connector
```python
from google_spreadsheet import GoogleSpreadsheet
instance = GoogleSpreadsheet(spreadsheet_id='1KOIw9H_FdN81iJw8ENeXm3aFt_R77N2DnJBwx_lWUiU',sheet_name='companylist',credentials_json_path='client_secret.json')
```
### GoogleSpreadsheet class arguments:
- spreadsheet_id = Google spreadsheet ID you wish to access
- sheet_name = Spreadsheet may contain many sheets. Mention the sheet name you wish to access.
- credentials_json_path = Credentials JSON file for Google drive API, downloded from Google developers console 

## Authentication and Authorization:
- For first time,Script redirects to google accounts URL for sign in and asking consern on accessing the google spreadsheets

## Sample Credentials JSON:

{
	"installed":
				{
					"client_id":"",
					"project_id":"",
					"auth_uri":"",
					"token_uri":"",
					"auth_provider_x509_cert_url":"",
					"client_secret":"",
					"redirect_uris":[]
				}
}