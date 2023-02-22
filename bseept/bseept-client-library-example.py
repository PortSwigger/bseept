
#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#


# Client library example

import os
import sys
import json

import bseeptsites


# Main function
def main():

    # Host URL
    BSEEURL = os.getenv('BSEEURL')
    if(BSEEURL is None):
        sys.stderr.write("Need to specify the BSEE URL either in the environment variable BSEEURL")
        exit()
    else:
        apiurl = BSEEURL
        apiurl = apiurl.rstrip('/')
        if(apiurl.startswith("https://") is not True):
            sys.stderr.write("Supplied URL does not begin with https:// as required")
            exit()

    # API key
    BSEEAPIKEY = os.getenv('BSEEAPIKEY')
    if(BSEEAPIKEY is None):
        sys.stderr.write("Need to specify the BSEE API key either in the environment variable BSEEAPIKEY")
        exit()

    # Example 1
    #   - we tell the API to not print itself
    #   - we tell the API to return the resulting JSON to our variable
    #   - we then print the JSON
    print("\n\n--- Example 1\n\n")
    ret = bseeptsites.getsites(apiurl,BSEEAPIKEY,doprint = False, output = True)
    print(json.dumps(ret))

    # Example 2
    #  - we tell the API to print itself
    #  - we tell the API to not return the resulting JSON
    print("\n\n--- Example 2\n\n")
    bseeptsites.getsites(apiurl,BSEEAPIKEY,doprint = True, output = False)

# Entry point
if __name__ == '__main__':
    main()
