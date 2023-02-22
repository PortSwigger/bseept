# BSEEPT: Burp Suite Enterprise Edition Power Tools

A command line utility and Python client library for Burp Suite Enterprise Edition's (https://portswigger.net/burp/enterprise) GraphQL API allowing you to query and configure.
* https://portswigger.net/burp/documentation/enterprise/api-documentation/graphql-api
* https://portswigger.net/burp/extensibility/enterprise/graphql-api/

All output returned is in JSON format which can be parsed and pretified by piping through `jq` and similar

## Features

This tool is currently work in progress. The following lists track the implemented versus to do features.

### Implemented

- [x] Get sites via `--getsites`
- [x] Get folders via `--getfolders`
- [x] Get site tree via `--getsitetree`
- [x] Get scans via `--getscans`
- [x] Get scan configurations via `--getscanconfigs`
- [x] Get scan issues via `--getscanissues`
- [x] Get scan report in HTML via `--getscanreport`
- [x] Get scan report in XML via `--getscanreportxml`
- [x] Get agents via `--getagents`
- [x] Get unauthorized agents via `--getunauthorizedagents`
- [x] Get agentpools via` --getagentpools`
- [x] Get schedule via `--getschedule`
- [x] Get extensions via `--getextensions`
- [x] Create site via `createsite`
- [x] Delete site via `deletesite`
- [x] Rename site via `renamesite`
- [x] Move site via `movesite`
- [x] Add scan via `addscanschedule`
- [x] Delete scan schedule via `deletescanschedule`
- [x] Update scan schedule via `updatescanschedule`
- [x] Create folder via `createfolder`
- [x] Delete folder via `deletefolder`
- [x] Rename folder via `renamefolder`
- [x] Move folder via `movefolder`
- [x] Rename agent via `renameagent`
- [x] Enable agent via `enableagent`
- [x] Disable agent via `disableagent`
- [x] Update agent maximum concurrent scans via `updateagentmaxconcurrentscans`

### To Do
- [ ] Update scan config via `updatescanconfig`
- [ ] Update site extensions via `updatesiteextensions`
- [ ] Create site login credentials via`createsitelogincredentials`
- [ ] Update site login credentials via `updatesitelogincredentials`
- [ ] Delete site login credentials via `deletesitelogincredentials`
- [ ] Create scan config via `createscanconfig`
- [ ] Update scan config via `updatescanconfig`
- [ ] Delete scan config via `deletescanconfig`
- [ ] Upload BApp via `uploadbapp`
- [ ] Get BApp details via `getbappdetails`
- [ ] Upload extension via `uploadextension`
- [ ] Update extension name via `updateextensionname`
- [ ] Update extension description via `updateextensiondescription`
- [ ] Update extension JAR via `updateextensionjar`
- [ ] Delete extension via `deleteextension`
- [ ] Authorize agent via `authorizeagent`
- [ ] Deauthorize agent via `deauthorizeagent`
- [ ] Create agent pool via `createagentpool`
- [ ] Update agent pool via `updateagentpool`
- [ ] Move agent pool via `moveagentpool`
- [ ] Delete agent pool via `deleteagentpool`
- [ ] Assign site to agent pool via `assignsitetogentpool`

## Authentication Configuration

You can configure authentication with the API key to work in one of two ways. Either via environment variables (i.e. setting the URL and/or API via specific variables) or by supplying the command line.

via environment variables example on Windows:
```
set BSEEURL=https://my.bsee.server/
set BSEEAPIKEY=MYAPIKEY
```

via command line
```
py bseept.py --url https://my.bsee.server/ --apikey MYAPIKEY --getsites
```


## Help

The following is the help output from the tool

```
# py bseept.py --help
usage: bseept [-h] [-u URL] [--apikey APIKEY] [--getsites] [--getfolders] [--getsitetree] [--getscans] [--getscanconfigs] [--getscanissues GETSCANISSUES] [--getscanreport GETSCANREPORT] [--getscanreportxml GETSCANREPORTXML] [--getschedule] [--getagents] [--getagentpools]
              [--getunauthorizedagents] [--getextensions]
              {createsite,deletesite,renamesite,movesite,updatesitescanconfig,updatesitescope,updatesiteextensions,createsitelogincredentials,updatesitelogincredentials,deletesitelogincredentials,createsiterecordedlogincredentials,updatesiterecordedlogincredentials,deletesiterecordedlogincredentials,addscanschedule,updatescanschedule,deletescanschedule,createscanconfig,updatescanconfig,deletescanconfig,uploadbapp,getbappdetails,uploadextension,updateextensionname,updateextensiondescription,updateextensionjar,deleteextension,authorizeagent,deauthorizeagent,enabledisableagent,renameagent,enableagent,disableagent,updateagentmaxconcurrentscans,createagentpool,updateagentpool,moveagentpool,deleteagentpool,assignsitetogentpool,createfolder,deletefolder,renamefolder,movefolder,updatefalsepositive}
              ...

Burp Suite Enterprise Edition Power Tools

positional arguments:
  {createsite,deletesite,renamesite,movesite,updatesitescanconfig,updatesitescope,updatesiteextensions,createsitelogincredentials,updatesitelogincredentials,deletesitelogincredentials,createsiterecordedlogincredentials,updatesiterecordedlogincredentials,deletesiterecordedlogincredentials,addscanschedule,updatescanschedule,deletescanschedule,createscanconfig,updatescanconfig,deletescanconfig,uploadbapp,getbappdetails,uploadextension,updateextensionname,updateextensiondescription,updateextensionjar,deleteextension,authorizeagent,deauthorizeagent,enabledisableagent,renameagent,enableagent,disableagent,updateagentmaxconcurrentscans,createagentpool,updateagentpool,moveagentpool,deleteagentpool,assignsitetogentpool,createfolder,deletefolder,renamefolder,movefolder,updatefalsepositive}
                        modify commands
    createsite          Create a site
    deletesite          Delete a site
    renamesite          Rename a site
    movesite            Move a site
    updatesitescanconfig
                        Update a site scan configuration
    updatesitescope     Update a site scope
    updatesiteextensions
                        Update a site extensions
    createsitelogincredentials
                        Create a sites login credentials
    updatesitelogincredentials
                        Update a sites login credentials
    deletesitelogincredentials
                        Delete a sites login credentials
    createsiterecordedlogincredentials
                        Create a sites recorded login credentials
    updatesiterecordedlogincredentials
                        Update a sites recorded login credentials
    deletesiterecordedlogincredentials
                        Delete a sites recorded login credentials
    addscanschedule     Add a scan schedule
    updatescanschedule  Update a scan schedule
    deletescanschedule  Delete a scan
    createscanconfig    Create a scan configuration
    updatescanconfig    Update a scan configuration
    deletescanconfig    Delete a scan configuration
    uploadbapp          Upload a BApp
    getbappdetails      Get BApp details without adding it to thelist of usable extensions
    uploadextension     Upload a custom extension
    updateextensionname
                        Update a custom extension name
    updateextensiondescription
                        Update a custom extension description
    updateextensionjar  Update a custom extension JAR
    deleteextension     Delete a custom extension or BApp
    authorizeagent      Authorize a new agent to be able to run scans
    deauthorizeagent    Deauthorize an existing agent from running scans
    enabledisableagent  Enable or disable an existing agent
    renameagent         Rename an existing agent
    enableagent         Enable an existing agent
    disableagent        Disable an existing agent
    updateagentmaxconcurrentscans
                        Update the maximum number of concurrent scans this agent host can run
    createagentpool     Create an agent pool
    updateagentpool     Update an agent pool
    moveagentpool       Move an agent pool
    deleteagentpool     Delete an agent pool
    assignsitetogentpool
                        Assign sites to an agent pool
    createfolder        Create a folder
    deletefolder        Delete a folder
    renamefolder        Rename a folder
    movefolder          Move a folder
    updatefalsepositive
                        Update the false positive for an issue

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Burp Suite Enterprise Edition URL
  --apikey APIKEY       Burp Suite Enterprise Edition API key
  --getsites            Configured all configured sites
  --getfolders          Configured folders in BSEE
  --getsitetree         Configured site tree in BSEE
  --getscans            Configured all configured scans
  --getscanconfigs      Get all scan configuration definitions
  --getscanissues GETSCANISSUES
                        Get scan issues specified by the supplied scan ID
  --getscanreport GETSCANREPORT
                        Get scan HTML report specified by the supplied scan ID
  --getscanreportxml GETSCANREPORTXML
                        Get scan XML report specified by the supplied scan ID
  --getschedule         Scan schedules
  --getagents           Configured scan agents
  --getagentpools       Configured scan agent pools
  --getunauthorizedagents
                        Get the curretly unauthorized agents
  --getextensions       Extensions installed

with 🧡 from PortSwigger
```


## Examples

The following are example uses cases.

### Creating a site
```
 > py bseept.py createsite --sitename MyTestSite --scanconfigurationid ba4f8ce0-af9a-4450-ad35-78f083375088 --siteurls https://ginandjuice.shop
 {"data": {"create_site": {"site": {"id": "46", "parent_id": "0", "scope": {"included_urls": ["https://ginandjuice.shop"], "protocol_options": "USE_SPECIFIED_PROTOCOLS"}, "application_logins": {"login_credentials": [], "recorded_logins": []}, "scan_configurations": [{"id": "ba4f8ce0-af9a-4450-ad35-78f083375088"}]}}}}
 ```
 
 ### Creating a scan from a site and parse the response via jq to prettyfi
 ```
> py bseept.py addscanschedule --siteid 1 --initialruntime 2024-08-19T11:07:25.664Z --schedule FREQ=DAILY;INTERVAL=2 --scanconfigurationids ba4f8ce0-af9a-4450-ad35-78f083375088 | c:\data\utils\jq
{
  "data": {
    "create_schedule_item": {
      "schedule_item": {
        "id": "27",
        "schedule": {
          "initial_run_time": "2024-08-19T11:07:25.664Z",
          "rrule": "FREQ=DAILY;INTERVAL=2"
        },
        "scan_configurations": [
          {
            "id": "ba4f8ce0-af9a-4450-ad35-78f083375088",
            "name": "Audit coverage - maximum"
          }
        ]
      }
    }
  }
}

 ```
 
 ### Get the extensions and parse via jq to prettyfi
 ```
 > py bseept.py --getextensions | c:\data\utils\jq
 {
  "data": {
    "extensions": [
      {
        "id": "526b9b32-9a0c-4a7a-9d73-60cfb53ad408",
        "uploaded_filename": "9cff8c55432a45808432e26dbb2b41d8 (1).bapp",
        "name": "Backslash Powered Scanner",
        "description": "Finds unknown classes of injection vulnerabilities.",
        "uploaded_date": "2022-11-02T13:48:53.774Z",
        "uploaded_by": "administrator",
        "bapp_details": {
          "bapp_uuid": "9cff8c55432a45808432e26dbb2b41d8",
          "author": "James 'albinowax' Kettle, PortSwigger Web Security",
          "version": "1.21"
        }
      },
      {
        "id": "034657cc-0f31-44b0-8d0a-b9a57627818e",
        "uploaded_filename": "test-custom-extension.jar",
        "name": "test-custom-extension.jar",
        "description": "Adds an issue to a scan",
        "uploaded_date": "2023-02-08T15:41:25.471Z",
        "uploaded_by": "administrator",
        "bapp_details": null
      }
    ]
  }
}
 ```
 
 ## Get the extensions and parse via jq to extract just the names
 ```
 > py bseept.py --getextensions | c:\data\utils\jq ".[].extensions[] | .name" | more
"Backslash Powered Scanner"
"test-custom-extension.jar"
 ```
 
 ### Get the scheduled scans and parse via jq to prettyfi
 ```
 > py bseept.py --getschedule | c:\data\utils\jq | more
{
  "data": {
    "schedule_items": [
      {
        "id": "1",
        "site": {
          "id": "1",
          "name": "Gin & Juice"
        },
        "schedule": {
          "initial_run_time": "2022-09-02T13:51:14.550Z",
          "rrule": "FREQ=DAILY;INTERVAL=2"
        },
        "has_run_more_than_once": true,
        "scheduled_run_time": "2023-02-21T13:51:14.000Z"
      }
    ]
  }
}
```

### Delete a scheduled scan
```
> py bseept.py deletescanschedule --scanid 25
{"data": {"delete_schedule_item": {"id": "25"}}}
```

## API Examples
The following will use the Python client library for various things. This can be found in `bseept-client-library-example.py`

```python
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


    # Example 3
    #  - we tell the API to return the resulting JSON and then print it
    #  - note: the API will by default also print the results itself as we don't specifically say what to do
    print("\n\n--- Example 3a\n\n")
    ret = bseeptsites.getsites(apiurl,BSEEAPIKEY,output = True)
    print(json.dumps(ret))

# Entry point
if __name__ == '__main__':
    main()

```


