from main import*
cred = Creds()
print(cred.update(SAMPLE_SPREADSHEET_ID, 'Лист1!A1:A2', 'RAW', [['Xyi'],['2']]))
