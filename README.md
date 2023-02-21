# BSEEPT
Burp Suite Enterprise Edition Power Tools

## Features

### Implemented

- [x] Get sites via --getsites
- [x] Get site tree via --getsitetree
- [x] Get scans via --getscans
- [x] Get scan configurations via --getscanconfigs
- [x] Get scan issues via --getscanissues
- [x] Get scan report in HTML via --getscanreport
- [x] Get scan report in XML via --getscanreportxml
- [x] Get agents via --getagent
- [x] Get agentpools via --getagentpools
- [x] Get schedule via --getschedule
- [x] Get extensions via `--getextensions`
- [x] Create site via `createsite`
- [x] Delete site via `deletesite`


### To do

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


## Help
```
# py bseept.py --help
usage: bseept [-h] [-u URL] [--apikey APIKEY] [--getsites] [--getfolders] [--getsitetree] [--getscans] [--getscanconfigs] [--getscanissues GETSCANISSUES] [--getscanreport GETSCANREPORT]
              [--getscanreportxml GETSCANREPORTXML] [--getschedule] [--getagents] [--getagentpools] [--getextensions]
              {createsite,deletesite,renamesite,movesite,updatesitescanconfig,updatesitescope,updatesiteextensions,createsitelogincredentials,updatesitelogincredentials,deletesitelogincredentials,createsiterecordedlogincredentials,updatesiterecordedlogincredentials,deletesiterecordedlogincredentials,addscanschedule,updatescanschedule,deletescanschedule,createscanconfig,updatescanconfig,deletescanconfig,uploadbapp,getbappdetails,uploadextension,updateextensionname,updateextensiondescription,updateextensionjar,deleteextension,authorizeagent,deauthorizeagent,enabledisableagent,renameagent,updateagentmaxconcurrentscans,createagentpool,updateagentpool,moveagentpool,deleteagentpool,assignsitetogentpool,createfolder,renamefolder,deletefolder,updatefalsepositive}
              ...

Burp Suite Enterprise Edition Power Tools

positional arguments:
  {createsite,deletesite,renamesite,movesite,updatesitescanconfig,updatesitescope,updatesiteextensions,createsitelogincredentials,updatesitelogincredentials,deletesitelogincredentials,createsiterecordedlogincredentials,updatesiterecordedlogincredentials,deletesiterecordedlogincredentials,addscanschedule,updatescanschedule,deletescanschedule,createscanconfig,updatescanconfig,deletescanconfig,uploadbapp,getbappdetails,uploadextension,updateextensionname,updateextensiondescription,updateextensionjar,deleteextension,authorizeagent,deauthorizeagent,enabledisableagent,renameagent,updateagentmaxconcurrentscans,createagentpool,updateagentpool,moveagentpool,deleteagentpool,assignsitetogentpool,createfolder,renamefolder,deletefolder,updatefalsepositive}
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
    updateagentmaxconcurrentscans
                        Update the maximum number of concurrent scans this agent host can run
    createagentpool     Create an agent pool
    updateagentpool     Update an agent pool
    moveagentpool       Move an agent pool
    deleteagentpool     Delete an agent pool
    assignsitetogentpool
                        Assign sites to an agent pool
    createfolder        Create a folder
    renamefolder        Rename a folder
    renamefolder        Move a folder
    deletefolder        Delete a folder
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
  --getextensions       Extensions installed

with 🧡 from PortSwigger
```


## Examples

### Creating a site
```
 py bseept.py createsite --sitename MyTestSite --scanconfigurationid ba4f8ce0-af9a-4450-ad35-78f083375088 --siteurls https://ginandjuice.shop
 {"data": {"create_site": {"site": {"id": "46", "parent_id": "0", "scope": {"included_urls": ["https://ginandjuice.shop"], "protocol_options": "USE_SPECIFIED_PROTOCOLS"}, "application_logins": {"login_credentials": [], "recorded_logins": []}, "scan_configurations": [{"id": "ba4f8ce0-af9a-4450-ad35-78f083375088"}]}}}}
 ```
 
 ### Get the scheduled scans and parse via jq
 ```
 py bseept.py --getschedule | c:\data\utils\jq | more
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


