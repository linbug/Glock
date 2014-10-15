Glock
=====

Clock in and out of google calendar events from the command line

## **Usage**

* `track "your event"`  : starts timer for your event; untracks any previously tracking events
* `untrack `            : ends timer; sends event to google calendar

## **Configuration**

Change "your_email@gmail.com" to your email address (or your preferred calendar address, if you have more than one calendar)
Google will ask you for authorisation the first time you use it. Then forever after your login details will be stored in the mysterious "calendar.dat" file somewhere on your hard drive....
You also need to link "track" and "untrack" to running the script:

* `ln -s /path/to/googlecal_functional.py track`
* `ln -s /path/to/googlecal_functional.py untrack`

and put them both in your $PATH.

## **Requirements**

* OS X or GNU/Linux
* Python packages:
  * [strict-rfc3339](https://pypi.python.org/pypi/strict-rfc3339)
  * apiclient, oauth2client, httplib2 ([get them all for Python 3](https://github.com/enorvelle/GoogleApiPython3x))
  * built-in libraries: tempfile, os, sys, argparse
