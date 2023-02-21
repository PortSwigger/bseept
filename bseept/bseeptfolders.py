
#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

# Library documentation
# https://github.com/prodigyeducation/python-graphql-client

from python_graphql_client import GraphqlClient
import json

def getsitetreefolders(APIURL,APIKEY):
    headers = { "Authorization": APIKEY }
    client = GraphqlClient(endpoint=APIURL+"/graphql/v1", verify=False, headers=headers)
    result = client.execute('''
    query GetSiteTreeFolders {
        site_tree {
            folders {
                id
                name
            }
        }
    }
    ''')

    print(json.dumps(result))