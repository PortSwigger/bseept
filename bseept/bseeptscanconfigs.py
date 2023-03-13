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


#
# Create a new system wide scan configuration
#
def createscanconfig(APIURL, APIKEY, name, jsonconfig, doprint=True, output=False):
    query = '''

     mutation CreateScanConfiguration($name: String!, $jsonconfig: String!) {
        create_scan_configuration (
            input: {
                name: $name
                scan_configuration_fragment_json: $jsonconfig
            }

        )

        {
            scan_configuration {
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
    }
    '''

    variables = {
        "name": name,
        "jsonconfig": jsonconfig
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result