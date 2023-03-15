# BSEEPT: Burp Suite Enterprise Edition Power Tools

A command line utility and Python client library for Burp Suite Enterprise Edition's (https://portswigger.net/burp/enterprise) GraphQL API allowing you to query and configure.
* https://portswigger.net/burp/documentation/enterprise/api-documentation/graphql-api
* https://portswigger.net/burp/extensibility/enterprise/graphql-api/

All output returned is in JSON format which can be parsed and pretified by piping through `jq` and similar

## Features

The following lists track the implemented versus to do features.

Please raise any bugs / feature requests as issues so they can be resolved.

E-mail with any questions / feedback to `ollie.whitehouse at portswigger [.] net`

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
- [x] Update site extensions via `updatesiteextensions`
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
- [x] Create agent pool via `createagentpool`
- [x] Update agent pool via `updateagentpool`
- [x] Delete agent pool via `deleteagentpool`
- [x] Update extension name via `updateextensionname`
- [x] Update extension description via `updateextensiondescription`
- [x] Upload extension via `uploadextension`
- [x] Update extension JAR via `updateextensionjar`
- [x] Delete extension via `deleteextension`
- [x] Upload BApp via `uploadbapp`
- [x] Get BApp details via `getbappdetails`
- [x] Create scan config via `createscanconfig`
- [x] Update scan config via `updatescanconfig`
- [x] Delete scan config via `deletescanconfig`
- [x] Create site login credentials via`createsitelogincredentials`
- [x] Update site login credentials via `createsitelogincredentials`
- [x] Delete site login credentials via `deletesitelogincredentials`
- [x] Create site recorded login credentials via`createsiterecordedlogin`
- [x] Delete site recorded login credentials via `deletesiterecordedlogin`
- [x] Create site email receipient via`createsiteemailreceipient`
- [x] Update site email receipient via `updatesiteemailreceipient`
- [x] Delete site email receipient via `deletesiteemailreceipient`
- [x] Authorize agent via `authorizeagent`
- [x] Deauthorize agent via `deauthorizeagent`
- [x] Move agent pool via `moveagentpool`
- [x] Assign site to agent pool via `assignsitetogentpool`
- [x] Update site scan config via `updatesitescanconfig`
- [x] Update site scope via `updatesitescope`
- [x] Update false positive status for an issue via `updatefalsepositive`
- [x] Higher-level concept/command - extract scan issue to JSON via `getissuedetails`

### To Do
- [ ] Write test case suite

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

```commandline
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
```commandline
 > py bseept.py createsite --sitename MyTestSite --scanconfigurationid ba4f8ce0-af9a-4450-ad35-78f083375088 --siteurls https://ginandjuice.shop
 {"data": {"create_site": {"site": {"id": "46", "parent_id": "0", "scope": {"included_urls": ["https://ginandjuice.shop"], "protocol_options": "USE_SPECIFIED_PROTOCOLS"}, "application_logins": {"login_credentials": [], "recorded_logins": []}, "scan_configurations": [{"id": "ba4f8ce0-af9a-4450-ad35-78f083375088"}]}}}}
 ```
 
### Creating a scan from a site and parse the response via jq to prettyfi
 ```commandline
> py bseept.py addscanschedule --siteid 44 --initialruntime 2024-08-19T11:07:25.664Z --schedule "FREQ=DAILY;INTERVAL=2" --scanconfigurationids ba4f8ce0-af9a-4450-ad35-78f083375088 8f7c2d95-0a72-40ce-a186-777348720870 | jq
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
 ```commandline
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
 
### Get the extensions and parse via jq to extract just the names
 ```commandline
 > py bseept.py --getextensions | c:\data\utils\jq ".[].extensions[] | .name" | more
"Backslash Powered Scanner"
"test-custom-extension.jar"
 ```
 
### Get the scheduled scans and parse via jq to prettyfi
 ```commandline
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
```commandline
> py bseept.py deletescanschedule --scanid 25
{"data": {"delete_schedule_item": {"id": "25"}}}
```

### Update a sites scope and parse the response through jq
 ```commandline
 > py bseept.py --url updatesitescope --siteid 55 --includedurls https://ginandjuice.shop https://www.binaryfirefly.com --excludedurls "https://portswigger.net" | jq 
{
  "data": {
    "update_site_scope": {
      "scope": {
        "included_urls": [
          "https://ginandjuice.shop",
          "https://www.binaryfirefly.com"
        ],
        "excluded_urls": [
          "https://portswigger.net"
        ],
        "protocol_options": "USE_SPECIFIED_PROTOCOLS"
      }
    }
  }
}
 ```

### Update a sites scan configuration IDs to use and parse the response through jq
 ```commandline
 > py bseept.py updatesitescanconfig --siteid 44 --scanconfigids 8f7c2d95-0a72-40ce-a186-777348720870 a6d11dcd-d3e7-424a-b8c4-90bf28b5785d | jq
{
  "data": {
    "update_site_scan_configurations": {
      "site": {
        "id": "44",
        "name": "thisis33ate4333st33324",
        "scan_configurations": [
          {
            "id": "8f7c2d95-0a72-40ce-a186-777348720870"
          },
          {
            "id": "a6d11dcd-d3e7-424a-b8c4-90bf28b5785d"
          }
        ]
      }
    }
  }
}

 ```

### Get scan details and then get scan results in various formats and outputs

First get the scan details
```commandline
bseept % python3 bseept.py --getscans  | jq 
{
  "data": {
    "scans": [
      {
        "id": "123",
        "status": "succeeded",
        "site_id": "1",
        "schedule_item": {
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
          "scheduled_run_time": "2023-03-15T13:51:14.000Z"
        },
        "scheduled_start_time": "2023-03-13T13:51:14.000Z",
        "start_time": "2023-03-13T13:51:54.525Z",
        "end_time": "2023-03-13T14:37:50.525Z",
        "duration_in_seconds": 2756,
        "scan_failure_code": null,
        "scan_metrics": {
          "crawl_request_count": 774,
          "unique_location_count": 54,
          "audit_request_count": 57437,
          "crawl_and_audit_progress_percentage": 100,
          "scan_phase": null,
          "audit_start_time": null,
          "current_url": "https://ginandjuice.shop:443/robots.txt"
        },
        "scan_failure_message": null,
        "scan_delta": {
          "new_issue_count": 0,
          "repeated_issue_count": 40,
          "regressed_issue_count": 0,
          "resolved_issue_count": 0
        },
        "issue_counts": {
          "total": 40,
          "high": {
            "total": 11,
            "firm": 4,
            "tentative": 0,
            "certain": 7
          },
          "medium": {
            "total": 0,
            "firm": 0,
            "tentative": 0,
            "certain": 0
          },
          "low": {
            "total": 10,
            "firm": 5,
            "tentative": 3,
            "certain": 2
          },
          "info": {
            "total": 19,
            "firm": 1,
            "tentative": 1,
            "certain": 17
          }
        },
        "scanner_version": "2023.2.3",
        "scanner_build_number": 19390
      },
...
```

Then extract the issues for the successful scan

```commandline
bseept % python3 bseept.py --getscanissues 123 | jq
{
  "data": {
    "scan": {
      "issues": [
        {
          "issue_type": {
            "name": "External service interaction (HTTP)",
            "description_html": "<p>External service interaction arises when it is possible to induce an application to interact with an arbitrary external service, such as a web or mail server. The ability to trigger arbitrary external service interactions does not constitute a vulnerability in its own right, and in some cases might even be the intended behavior of the application.\nHowever, in many cases, it can indicate a vulnerability with serious consequences.</p>\n<p>The ability to send requests to other systems can allow the vulnerable server to be used as an attack proxy.\n  By submitting suitable payloads, an attacker can cause the application server to attack other systems that it can interact with. \n  This may include public third-party systems, internal systems within the same organization, or services available on the local loopback adapter of the application server itself. \n  Depending on the network architecture, this may expose highly vulnerable internal services that are not otherwise accessible to external attackers. </p>",
            "remediation_html": "<p>You should review the purpose and intended use of the relevant application functionality, \n  and determine whether the ability to trigger arbitrary external service interactions is intended behavior. \n  If so, you should be aware of the types of attacks that can be performed via this behavior and take appropriate measures. \n  These measures might include blocking network access from the application server to other internal systems, and hardening the application server itself to remove any services available on the local loopback adapter.</p>\n<p>If the ability to trigger arbitrary external service interactions is not intended behavior, then you should implement a whitelist of permitted services and hosts, and block any interactions that do not appear on this whitelist.</p>\n\n<p>Out-of-Band Application Security Testing (OAST) is highly effective at uncovering high-risk features, to the point where finding the root cause of an interaction can be quite challenging. To find the source of an external service interaction, try to identify whether it is triggered by specific application functionality, or occurs indiscriminately on all requests. If it occurs on all endpoints, a front-end CDN or application firewall may be responsible, or a back-end analytics system parsing server logs. In some cases, interactions may originate from third-party systems; for example, a HTTP request may trigger a poisoned email which passes through a link-scanner on its way to the recipient.</p>",
            "vulnerability_classifications_html": "<ul>\n<li><a href=\"https://cwe.mitre.org/data/definitions/918.html\">CWE-918: Server-Side Request Forgery (SSRF)</a></li>\n<li><a href=\"https://cwe.mitre.org/data/definitions/406.html\">CWE-406: Insufficient Control of Network Message Volume (Network Amplification)</a></li>\n</ul>",
            "references_html": "<ul>\n  <li><a href=\"https://portswigger.net/blog/introducing-burp-collaborator\">Burp Collaborator</a></li>\n  <li><a href=\"https://portswigger.net/burp/application-security-testing/oast\">Out-of-band application security testing (OAST)</a></li>\n  <li><a href=\"https://portswigger.net/research/cracking-the-lens-targeting-https-hidden-attack-surface\">PortSwigger Research: Cracking the Lens</a></li>\n</ul>"
          },
          "confidence": "certain",
          "display_confidence": null,
          "serial_number": "5601616512020228096",
          "severity": "high",
          "description_html": "It is possible to induce the application to perform server-side HTTP and HTTPS requests to arbitrary domains.<br><br>The payload <b>http://s0t5stlr0i5p270b2o0hxzl1ksqlee24qzdq1f.oastify.com/</b> was submitted in the <b>Referer</b> HTTP header.<br><br>The application performed an HTTP request to the specified domain.",
          "remediation_html": null,
          "path": "/catalog",
          "origin": "https://ginandjuice.shop",
          "novelty": "repeated",
          "tickets": null,
          "generated_by_extension": null
        },

```

Then use jq to parse the JSON and print the issue titles

```commandline
bseept % python3 bseept.py --getscanissues 123 | jq ".[].scan.issues[].issue_type.name"        
"External service interaction (HTTP)"
"External service interaction (HTTP)"
"External service interaction (HTTP)"
"HTTP response header injection"
"External service interaction (HTTP)"
"Cross-site scripting (reflected)"
"Cross-site scripting (reflected)"
"SQL injection"
"XML external entity injection"
"Cross-site scripting (reflected)"
"Client-side template injection"
"Strict transport security not enforced"
"Password field with autocomplete enabled"
"Iterable input"
"Iterable input"
"Iterable input"
"Iterable input"
"Iterable input"
"Open redirection (DOM-based)"
"Open redirection (DOM-based)"
"Vulnerable JavaScript dependency"
"Cookie without HttpOnly flag set"
"Cookie without HttpOnly flag set"
"Input returned in response (reflected)"
"Cacheable HTTPS response"
"TLS certificate"
"TLS cookie without secure flag set"
"External service interaction (DNS)"
"External service interaction (DNS)"
"Input returned in response (reflected)"
"External service interaction (DNS)"
"Input returned in response (reflected)"
"Cross-site scripting (reflected)"
"Input returned in response (reflected)"
"External service interaction (DNS)"
"Input returned in response (reflected)"
"Input returned in response (reflected)"
"Input returned in response (reflected)"
"Client-side prototype pollution"
"Request URL override"
```

Then extract into CSV lines

```commandline
bseept % python3 bseept.py --getscanissues 123 | jq '.[].scan.issues[] | "\(.issue_type.name),\(.origin),\(.path)"'
"External service interaction (HTTP),https://ginandjuice.shop,/catalog"
"External service interaction (HTTP),https://ginandjuice.shop,/catalog/filter"
"External service interaction (HTTP),https://ginandjuice.shop,/catalog/product"
"HTTP response header injection,https://ginandjuice.shop,/catalog/product-search-results/5"
"External service interaction (HTTP),https://ginandjuice.shop,/catalog/product/stock"
"Cross-site scripting (reflected),https://ginandjuice.shop,/catalog/search/3"
"Cross-site scripting (reflected),https://ginandjuice.shop,/catalog/search/4"
"SQL injection,https://ginandjuice.shop,/catalog/filter"
"XML external entity injection,https://ginandjuice.shop,/catalog/product/stock"
"Cross-site scripting (reflected),https://ginandjuice.shop,/catalog/search/2"
"Client-side template injection,https://ginandjuice.shop,/catalog/search/4"
"Strict transport security not enforced,https://ginandjuice.shop,/"
"Password field with autocomplete enabled,https://ginandjuice.shop,/login"
"Iterable input,https://ginandjuice.shop,/post"
"Iterable input,https://ginandjuice.shop,/post"
"Iterable input,https://ginandjuice.shop,/post"
"Iterable input,https://ginandjuice.shop,/post"
"Iterable input,https://ginandjuice.shop,/post"
"Open redirection (DOM-based),https://ginandjuice.shop,/catalog/product"
"Open redirection (DOM-based),https://ginandjuice.shop,/catalog/product"
"Vulnerable JavaScript dependency,https://ginandjuice.shop,/resources/js/angular_1-7-7.js"
"Cookie without HttpOnly flag set,https://ginandjuice.shop,/"
"Cookie without HttpOnly flag set,https://ginandjuice.shop,/"
"Input returned in response (reflected),https://ginandjuice.shop,/"
"Cacheable HTTPS response,https://ginandjuice.shop,/"
"TLS certificate,https://ginandjuice.shop,/"
"TLS cookie without secure flag set,https://ginandjuice.shop,/"
"External service interaction (DNS),https://ginandjuice.shop,/catalog"
"External service interaction (DNS),https://ginandjuice.shop,/catalog/filter"
"Input returned in response (reflected),https://ginandjuice.shop,/catalog/filter"
"External service interaction (DNS),https://ginandjuice.shop,/catalog/product"
"Input returned in response (reflected),https://ginandjuice.shop,/catalog/product-search-results/1"
"Cross-site scripting (reflected),https://ginandjuice.shop,/catalog/product-search-results/1"
"Input returned in response (reflected),https://ginandjuice.shop,/catalog/product-search-results/5"
"External service interaction (DNS),https://ginandjuice.shop,/catalog/product/stock"
"Input returned in response (reflected),https://ginandjuice.shop,/catalog/search/2"
"Input returned in response (reflected),https://ginandjuice.shop,/catalog/search/3"
"Input returned in response (reflected),https://ginandjuice.shop,/catalog/search/4"
"Client-side prototype pollution,https://ginandjuice.shop,/"
"Request URL override,https://ginandjuice.shop,/"
```

then do the same, sort and count

```commandline
bseept % python3 bseept.py --getscanissues 123 | jq ".[].scan.issues[].issue_type.name" | sort | uniq -c
   1 "Cacheable HTTPS response"
   1 "Client-side prototype pollution"
   1 "Client-side template injection"
   2 "Cookie without HttpOnly flag set"
   4 "Cross-site scripting (reflected)"
   4 "External service interaction (DNS)"
   4 "External service interaction (HTTP)"
   1 "HTTP response header injection"
   7 "Input returned in response (reflected)"
   5 "Iterable input"
   2 "Open redirection (DOM-based)"
   1 "Password field with autocomplete enabled"
   1 "Request URL override"
   1 "SQL injection"
   1 "Strict transport security not enforced"
   1 "TLS certificate"
   1 "TLS cookie without secure flag set"
   1 "Vulnerable JavaScript dependency"
   1 "XML external entity injection"
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


