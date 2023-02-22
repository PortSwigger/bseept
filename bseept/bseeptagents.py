#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

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