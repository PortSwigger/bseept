#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json


#
# Rename a site
#
def updatefalsepositive(APIURL, APIKEY, scanid, issueserialnumber, isfalsepositive, propagationmode, doprint=True, output=False):
    query = '''
    mutation UpdateFalsePositive($scanid: ID!, $serialnumber: ID, $isfalsepositive: Boolean, $propagationmode: FalsePositivePropagationMode) {

        update_false_positive(
            input: {
                scan_id: $scanid
                serial_number: $serialnumber
                is_false_positive: $isfalsepositive
                propagation_mode: $propagationmode
            } 
        ) 

        {
            successful
        }
    }'''

    variables = {
        "scanid": scanid,
        "serialnumber": issueserialnumber,
        "isfalsepositive": isfalsepositive,
        "propagationmode": propagationmode
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

