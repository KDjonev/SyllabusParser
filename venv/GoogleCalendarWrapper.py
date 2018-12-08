from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from datetime import datetime, timedelta


def AddEvent(eventTitle, dateEventPairs):
    # Refer to the Python quickstart on how to setup the environment:
    # https://developers.google.com/calendar/quickstart/python
    # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
    # stored credentials.
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    for date, event in dateEventPairs:
        start = str(date).replace(' ', 'T')
        end = str(date + timedelta(hours=8)).replace(' ', 'T')

        event = {
            'summary': eventTitle,
            'description': event,
            'start': {
                'dateTime': start,
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': end,
                'timeZone': 'America/Los_Angeles',
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = service.events().insert(calendarId='inserEmailAdressHere@gmail.com', body=event).execute()
        #print('Event created: %s' % (event.get('htmlLink')))
