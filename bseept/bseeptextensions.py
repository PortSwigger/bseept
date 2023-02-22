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
