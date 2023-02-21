#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# Get the agent pools configured in the system
#
def getagentpools(APIURL,APIKEY):
    
    query = '''
        query GetAgentPools {
            
            agent_pools {
                id
                name
                description
                agents{
                    id
                    name
                }
                sites {
                    id
                    name
                }
            }
        }
        '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)
    print(json.dumps(result))
