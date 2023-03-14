#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# Create site email receipient
#
def createsiteemailreceipient(APIURL, APIKEY, id, email, doprint=True, output=False):
    query = '''

     mutation CreateSiteEmailRecipient($id: ID!, $email: String!) {
        create_site_email_recipient(
            input: {
                site_id: $id
                email_recipient: {
                    email: $email
                }
            }

        )

        {
            email_recipient {
                id
                email
            }
        }
    }
    '''

    variables = {
        "id": id,
        "email": email
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Update site email receipient
#
def updatesiteemailreceipient(APIURL, APIKEY, id, email, doprint=True, output=False):
    query = '''

     mutation UpdateSiteEmailRecipient($id: ID!, $email: String!) {
        update_site_email_recipient(
            input: {
                id: $id
                email: $email
            }

        )

        {
            email_recipient {
                id
                email
            }
        }
    }
    '''

    variables = {
        "id": id,
        "email": email
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Delete site email receipient
#
def deletesiteemailreceipient(APIURL, APIKEY, id, doprint=True, output=False):
    query = '''

     mutation DeleteSiteEmailRecipient($id: ID!) {
        delete_site_email_recipient(
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

