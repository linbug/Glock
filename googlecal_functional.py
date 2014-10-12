#!/usr/bin/env python2
le_nom_de_calendrier = "your_email@gmail.com"

def make_filename():
    import tempfile
    import os.path
    return os.path.join(tempfile.gettempdir(),"glockfile.txt")
le_rue_de_fichier = make_filename()

le_clef_dapi = '22808445872-fkcaacm3fa4ponpto1nnech8154f65me.apps.googleusercontent.com'
le_secret_de_client = '0IzXQ9JqGOv_w5i7YeJVzNG_'

def gcal (label):
    """Write the thing you want to track, or None for untrack"""
    untrack()
    if label is not None:
        track(label)

def untrack():
    """end the currently tracked label (if it exists) and send the event to gcal; then delete the file"""
    contents = read_file()
    if contents is not None:
        (start, label) = contents
        end = now()
        event = make_event (start, end, label)
        send(event)
    erase_file()

def track(label):
    """put the label and the current time into the file"""
    start = now()
    write_file(start, label)

def now():
    """the current time point"""
    import time
    from rfc3339 import rfc3339
    return str(rfc3339(time.time()))

def read_file():
    """open the file and return the timestamp and event name as a tuple"""
    try:
        with open (le_rue_de_fichier) as f:
            lines = f.readlines()
            if len(lines) == 2:
                return lines [0].strip(), lines[1]
            else:
                print "File contents in the wrong format"
                return None
    except:
        print "No file found"
        return None
        
     

def erase_file():
    """erase the file"""
    try:
        import os
        os.remove(le_rue_de_fichier)
    except:
        return None

def write_file(start, label):
    """make a file and write in it the start time and event name"""
    with open (le_rue_de_fichier, 'w') as f:
        f.writelines ([start, "\n", label])

def make_event(start, end, label):
    """this makes an event in gcal format"""
    return {
    'summary': label,
    'start': {'dateTime': start},
    'end': {'dateTime': end}
    }

def send(event):
    """send your event to google calendar!!!"""

    import httplib2
    from apiclient.discovery import build
    from oauth2client.file import Storage
    from oauth2client.client import OAuth2WebServerFlow
    from oauth2client.tools import run

    FLOW = OAuth2WebServerFlow(
        client_id= le_clef_dapi,
        client_secret= le_secret_de_client,
        scope='https://www.googleapis.com/auth/calendar',
        user_agent='GoogleCalendarApp/1.0')

    storage = Storage('calendar.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid == True:
        credentials = run(FLOW, storage)

    http = httplib2.Http()
    http = credentials.authorize(http)

    service = build(serviceName='calendar', version='v3', http=http, developerKey = le_clef_dapi)

    service.events().insert(calendarId= le_nom_de_calendrier, body=event).execute()
    print "Event successfully logged"

import sys
if sys.argv[0] == "track":
    gcal(sys.argv[1])
else:
    gcal(None)
