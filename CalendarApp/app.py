import os
import datetime
import google.auth
from googleapiclient.discovery import build

# Load credentials from file
credentials_path = 'client_secret_338986250703-egjuthgkbhi05hj4uvump7gcop4g600t.apps.googleusercontent.com.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

# Authenticate and create the Calendar service
credentials, project = google.auth.default()
service = build('calendar', 'v3', credentials=credentials)

# Get the list of events from the primary calendar
now = datetime.datetime.utcnow().isoformat() + 'Z'  # Current time in UTC
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

# Print the events
if not events:
    print('No upcoming events found.')
for event in events:
    start = event['start'].get('dateTime', event['start'].get('date'))
    print(start, event['summary'])
