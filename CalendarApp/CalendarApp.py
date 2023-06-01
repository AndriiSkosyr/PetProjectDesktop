from __future__ import print_function


import sys
import formatConverter
import whisper
import summarizing_app
import emailApp

from datetime import datetime
from os import scandir
import os
import datetime
import os.path
from dateutil import tz
import pytz

from jproperties import Properties
from dateutil import parser
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

configs = Properties()

with open('app_config.properties', 'rb') as config_file:
    configs.load(config_file)

utc = pytz.UTC


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        beginDate = (datetime.datetime.today() - datetime.timedelta(days=1)).isoformat() + 'Z'  # 'Z' indicates UTC time
        endDate = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

        events_result = service.events().list(calendarId='primary', timeMin=beginDate,
                                              timeMax=endDate,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            end = event['end'].get('dateTime', event['end'].get('date'))
            date_format = '%Y-%m-%d %H:%M:%S%z'
            # start_obj = parser.parse(start)
            # end_obj = parser.parse(end)
            with os.scandir(configs.get("PATH").data) as entries:
                for entry in entries:
                    print(entry.name)
                    create_time = os.path.getctime(configs.get("PATH").data + entry.name)
                    print('Create_time: ', create_time)
                    create_date = datetime.datetime.fromtimestamp(create_time)
                    # start_obj = start_obj.replace(tzinfo=pytz.UTC)
                    # end_obj = end_obj.replace(tzinfo=pytz.UTC)

                    print('Created on:', create_date, ' StartGoogle: ', start, ' EndGoogle: ', end)

                    # print('Created on:', create_date, ' StartGoogle: ', start_obj, ' EndGoogle: ', end_obj)

                    # print('Comparing: ', create_date < start_obj)

                    if(True):
                        with os.scandir(configs.get("PATH").data + entry.name + '/') as audios:
                            for audiofile in audios:
                                initialAudiofileName = configs.get("PATH").data + entry.name + '/' + audiofile.name
                                destinationAudiofileName = initialAudiofileName.replace('m4a', 'wav')
                                formatConverter.formatting(initialAudiofileName, destinationAudiofileName)
                                text = whisper.get_transcription_whisper(destinationAudiofileName)
                                summary = summarizing_app.summarize_text(text)
                                emailApp.send_simple_message('akaciand29@gmail.com', 'Summary of the meeting ' + entry.name, summary)

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()
