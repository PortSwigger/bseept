#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# Get the sites configured in the system
#
def getsites(APIURL,APIKEY,doprint=True, output=False):
    
    query = '''
        query GetSiteTree {
            site_tree {
                sites {
                    id
                    name
                    parent_id
                    scope {
                        included_urls
                        excluded_urls
                        protocol_options
                    }
                    scan_configurations{
                        id
                    }
                    application_logins {
                        login_credentials {
                            id
                            label
                            username
                            password
                        }
                        recorded_logins {
                            id
                            label
                        }
                    }
                    extensions {
                        id
                    }
                    ephemeral
                    email_recipients{
                        id
                        email
                    }
                }
            }
        }
        '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
# Get the site tree which is comprised of folders and sites
#
def getsitetree(APIURL,APIKEY, urls=None, parent=1,doprint=True, output=False):
    query = '''
        query GetSiteTree {
            site_tree {
                folders {
                    id
                    name
                    parent_id
                }
                sites {
                    id
                    name
                    parent_id
                    scope {
                        included_urls
                        excluded_urls
                        protocol_options
                    }
                    scan_configurations{
                        id
                    }
                    application_logins {
                        login_credentials {
                            label
                            username
                        }
                        recorded_logins {
                            label
                        }
                    }
                    extensions {
                        id
                    }
                    ephemeral
                    email_recipients{
                        id
                        email
                    }
                }
            }
        }
    '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Create a site
#
def createsite(APIURL,APIKEY, name, urls, parent_id, scan_configuration_ids, protocol_options, email_recipients = "", agent_pool_id = "-1", doprint=True, output=False):
 
    #
    #                 $scan_configuration_id: [ID!]           
    # scan_configuration_ids: [$scan_configuration_id]
   #               scan_configuration_ids {
   #                   id
   #              }
    #

    # $email_recipients: [EmailRecipientInput!]
    #                 email_recipients: $email_recipients

    query = '''
    mutation CreateSite($name: String!, $parent_id: ID!, $urls: [String!]!, $protocol_options: ScopeProtocolOptions!, $scan_configuration_ids: [ID!], $agentpoolid: ID!, ) {
 

        create_site(
            input: {
                name: $name
                parent_id: $parent_id
                scope: {
                    included_urls: $urls
                    protocol_options: $protocol_options
                }
                application_logins: {
                    login_credentials: [] 
                    recorded_logins: []
                } 
                scan_configuration_ids: $scan_configuration_ids

                agent_pool_id: $agentpoolid
            } 
            ) 
        
        {
            site {
                id
                parent_id
                scope {
                    included_urls
                    protocol_options
                }
                application_logins {
                    login_credentials {
                        id
                        label
                        username
                    }
                    recorded_logins {
                        id
                        label
                    }
                }
                scan_configurations{
                    id
                }
                extensions {
                        id
                }
                ephemeral
                email_recipients {
                    id
                    email
                }
                agent_pool{
                    id
                    name
                    description
                }
           }
        }
    }'''

    variables = { 
            "name": name, 
            "parent_id": parent_id, 
            "urls": urls, 
            "protocol_options": protocol_options.lstrip('\'').rstrip('\''), 
            "scan_configuration_ids": scan_configuration_ids,
            "email_recipients": email_recipients,
            "agentpoolid": agent_pool_id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Delete a site
#
def deletesite(APIURL,APIKEY, site_id,doprint=True, output=False):
 
    query = '''
    mutation DeleteSite($siteid: ID!) {
 
        delete_site(
            input: {
                id: $siteid
            } 
            ) 
        
        {
            id
        }
    }'''

    variables = { 
            "siteid": site_id, 
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
# Rename a site
#
def renamesite(APIURL,APIKEY, site_id, newname,doprint=True, output=False):
 
    query = '''
    mutation RenameSite($siteid: ID!, $name: String!) {
 
        rename_site(
            input: {
                id: $siteid
                name: $name
            } 
        ) 
        
        {
            id
            name
        }
    }'''

    variables = { 
            "siteid": site_id, 
            "name": newname
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Update extensions enabled for a site
#
def updatesiteextensions(APIURL, APIKEY, site_id, ids, doprint=True, output=False):
    query = '''
    mutation UpdateSiteExtensions($siteid: ID!, $ids: [ID!]) {

        update_site_extensions (
            input: {
                id: $siteid
                extension_ids: $ids
            } 
        ) 

        {
            site {
                id
                parent_id
                scope {
                    included_urls
                    protocol_options
                }
                application_logins {
                    login_credentials {
                        id
                        label
                        username
                    }
                    recorded_logins {
                        id
                        label
                    }
                }
                scan_configurations{
                    id
                }
                extensions {
                        id
                }
                ephemeral
                email_recipients {
                    id
                    email
                }
                agent_pool{
                    id
                    name
                    description
                }
           }
        }
    }'''

    variables = {
        "siteid": site_id,
        "ids": ids
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result


#
# Assign sites to an agent pool
#
def assignsitestoagentpool(APIURL, APIKEY, site_ids, agentpoolid, doprint=True, output=False):

    query = '''
    mutation AssignSitesToAgentPool($siteids: [ID!], $agentpoolid: ID!) {

        assign_sites_to_agent_pool(
            input: {
                site_ids : $siteids
                agent_pool_id: $agentpoolid
            } 
        ) 

        {
            sites {
                id
                agent_pool{
                    id
                    name
                    description
                }
           }
        }
    }'''

    variables = {
        "siteids": site_ids,
        "agentpoolid": agentpoolid
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Update site scan configuration
#
def updatesitescanconfiguration(APIURL, APIKEY, site_id, scanconfigids, doprint=True, output=False):

    query = '''
    mutation UpdateSiteScanConfigurations($siteid: ID!, $scanconfigids: [ID!]) {

        update_site_scan_configurations(
            input: {
                id : $siteid
                scan_configuration_ids: $scanconfigids
            } 
        ) 

        {
            site {
                id
                name
                scan_configurations {
                    id
                }
           }
        }
    }'''

    variables = {
        "siteid": site_id,
        "scanconfigids": scanconfigids
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result





