#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

# Library documentation
# https://github.com/prodigyeducation/python-graphql-client

from python_graphql_client import GraphqlClient

#
# Generic handler function for GraphQL calling
#
def dographql(APIURL,APIKEY, query, variables):
    headers = { "Authorization": APIKEY }
    client = GraphqlClient(endpoint=APIURL+"/graphql/v1", verify=False, headers=headers)
    
    if (variables is not None):
        res = client.execute(query=query, variables=variables)
    else:
        res = client.execute(query=query)

    return res

