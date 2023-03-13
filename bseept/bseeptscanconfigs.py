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
# Create a new system-wide scan configuration
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

#
# Update a system-wide scan configuration
#
def updatescanconfig(APIURL, APIKEY, id, name, jsonconfig, doprint=True, output=False):
    query = '''

     mutation UpdateScanConfiguration($id: ID!, $name: String!, $jsonconfig: String!) {
        update_scan_configuration (
            input: {
                id: $id
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
        "id": id,
        "name": name,
        "jsonconfig": jsonconfig
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Update a system-wide scan configuration
#
def deletescanconfig(APIURL, APIKEY, id, force, doprint=True, output=False):
    query = '''

     mutation DeleteScanConfiguration($id: ID!, $force: Boolean) {
        delete_scan_configuration (
            input: {
                id: $id
                force: $force
            }

        )

        {
            id
        }
    }
    '''

    variables = {
        "id": id,
        "force": force,
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result