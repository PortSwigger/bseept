
#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

# Library documentation
# https://github.com/prodigyeducation/python-graphql-client

import bseeptgraphql
import json

def getsitetreefolders(APIURL,APIKEY,doprint=True, output=False):

    query = '''
    query GetSiteTreeFolders {
        site_tree {
            folders {
                id
                name
                parent_id
            }
        }
    }
    '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

def createfolder(APIURL,APIKEY,doprint=True, output=False):
    query = '''CreateFolder {
        site_tree {
            folders {
                id
                name
                parent_id
            }
        }
    }
    '''

    variables = { 
            "sort_by": sortby, 
            "sort_order": sortorder, 
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result
