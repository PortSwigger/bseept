#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

# Library documentation
# https://github.com/prodigyeducation/python-graphql-client

from python_graphql_client import GraphqlClient
import bseeptgraphql
import json

def getevents(APIURL,APIKEY,doprint=True, output=False):
    
    query = ''' GetEventLog {
        scaneventlog {
            entires{
                type
                scanner_message_id
                message
                cause
                remediation
                timestamp
                duplicate_count
            }
        }
    }
    '''



    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result
