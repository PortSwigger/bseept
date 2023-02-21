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
def getscheduleitems(APIURL,APIKEY,sortby="start", sortorder="asc"):
 
    # , sort_order: SortOrder <- DIDNTWORK
    query = '''
        query GetScheduleItems  ($sort_by: SortBy) {
            schedule_items (sort_by: $sort_by) {
                id
                site{
                    id
                    name
                }
                schedule {
                    initial_run_time
                    rrule
                }
                has_run_more_than_once
                scheduled_run_time
            }
        }
        '''

    variables = { 
            "sort_by": sortby, 
            "sort_order": sortorder, 
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)
    print(json.dumps(result))
