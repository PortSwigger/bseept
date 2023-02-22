
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

def createfolder(APIURL,APIKEY,name,parentid,doprint=True, output=False):
    query = '''
    
     mutation CreateFolder($name: String!, $parent_id: ID!) {
        create_folder (
            input: {
                name: $name
                parent_id: $parent_id
            }

        )
        
        {
            folder {
                id
                name
                parent_id
            }
        }
    }
    '''

    variables = { 
            "name": name, 
            "parent_id": parentid
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


def renamefolder(APIURL,APIKEY,name,parentid,doprint=True, output=False):
    query = '''
    
     mutation CreateFolder($name: String!, $parent_id: ID!) {
        create_folder (
            input: {
                name: $name
                parent_id: $parent_id
            }

        )
        
        {
            folder {
                id
                name
                parent_id
            }
        }
    }
    '''

    variables = { 
            "name": name, 
            "parent_id": parentid
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

def movefolder(APIURL,APIKEY,name,parentid,doprint=True, output=False):
    query = '''
    
     mutation CreateFolder($name: String!, $parent_id: ID!) {
        create_folder (
            input: {
                name: $name
                parent_id: $parent_id
            }

        )
        
        {
            folder {
                id
                name
                parent_id
            }
        }
    }
    '''

    variables = { 
            "name": name, 
            "parent_id": parentid
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

def deletefolder(APIURL,APIKEY,id,doprint=True, output=False):
    query = '''
    
     mutation DeleteFolder($id: ID!) {
        delete_folder (
            input: {
                id: $id
            }

        )
        
        {
            id
        }
    }
    '''

    variables = { 
            "id": id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result