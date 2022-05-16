import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

class GoogleSheets:
    # instalar:
    # pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    def _credentials(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('./update_enrol_user/credentials/token.json'):
            creds = Credentials.from_authorized_user_file('./update_enrol_user/credentials/token.json', SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    './update_enrol_user/credentials/client_secret.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('./update_enrol_user/credentials/token.json', 'w') as token:
                token.write(creds.to_json())
        return creds

    def service(self):
        listDataSheet = []
        creds = self._credentials()
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
        else:
           
            for row in values:
               
                # Print columns A and E, which correspond to indices 0 and 4.
                # Verificar e salvar os indicies inciciaris para orientar e criar as chaves do discionario
                if row == values[0]:
                    indices = row
                else:
                    dictDataSheet = {}
                    for indice, value in enumerate(indices):
                        if indice < len(row):
                            dictDataSheet[value] = row[indice]
                        else:
                            dictDataSheet[value] = ''
                    listDataSheet.append(dictDataSheet)

                # print(row)
                # print('%s, %s' % (row[0], row[4]))
        
        return listDataSheet
