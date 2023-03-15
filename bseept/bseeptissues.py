#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json


#
# Get details for a specific issue
#
def getissuedetails(APIURL, APIKEY, scanid, issueserialnumber, doprint=True, output=False):
    query = '''

    query getIssue ($scanid: ID!, $serialnumber: ID!) {
        issue (scan_id: $scanid, serial_number: $serialnumber) {
            confidence
            display_confidence
            serial_number
            severity
            description_html
            remediation_html
            path
            origin
            evidence {
                ... on Request {
                    request_index
                    request_count
                    request_segments {
                        ... on DataSegment {
                            data_html
                        }
                        ... on HighlightSegment {
                            highlight_html
                        }
                        ... on SnipSegment {
                            snip_length
                        }
                    }
                }
                ... on Response {
                    response_index
                    response_count
                    response_segments {
                        ... on DataSegment {
                            data_html
                        }
                        ... on HighlightSegment {
                            highlight_html
                        }
                        ... on SnipSegment {
                            snip_length
                        }
                    }
                }
                ... on HttpInteraction {
                    title
                    description_html
                    request {
                        ... on DataSegment {
                            data_html
                        }
                        ... on HighlightSegment {
                            highlight_html
                        }
                        ... on SnipSegment {
                            snip_length
                        }
                    }
                    response {
                        ... on DataSegment {
                            data_html
                        }
                        ... on HighlightSegment {
                            highlight_html
                        }
                        ... on SnipSegment {
                            snip_length
                        }
                    }
                }
                ... on DescriptiveEvidence {
                    title
                    description_html
                }
            }
            novelty
            generated_by_extension {
                name
            }
        }
    }
    '''

    variables = {
        "scanid": scanid,
        "serialnumber": issueserialnumber
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

#
# Update false positive status for an issue
#
def updatefalsepositive(APIURL, APIKEY, scanid, issueserialnumber, isfalsepositive, propagationmode, doprint=True, output=False):
    query = '''
    mutation UpdateFalsePositive($scanid: ID!, $serialnumber: ID, $isfalsepositive: Boolean, $propagationmode: FalsePositivePropagationMode) {

        update_false_positive(
            input: {
                scan_id: $scanid
                serial_number: $serialnumber
                is_false_positive: $isfalsepositive
                propagation_mode: $propagationmode
            } 
        ) 

        {
            successful
        }
    }'''

    variables = {
        "scanid": scanid,
        "serialnumber": issueserialnumber,
        "isfalsepositive": isfalsepositive,
        "propagationmode": propagationmode
    }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)

    if (doprint is True):
        print(json.dumps(result))
    if (output is True):
        return result

