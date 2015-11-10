Glock
=====

Clock in and out of google calendar events from the command line

## **Usage**

* `track "your event"`  : starts timer for your event; untracks any previously tracking events
* `untrack `            : ends timer; sends event to google calendar

## **Configuration**

Change "your_email@gmail.com" to your email address (or your preferred calendar address, if you have more than one calendar).
Google will ask you for authorisation the first time you use it. Then forever after your login details will be stored in the mysterious "calendar.dat" file in your home directory. This path can be set manually by changing the `le_rue_de_calendardat` variable.

You also need to link "track" and "untrack" to running the script, by adding the following to your .bash_profile:

* alias untrack='/path/to/googlecal_functional.py untrack'
* alias track='/path/to/googlecal_functional.py track'

and put them both in your $PATH.

## **Requirements**

* Python 3 (if you're using Python 2, you can set up a virtual environment)
* OS X or GNU/Linux
* Python packages:
  * [strict-rfc3339](https://pypi.python.org/pypi/strict-rfc3339)
  * apiclient, oauth2client, httplib2 ([get them all for Python 3](https://github.com/enorvelle/GoogleApiPython3x))
  * built-in libraries: tempfile, os, sys, argparse
