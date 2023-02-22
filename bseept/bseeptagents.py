#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json


#
# Get the currenly unauthorised agents
def getunauthorisedagents(APIURL,APIKEY,doprint=True, output=False):
    
    query = '''
        query GetUnauthorisedAgents {
            
            unauthorized_agents {
                ip
            }
        }
        '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
#
# Get the agents configured in the system
#
def getagents(APIURL,APIKEY,doprint=True, output=False):
    
    query = '''
        query GetAgents {
            
            agents {
                id
                machine_id
                current_scan_count
                ip
                name
                state
                error {
                    code
                    error
                }
                enabled
                max_concurrent_scans
                agent_pool{
                    id
                    name
                }
                warning
            }
        }
        '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
#
#
def renameagent (APIURL,APIKEY,name,id, doprint=True, output=False):
    query = '''
    
     mutation RenameAgent($name: String!, $id: ID!) {
        rename_agent (
            input: {
                name: $name
                id: $id
            }

        )
        
        {
            agent {
                id
                name
            }
        }
    }
    '''

    variables = { 
            "name": name, 
            "id": id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


def enabledisableagent (APIURL,APIKEY,enabled,id, doprint=True, output=False):
    query = '''
    
     mutation EnableAgent($enabled: Boolean!, $id: ID!) {
        enable_agent (
            input: {
                enabled: $enabled
                id: $id
            }

        )
        
        {
            agent {
                id
                name
                enabled
            }
        }
    }
    '''

    variables = { 
            "enabled": enabled, 
            "id": id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


def concurrentscansforagent (APIURL,APIKEY,scans,id, doprint=True, output=False):

    query = '''
    
     mutation UpdateAgentMaxConcurrentScans($scans: Int!, $id: ID!) {
        update_agent_max_concurrent_scans (
            input: {
                max_concurrent_scans: $scans
                id: $id
            }

        )
        
        {
            agent {
                id
                name
                max_concurrent_scans
                enabled
            }
        }
    }
    '''

    variables = { 
            "scans": scans, 
            "id": id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result