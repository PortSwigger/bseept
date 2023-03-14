#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# Create a site login credential
#
def createsitelogincred(APIURL, APIKEY, id, label, username, password, doprint=True, output=False):
    query = '''

     mutation CreateSiteLoginCredential($id: ID!, $label: String!, $username: String!, $password: String!) {
        create_site_login_credential(
            input: {
                site_id: $id
                login_credential: {
                    label: $label
                    username: $username
                    password: $password
                }
            }

        )

        {
            login_credential {
                id
                label
                username
            }
        }
    }
    '''

    variables = {
        "id": id,
        "label": label,
        "username": username,
        "password": password
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Update a site login credential
#
def updatesitelogincred(APIURL, APIKEY, id, label, username, password, doprint=True, output=False):
    query = '''

     mutation UpdateSiteLoginCredential($id: ID!, $label: String!, $username: String!, $password: String!) {
        update_site_login_credential(
            input: {
                id: $id
                label: $label
                username: $username
                password: $password
            }

        )

        {
            login_credential {
                id
                label
                username
                password
            }
        }
    }
    '''

    variables = {
        "id": id,
        "label": label,
        "username": username,
        "password": password
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Delete a site login credential
#
def deletesitelogincred(APIURL, APIKEY, id, doprint=True, output=False):
    query = '''

     mutation DeleteSiteLoginCredential($id: ID!) {
        delete_site_login_credential(
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

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result


#
# Create a site recorded login credential
#
def createsiterecordedlogin(APIURL, APIKEY, id, label, script, doprint=True, output=False):
    query = '''

     mutation CreateSiteRecordedLogin($id: ID!, $label: String!, $script: String!) {
        create_site_recorded_login(
            input: {
                site_id: $id
                recorded_login: {
                    label: $label
                    script: $script
                }
            }

        )

        {
            recorded_login {
                id
                label
                script
            }
        }
    }
    '''

    variables = {
        "id": id,
        "label": label,
        "script": script
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Delete a site recorded login credential
#
def deletesiterecordedlogin(APIURL, APIKEY, id, doprint=True, output=False):

    query = '''

     mutation DeleteSiteRecordedLogin($id: ID!) {
        delete_site_recorded_login(
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

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result