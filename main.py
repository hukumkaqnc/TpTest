import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1bZuEfz7QU8x8a9dKbg1yDTlgXW5tB3qJRQe2QUf18Mk"
groups_list = ['1 курс ПИ-С-22',' 2 курс ПИ-С-21  ', '3 курс ПИ-С-20', '4 курс ПИ-С-19']
groups_list1 = ['1 курс Прог-С-22', '3 курс Прог-С-20', '2 курс Прог-С-21  ', '2 курс Прог-СПО-21', '3 курс Прог-СПО-20', '4 курс Прог-С-19', '4 курс Прог-С-19 ИУПы']
SAMPLE_RANGE_NAME = "A1:A2"



class Creds():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  def __init__(self):

    self.creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
      self.creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not self.creds or not self.creds.valid:
      if self.creds and self.creds.expired and self.creds.refresh_token:
        self.creds.refresh(Request())
      else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        self.creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open("token.json", "w") as token:
        token.write(self.creds.to_json())
  def get(self, spr_id, range_name):
    service = build("sheets", "v4", credentials=self.creds)
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=spr_id, range=range_name)
        .execute()
    )
    values = result.get("values", [])
    return result
  def batch(self, spr_id, range_names, md='ROWS'):
    service = build("sheets", "v4", credentials=self.creds)
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .batchGet(spreadsheetId=spr_id, ranges=range_names, majorDimension = md)
        .execute()
    )

    return result
  def update(self, spr_id, range_name, value_input, values):
    service = build("sheets", "v4", credentials=self.creds)
    sheet = service.spreadsheets()
    body = {"values": values}
    result = (
        sheet.values()
        .update(
            spreadsheetId=spr_id,
            range=range_name,
            valueInputOption=value_input,
            body=body,
        )
        .execute()
    )
    return result

  