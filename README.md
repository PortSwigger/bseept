# BSEEPT
Burp Suite Enterprise Edition Power Tools

## Authentication Configuration

You can configure authentication to work in one of two ways. Either via environment variables or via the command line.

via environment variables 
```
set BSEEURL=https://my.bsee.server/
set BSEEAPIKEY=MYAPIKEY
```

via command line
```
py bseept.py --url https://my.bsee.server/ --apikey MYAPIKEY --getsites
```