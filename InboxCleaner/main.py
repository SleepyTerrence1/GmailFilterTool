from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import json
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def gmail_login():
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('gmail', 'v1', credentials=creds)
    return service

def load_filters():
    with open('InboxCleaner/filters.json', 'r') as f:
        return json.load(f)

def main():
    service = gmail_login()
    filters = load_filters()
    print("Filters loaded:", filters)
    # TODO: Add Gmail fltering/preview/deletion logic here

if __name__ == '__main__':
    main()