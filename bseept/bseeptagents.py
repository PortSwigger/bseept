#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json


#
# Get the currently unauthorised agents
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


#
#
#
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


#
#
#
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


#
#
#
def createpool (APIURL,APIKEY,name,desc, doprint=True, output=False):

    query = '''
    
     mutation CreateAgentPool($name: String!, $desc: String) {
        create_agent_pool (
            input: {
                name: $name
                description: $desc
            }

        )
        
        {
            agent_pool {
                id
                name
                description
            }
        }
    }
    '''

    variables = { 
            "name": name, 
            "desc": desc
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
#
#
def updatepool (APIURL,APIKEY,id,name,desc,doprint=True, output=False):

    query = '''
    
     mutation UpdateAgentPool($id: ID!, $name: String!, $desc: String) {
        update_agent_pool (
            input: {
                agent_pool_id: $id
                name: $name
                description: $desc
            }

        )
        
        {
            agent_pool {
                id
                name
                description
            }
        }
    }
    '''

    variables = { 
            "id": id,
            "name": name, 
            "desc": desc
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

#
#
#
def deletepool (APIURL,APIKEY,id, doprint=True, output=False):

    query = '''
    
     mutation DeleteAgentPool($id: ID!) {
        delete_agent_pool (
            input: {
                id: $id
            }

        )
        
        {
            id
        }
    }
    '''

    variables = { 
            "id": id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


#
# Authorize a specific agent
#
def authorizeagent(APIURL, APIKEY, id, agentpool, doprint=True, output=False):
    query = '''

     mutation AuthorizeAgent($id: ID!, $agentpool: ID) {
        authorize_agent (
            input: {
                machine_id: $id
                agent_pool_id: $agentpool
            }

        )

        {
            agent {
                id
                name
                machine_id
                ip
            }
        }
    }
    '''

    variables = {
        "id": id,
        "agentpool": agentpool
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Deauthorize a specific agent
#
def deauthorizeagent(APIURL, APIKEY, id, doprint=True, output=False):

    query = '''

     mutation DeauthorizeAgent($id: ID!) {
        deauthorize_agent (
            input: {
                id: $id
            }
        )

        {
            id
        }
    }
    '''

    variables = {
        "id": id
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Move agent from its current pool to a new one
#
def moveagentpool(APIURL, APIKEY, id, agentpool, doprint=True, output=False):
    query = '''

     mutation MoveAgentPool($id: ID!, $agentpool: ID!) {
        move_agent_pool(
            input: {
                agent_id: $id
                agent_pool_id: $agentpool
            }

        )

        {
            agent {
                id
                name
                machine_id
                ip
                agent_pool { 
                    id
                    name
                }
            }
        }
    }
    '''

    variables = {
        "id": id,
        "agentpool": agentpool
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result