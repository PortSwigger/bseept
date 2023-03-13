#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# System wide scan configurations
#
def getscanconfigs(APIURL, APIKEY,doprint=True, output=False):

    # scan_configurations(): [ScanConfiguration!]

    query = '''
    query GetScanConfigurations{
        scan_configurations {
            id
            name
            built_in
            scan_configuration_fragment_json
            last_modified_time
            last_modified_by{
                username
            }
        }
    }
    '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result
