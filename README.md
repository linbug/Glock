Glock
=====

Clock in and out of google calendar events from the command line 

## **Usage**

* `track "your event"`  : starts timer for your event; untracks any previously tracking events
* `untrack `            : ends timer; sends event to google calendar 

## **Configuration**

Change "your_email@gmail.com" to your email address (or your preferred calendar address, if you have more than one calendar)
Google will ask you for authorisation the first time you use it. Then forever after your login details will be stored in the mysterious "calendar.dat" file somewhere on your hard drive....

## **Requirements**

* Mac OSX or Linux 
* Python packages: tempfile, os.path, time, rfc3339, os, httplib2, apiclient, oauth2client, sys
