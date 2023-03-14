#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

# Burp Suite Enterprise Edition GraphQL API documentation
# https://portswigger.net/burp/documentation/enterprise/api-documentation/graphql-api
# https://portswigger.net/burp/extensibility/enterprise/graphql-api/

# Library documentation
# https://github.com/prisma-labs/python-graphql-client

# Tips
# https://stackoverflow.com/questions/60115681/python-multiline-graphql-mutation-with-variables-keyerror
# https://stackoverflow.com/questions/53510102/pass-variable-to-graphql-using-python-module-graphqlclient


# Using
#   py bseept.py createsite --sitename kdkd2342j22 --siteurls ginandjuice.shop zemes.com
#   py bseept.py createsite --sitename thisis33ate4333st333243 --scanconfigurationid ba4f8ce0-af9a-4450-ad35-78f083375088 --siteurls https://ginandjuice.shop
# Using jq
#   jq ".[].scans[] | .status, .id" | more
# 

import os
import sys
import argparse # command line processing
import base64 # for encoding JAR files

# BSEE client library elements
import bseeptfolders
import bseeptagentpools
import bseeptagents
import bseeptbapps
import bseeptcredentials
import bseeptemailrecipients
import bseeptevents
import bseeptextensions
import bseeptfolders
import bseeptgraphql
import bseeptissues
import bseeptscanconfigs
import bseeptscans
import bseeptscanschedules
import bseeptsites

import urllib3

version = "0.1"
versioncheckurl = ""
apiurl = ""

# Print the help screen
def printhelp():
    print("[Help]", file=sys.stderr)

# Main entry point
def main():
    parser = argparse.ArgumentParser(
                    prog = 'bseept',
                    description = 'Burp Suite Enterprise Edition Power Tools',
                    epilog = 'with 🧡 from PortSwigger')

    parser.add_argument('-u', '--url', help='Burp Suite Enterprise Edition URL')
    parser.add_argument('--apikey', help='Burp Suite Enterprise Edition API key')
    

    # ---------------------
    # queries
    # https://portswigger.net/burp/extensibility/enterprise/graphql-api/queries.html
    # ---------------------

    # get sites and folders
    parser.add_argument('--getsites', help='Configured all configured sites', action='store_true')
    parser.add_argument('--getfolders', help='Configured folders in BSEE', action='store_true')
    parser.add_argument('--getsitetree', help='Configured site tree in BSEE', action='store_true')

    # get scans
    parser.add_argument('--getscans', help='Configured all configured scans', action='store_true')

    # get scan configurations
    parser.add_argument('--getscanconfigs', help='Get all scan configuration definitions', action='store_true')

    # get specific scan information
    parser.add_argument('--getscanissues', help='Get scan issues specified by the supplied scan ID', action='store') # takes a scan ID
    parser.add_argument('--getscanreport', help='Get scan HTML report specified by the supplied scan ID', action='store') # takes a scan ID
    parser.add_argument('--getscanreportxml', help='Get scan XML report specified by the supplied scan ID', action='store') # takes a scan ID

    # get scan schedules
    parser.add_argument('--getschedule', help='Scan schedules', action='store_true')

    # get agents and pools
    parser.add_argument('--getagents', help='Configured scan agents', action='store_true')
    parser.add_argument('--getagentpools', help='Configured scan agent pools', action='store_true')
    parser.add_argument('--getunauthorizedagents', help='Get the curretly unauthorized agents', action='store_true')

    # get extensions
    parser.add_argument('--getextensions', help='Extensions installed', action='store_true')

    # ---------------------
    # mutations (set etc.) - these are implemented as subcommands 
    # https://portswigger.net/burp/extensibility/enterprise/graphql-api/mutations.html
    # ---------------------

    subparsers = parser.add_subparsers(help='modify commands' , dest='command')

    #
    # sites
    #
    parser_createsite = subparsers.add_parser('createsite', help='Create a site')
    parser_createsite.add_argument('--sitename', help='site name', required=True)
    parser_createsite.add_argument('--siteurls', nargs='+', help='site URLs', required=True)
    parser_createsite.add_argument('--parentfolderid', help='parent folder ID in site tree otherwise defaults to 0', default="0")
    parser_createsite.add_argument('--protocoloptions', help='which protocols are used when scanning the sites URLs', default='USE_SPECIFIED_PROTOCOLS', choices=['USE_SPECIFIED_PROTOCOLS', 'USE_HTTP_AND_HTTPS'])
    parser_createsite.add_argument('--scanconfigurationids', help='scan configuration IDs to use', required=True)

    parser_deletesite = subparsers.add_parser('deletesite', help='Delete a site')
    parser_deletesite.add_argument('--siteid', help='site ID', required=True)

    parser_renamesite = subparsers.add_parser('renamesite', help='Rename a site')
    parser_renamesite.add_argument('--siteid', help='site ID', required=True)
    parser_renamesite.add_argument('--newname', help='new site name', required=True)

    parser_movesite = subparsers.add_parser('movesite', help='Move a site')
    parser_movesite.add_argument('--siteid', help='site ID', required=True)
    parser_movesite.add_argument('--newparentfolderid', help='new parent folder ID', required=True)

    parser_updatesitescanconfig = subparsers.add_parser('updatesitescanconfig', help='Update a site scan configuration')

    parser_updatesitescope = subparsers.add_parser('updatesitescope', help='Update a site scope')

    parser_updatesiteextensions = subparsers.add_parser('updatesiteextensions', help='Update a site\'s extensions')
    parser_updatesiteextensions.add_argument('--siteid', help='site ID', required=True)
    parser_updatesiteextensions.add_argument('--extensionids', help='extension IDs to use', required=True)

    #
    # Site credentials
    #
    parser_createsitelogincredentials = subparsers.add_parser('createsitelogincredentials', help='Create a sites login credentials')
    parser_createsitelogincredentials.add_argument('--siteid', help='site ID from --getsites', required=True)
    parser_createsitelogincredentials.add_argument('--label', help='descriptive name', required=True)
    parser_createsitelogincredentials.add_argument('--username', help='username', required=True)
    parser_createsitelogincredentials.add_argument('--password', help='password', required=True)

    parser_updatesitelogincredentials = subparsers.add_parser('updatesitelogincredentials', help='Update a sites login credentials')
    parser_updatesitelogincredentials.add_argument('--credid', help='credential ID from --getsites', required=True)
    parser_updatesitelogincredentials.add_argument('--label', help='descriptive name', required=True)
    parser_updatesitelogincredentials.add_argument('--username', help='username', required=True)
    parser_updatesitelogincredentials.add_argument('--password', help='password', required=True)

    parser_deletesitelogincredentials = subparsers.add_parser('deletesitelogincredentials', help='Delete a sites login credentials')
    parser_deletesitelogincredentials.add_argument('--credid', help='credential ID from --getsites', required=True)

    parser_createsiterecordedlogincredentials = subparsers.add_parser('createsiterecordedlogin', help='Create a sites recorded login credentials')
    parser_createsiterecordedlogincredentials.add_argument('--siteid', help='site ID from --getsites', required=True)
    parser_createsiterecordedlogincredentials.add_argument('--label', help='descriptive name', required=True)
    parser_createsiterecordedlogincredentials.add_argument('--script', help='recorded login script', required=True)

    parser_deletesiterecordedlogincredentials = subparsers.add_parser('deletesiterecordedlogin', help='Delete a sites recorded login credentials')
    parser_deletesiterecordedlogincredentials.add_argument('--rlid', help='recorded login ID from --getsites', required=True)

    #
    # Site email recipients
    #
    parser_createsitelogincredentials = subparsers.add_parser('createsiteemailreceipient', help='Create a site email receipient for reporting')
    parser_createsitelogincredentials.add_argument('--siteid', help='site ID from --getsites', required=True)
    parser_createsitelogincredentials.add_argument('--email', help='e-mail address', required=True)

    parser_updatesitelogincredentials = subparsers.add_parser('updatesiteemailreceipient', help='Update a site email receipient for reporting')
    parser_updatesitelogincredentials.add_argument('--emailid', help='e-mail receipient ID from --getsites', required=True)
    parser_updatesitelogincredentials.add_argument('--email', help='e-mail address', required=True)

    parser_deletesitelogincredentials = subparsers.add_parser('deletesiteemailreceipient', help='Delete a site email receipient for reporting')
    parser_deletesitelogincredentials.add_argument('--emailid', help='e-mail receipient ID from --getsites', required=True)

    #
    # Scan schedules
    #
    parser_addscan = subparsers.add_parser('addscanschedule', help='Add a scan schedule')
    parser_addscan.add_argument('--siteid', help='site ID returned from createsite, --getsites or --getsitetree', required=True)
    parser_addscan.add_argument('--initialruntime', help='initial run time e.g. 2024-08-19T11:07:25.664Z', required=True)
    parser_addscan.add_argument('--schedule', help='fequency of scan run beyond initial run in RRULE format decribed in RFC5545, RFC5546, and RFC5547.', required=True)
    parser_addscan.add_argument('--scanconfigurationids', help='scan configuration IDs to use', required=True)

    parser_updatescanschedule = subparsers.add_parser('updatescanschedule', help='Update a scan schedule')
    parser_updatescanschedule.add_argument('--scanid', help='scan ID returned from addscanedule or --getschedule', required=True)
    parser_updatescanschedule.add_argument('--siteid', help='site ID returned from createsite, --getsites or --getsitetree', required=True)
    parser_updatescanschedule.add_argument('--initialruntime', help='initial run time e.g. 2024-08-19T11:07:25.664Z', required=True)
    parser_updatescanschedule.add_argument('--schedule', help='fequency of scan run beyond initial run in RRULE format decribed in RFC5545, RFC5546, and RFC5547.', required=True)
    parser_updatescanschedule.add_argument('--scanconfigurationids', help='scan configuration IDs to use', required=True)

    parser_deletescansschedule = subparsers.add_parser('deletescanschedule', help='Delete a scan')
    parser_deletescansschedule.add_argument('--scanid', help='scanid ID returned from addscanschedule or --getschedules', required=True)

    #
    # scan configurations
    #
    parser_createscanconfig = subparsers.add_parser('createscanconfig', help='Create a scan configuration')
    parser_createscanconfig.add_argument('--name', help='scan configuration name', required=True)
    parser_createscanconfig.add_argument('--jsonconfig', help='escaped JSON configuration fragment', required=True)

    parser_updatescanconfig = subparsers.add_parser('updatescanconfig', help='Update a scan configuration')
    parser_updatescanconfig.add_argument('--scanconfigid', help='scan configuration ID returned from --createscanconfig or --getscanconfigs', required=True)
    parser_updatescanconfig.add_argument('--name', help='scan configuration name', required=True)
    parser_updatescanconfig.add_argument('--jsonconfig', help='escaped JSON configuration fragment', required=True)

    parser_deletescanconfig = subparsers.add_parser('deletescanconfig', help='Delete a scan configuration')
    parser_deletescanconfig.add_argument('--scanconfigid', help='scan configuration ID returned from --createscanconfig or --getscanconfigs', required=True)

    #
    # BApps
    #
    parser_uploadbapp = subparsers.add_parser('uploadbapp', help='Upload a BApp')
    parser_uploadbapp.add_argument('--filename', help='extension filename', required=True)
    parser_uploadbapp.add_argument('--localjarname', help='path to local JAR', required=True)

    parser_getbappdetails = subparsers.add_parser('getbappdetails', help='Get BApp details without adding it to the list of usable extensions - this uploads and parses the BApp')
    parser_getbappdetails.add_argument('--filename', help='extension filename', required=True)
    parser_getbappdetails.add_argument('--localjarname', help='path to local JAR', required=True)

    #
    # Extensions
    #
    parser_uploadextension = subparsers.add_parser('uploadextension', help='Upload a custom extension')
    parser_uploadextension.add_argument('--filename', help='extension filename', required=True)
    parser_uploadextension.add_argument('--name', help='extension name', required=True)
    parser_uploadextension.add_argument('--description', help='extension description', required=True)
    parser_uploadextension.add_argument('--localjarname', help='path to local JAR', required=True)

    parser_updateextensionname = subparsers.add_parser('updateextensionname', help='Update a custom extension name')
    parser_updateextensionname.add_argument('--extid', help='extension ID returned from --getextensions', required=True)
    parser_updateextensionname.add_argument('--jarname', help='new extension JAR name', required=True)

    parser_updateextensiondescription = subparsers.add_parser('updateextensiondescription', help='Update a custom extension description')
    parser_updateextensiondescription.add_argument('--extid', help='extension ID returned from --getextensions', required=True)
    parser_updateextensiondescription.add_argument('--description', help='new extension description', required=True)

    parser_updateextensionjar = subparsers.add_parser('updateextensionjar', help='Update a custom extension JAR')
    parser_updateextensionjar.add_argument('--extid', help='extension ID returned from --getextensions', required=True)
    parser_updateextensionjar.add_argument('--filename', help='extension filename', required=True)
    parser_updateextensionjar.add_argument('--localjarname', help='path to local JAR', required=True)

    parser_deleteextension = subparsers.add_parser('deleteextension', help='Delete a custom extension or BApp')
    parser_deleteextension.add_argument('--extid', help='extension ID returned from --getextensions', required=True)

    #
    # Agents
    #
    parser_authorizeagent = subparsers.add_parser('authorizeagent', help='Authorize a new agent to be able to run scans')
    parser_authorizeagent.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)
    parser_authorizeagent.add_argument('--agentpoolid', help='agent pool ID returned from createagentpool or --getagentpools', required=True)

    parser_deauthorizeagent = subparsers.add_parser('deauthorizeagent', help='Deauthorize an existing agent from running scans')
    parser_deauthorizeagent.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)

    parser_renameagent = subparsers.add_parser('renameagent', help='Rename an existing agent')
    parser_renameagent.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)
    parser_renameagent.add_argument('--name', help='new name of the agent', required=True)

    parser_enableagent = subparsers.add_parser('enableagent', help='Enable an existing agent')
    parser_enableagent.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)

    parser_disableagent = subparsers.add_parser('disableagent', help='Disable an existing agent')
    parser_disableagent.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)

    parser_updateagentmaxconcurrentscans = subparsers.add_parser('updateagentmaxconcurrentscans', help='Update the maximum number of concurrent scans this agent host can run')
    parser_updateagentmaxconcurrentscans.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)
    parser_updateagentmaxconcurrentscans.add_argument('--concurrentscans', help='number of concurrent scans for this agent', required=True)

    #
    # Agent pools
    #
    parser_createagentpool = subparsers.add_parser('createagentpool', help='Create an agent pool')
    parser_createagentpool.add_argument('--name', help='name of the agent pool', required=True)
    parser_createagentpool.add_argument('--description', help='description of the agent pool', required=True)

    parser_updateagentpool = subparsers.add_parser('updateagentpool', help='Update an agent pool')
    parser_updateagentpool.add_argument('--poolid', help='ID of the agent pool', required=True)
    parser_updateagentpool.add_argument('--name', help='name of the agent pool', required=True)
    parser_updateagentpool.add_argument('--description', help='description of the agent pool', required=True)

    parser_moveagentpool = subparsers.add_parser('moveagentpool', help='Move an agent pool')
    parser_moveagentpool.add_argument('--agentid', help='agent ID returned from createagent or --getagents', required=True)
    parser_moveagentpool.add_argument('--agentpoolid', help='agent pool ID returned from createagentpool or --getagentpools', required=True)

    parser_deleteagentpool = subparsers.add_parser('deleteagentpool', help='Delete an agent pool')
    parser_deleteagentpool.add_argument('--poolid', help='ID of the agent pool', required=True)

    parser_assignsitetogentpool = subparsers.add_parser('assignsitetogentpool', help='Assign sites to an agent pool')

    #
    # Folders
    #
    parser_createfolder = subparsers.add_parser('createfolder', help='Create a folder')
    parser_createfolder.add_argument('--parentfolderid', help='folder ID returned from createfolder or --getfolders', required=True)
    parser_createfolder.add_argument('--name', help='name of the folder', required=True)

    parser_deletefolder = subparsers.add_parser('deletefolder', help='Delete a folder')
    parser_deletefolder.add_argument('--id', help='folder ID returned from createfolder or --getfolders', required=True)

    parser_renamefolder = subparsers.add_parser('renamefolder', help='Rename a folder')
    parser_renamefolder.add_argument('--folderid', help='folder ID returned from createfolder or --getfolders', required=True)
    parser_renamefolder.add_argument('--name', help='new name of the folder', required=True)

    parser_movefolder = subparsers.add_parser('movefolder', help='Move a folder')
    parser_movefolder.add_argument('--folderid', help='folder ID returned from createfolder or --getfolders', required=True)
    parser_movefolder.add_argument('--parentfolderid', help='new parent folder ID returned from createfolder or --getfolders', required=True)

    #
    # Issues
    #
    parser_updatefalsepositive = subparsers.add_parser('updatefalsepositive', help='Update the false positive for an issue')

###################################
# now parse
###################################

    args = parser.parse_args()

    # Discuss 
    urllib3.disable_warnings()

    # Host URL
    BSEEURL = os.getenv('BSEEURL')
    if(BSEEURL is None and args.url is None):
        sys.stderr.write("Need to specify the BSEE URL either in the environment variable BSEEURL or on the command line via --url")
        exit()
    else:
        if(BSEEURL is not None and args.url is not None):
            sys.stderr.write("Environment URL variable set and command line supplied - using environment variable")

        if(BSEEURL is not None): # environment trumps command line
            apiurl = BSEEURL
        else:
            apiurl = args.url

        apiurl = apiurl.rstrip('/')
        if(apiurl.startswith("https://") is not True):
            sys.stderr.write("Supplied URL does not begin with https:// as required")
            exit()



    # API key
    BSEEAPIKEY = os.getenv('BSEEAPIKEY')
    if(BSEEAPIKEY is None and args.apikey is None):
        sys.stderr.write("Need to specify the BSEE API key either in the environment variable BSEEAPIKEY or on the command line via --apikey")
        exit()
    else:
        if(BSEEAPIKEY is not None and args.apikey is not None):
            sys.stderr.write("Environment API key variable set and command line supplied - using environment variable")

        if(BSEEAPIKEY is not None): # environment trumps command line
            apikey = BSEEAPIKEY
        else:
            apikey = args.apikey

###################################
# logic to deal with command line options and invoke the relevant functions
###################################

    #
    # GraphQL queries i.e. read operations
    #

    # We don't do if/else here as we may want various commands
    if(args.getsites is True):
        bseeptsites.getsites(apiurl,apikey)

    if(args.getfolders is True):
        bseeptfolders.getsitetreefolders(apiurl,apikey)

    if(args.getsitetree is True):
        bseeptsites.getsitetree(apiurl,apikey)

    if(args.getscans is True):
        bseeptscans.getscans(apiurl,apikey)

    if(args.getscanissues is not None):
        bseeptscans.getscanissues(apiurl, apikey, args.getscanissues)
    
    if(args.getscanreport is not None):
        bseeptscans.getscanreport(apiurl, apikey, args.getscanreport, True)

    if(args.getscanreportxml is not None):
        bseeptscans.getscanreportxml(apiurl, apikey, args.getscanreportxml, True)

    if(args.getscanconfigs is True):
        bseeptscanconfigs.getscanconfigs(apiurl, apikey)

    if(args.getagents is True):
        bseeptagents.getagents(apiurl,apikey)

    if(args.getagentpools is True):
        bseeptagentpools.getagentpools(apiurl,apikey)

    if(args.getschedule is True):
        bseeptscanschedules.getscheduleitems(apiurl,apikey)

    if(args.getextensions is True):
        bseeptextensions.getextensions(apiurl,apikey) 

    if(args.getunauthorizedagents is True):
        bseeptagents.getunauthorisedagents(apiurl,apikey)

    #
    # GraphQL Mutations i.e. write operations
    #

    #
    # Sites
    if(args.command =="createsite"):                           
        bseeptsites.createsite(apiurl, apikey, args.sitename, args.siteurls, args.parentfolderid, args.scanconfigurationids, args.protocoloptions)

    if(args.command =="deletesite"):                           
        bseeptsites.deletesite(apiurl, apikey, args.siteid)

    if(args.command =="renamesite"):                           
        bseeptsites.deletesite(apiurl, apikey, args.siteid, args.newname)
    #
    # Scans / Schedules
    if(args.command =="addscanschedule"):
        bseeptscanschedules.addscanschedule(apiurl, apikey,args.siteid, args.initialruntime, args.schedule, args.scanconfigurationids)

    if(args.command =="updatescanschedule"):
        bseeptscanschedules.updatescanschedule(apiurl, apikey, args.scanid, args.siteid, args.initialruntime, args.schedule, args.scanconfigurationids)

    if(args.command == "deletescanschedule"):
        bseeptscanschedules.deletescanschedule(apiurl, apikey, args.scanid)

    if(args.command == "updatesiteextensions"):
        bseeptsites.updatesiteextensions(apiurl, apikey, args.siteid, args.extensionids)

    #
    # Folders
    if(args.command == "createfolder"):
        bseeptfolders.createfolder(apiurl, apikey, args.name, args.parentfolderid)

    if(args.command == "deletefolder"):
        bseeptfolders.deletefolder(apiurl, apikey, args.id)

    if(args.command == "renamefolder"):
        bseeptfolders.renamefolder(apiurl, apikey, args.name, args.folderid)

    if(args.command == "movefolder"):
        bseeptfolders.movefolder(apiurl, apikey, args.folderid, args.parentfolderid)

    #
    # Agents
    if(args.command == "renameagent"):
        bseeptagents.renameagent(apiurl, apikey, args.name, args.agentid)

    if(args.command == "enableagent"):
        bseeptagents.enabledisableagent(apiurl, apikey, True, args.agentid)

    if(args.command == "disableagent"):
        bseeptagents.enabledisableagent(apiurl, apikey, False, args.agentid)

    if(args.command == "updateagentmaxconcurrentscans"):
        bseeptagents.concurrentscansforagent(apiurl,apikey,args.concurrentscans, args.agentid)

    if(args.command == "createagentpool"):
        bseeptagents.createpool(apiurl,apikey, args.name, args.description)

    if(args.command == "updateagentpool"):
        bseeptagents.updatepool(apiurl,apikey,args.poolid, args.name, args.description)

    if(args.command == "deleteagentpool"):
        bseeptagents.deletepool(apiurl,apikey, args.poolid)

    if(args.command == "authorizeagent"):
        bseeptagents.authorizeagent(apiurl, apikey, args.agentid, args.agentpoolid)

    if(args.command == "deauthorizeagent"):
        bseeptagents.deauthorizeagent(apiurl, apikey, args.agentid)

    if(args.command == "moveagentpool"):
        bseeptagents.moveagentpool(apiurl, apikey, args.agentid, args.agentpoolid)

    #
    # Extensions
    if(args.command == "updateextensionname"):
        bseeptextensions.updateextensionname(apiurl,apikey, args.extid, args.jarname)

    if(args.command == "updateextensiondescription"):
        bseeptextensions.updateextensiondescription(apiurl,apikey, args.extid, args.description)

    if(args.command == "deleteextension"):
        bseeptextensions.deleteextension(apiurl, apikey,args.extid)

    if(args.command == "uploadextension"):

        try:
            with open(args.localjarname, "rb") as jar_file:
                b64jar = base64.b64encode(jar_file.read())

        except Exception as inst:
            print("[!] Error whilst processing JAR file")
            return

        bseeptextensions.uploadcustomeextension(apiurl, apikey, args.filename, b64jar.decode('utf-8'), args.name, args.description)

    if(args.command == "updateextensionjar"):
        try:
            with open(args.localjarname, "rb") as jar_file:
                b64jar = base64.b64encode(jar_file.read())

        except Exception as inst:
            print("[!] Error whilst processing JAR file")
            return

        bseeptextensions.updatecustomeextensionjar(apiurl, apikey, args.extid, args.filename, b64jar.decode('utf-8'))

    if(args.command == "uploadbapp"):

        try:
            with open(args.localjarname, "rb") as jar_file:
                b64jar = base64.b64encode(jar_file.read())

        except Exception as inst:
            print("[!] Error whilst processing JAR file")
            return

        bseeptextensions.uploadbapp(apiurl, apikey, args.filename, b64jar.decode('utf-8'))

    if(args.command == "getbappdetails"):

        try:
            with open(args.localjarname, "rb") as jar_file:
                b64jar = base64.b64encode(jar_file.read())

        except Exception as inst:
            print("[!] Error whilst processing JAR file")
            return

        bseeptextensions.getbappdetails(apiurl, apikey, args.filename, b64jar.decode('utf-8'))


    #
    # Scan configurations

    if(args.command == "createscanconfig"):
        bseeptscanconfigs.createscanconfig(apiurl,apikey,args.name, args.jsonconfig)

    if(args.command == "updatescanconfig"):
        bseeptscanconfigs.updatescanconfig(apiurl,apikey,args.scanconfigid,args.name, args.jsonconfig)

    if(args.command == "deletescanconfig"):
        bseeptscanconfigs.deletescanconfig(apiurl,apikey,args.scanconfigid, False)

    #
    # Site credentials

    if(args.command == "createsitelogincredentials"):
        bseeptcredentials.createsitelogincred(apiurl, apikey, args.siteid, args.label, args.username, args.password)

    if (args.command == "updatesitelogincredentials"):
        bseeptcredentials.updatesitelogincred(apiurl, apikey, args.credid, args.label, args.username, args.password)

    if (args.command == "deletesitelogincredentials"):
        bseeptcredentials.deletesitelogincred(apiurl, apikey, args.credid)

    if (args.command == "createsiterecordedlogin"):
       bseeptcredentials.createsiterecordedlogin(apiurl, apikey, args.siteid, args.label, args.script)

    if (args.command == "deletesiterecordedlogin"):
        bseeptcredentials.deletesiterecordedlogin(apiurl, apikey, args.rlid)

    #
    # Site email recipients
    if (args.command == "createsiteemailreceipient"):
        bseeptemailrecipients.createsiteemailreceipient(apiurl, apikey, args.siteid, args.email)

    if(args.command == "updatesiteemailreceipient"):
        bseeptemailrecipients.updatesiteemailreceipient(apiurl,apikey, args.emailid, args.email)

    if(args.command == "deletesiteemailreceipient"):
        bseeptemailrecipients.deletesiteemailreceipient(apiurl, apikey, args.emailid)


# Entry point
if __name__ == '__main__':
    main()







