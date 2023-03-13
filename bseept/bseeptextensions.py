#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json


#
# Get the extensions installed
#
def getextensions(APIURL,APIKEY, doprint=True, output=False):
 
    query = '''
        query GetExtensions {
            extensions {
                id
                uploaded_filename
                name
                description
                uploaded_date
                uploaded_by
                bapp_details{
                    bapp_uuid
                    author
                    version
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
# Get the extensions installed
#
def updateextensionname(APIURL, APIKEY, id, name, doprint=True, output=False):
    query = '''

     mutation UpdateCustomExtensionName($id: ID!, $name: String!) {
        update_custom_extension_name (
            input: {
                id: $id
                name: $name
            }

        )

        {
            extension {
                id
                uploaded_filename
                name
                description
                uploaded_date
                uploaded_by
                bapp_details{
                    bapp_uuid
                    author
                    version
                }
            }
        }
    }
    '''

    variables = {
        "id": id,
        "name": name
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

