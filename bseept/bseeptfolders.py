
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

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result


def renamefolder(APIURL,APIKEY,name,id, doprint=True, output=False):
    query = '''
    
     mutation RenameFolder($name: String!, $id: ID!) {
        rename_folder (
            input: {
                name: $name
                id: $id
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
            "id": id
    } 

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables )

    if(doprint is True):
        print(json.dumps(result))
    if(output is True):
        return result

def movefolder(APIURL,APIKEY,id,parentid,doprint=True, output=False):
    query = '''
    
     mutation MoveFolder($id: ID!, $parent_id: ID!) {
        move_folder (
            input: {
                folder_id: $id
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
            "id": id, 
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