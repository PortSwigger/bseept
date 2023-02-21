#
# Burp Suite Enterprise Edition Power Tools
#
# Ollie Whitehouse - @ollieatnowhere
#

import bseeptgraphql
import json

#
# All configured scans on the system
#
def getscans(APIURL,APIKEY):

    # scans(offset: Int, limit: Int, sort_column: ScansSortColumn, sort_order: SortOrder, scan_status: [ScanStatus], site_id: ID, schedule_item_id: ID, scan_end_time_from: Timestamp, scan_end_time_to: Timestamp): [Scan!]

    query = '''
    query GetScans {
        scans {
            id
            status
            site_id
            schedule_item{
                id
                site {
                    id
                    name
                }
                schedule{
                    initial_run_time
                    rrule
                }
                has_run_more_than_once
                scheduled_run_time
            }
            scheduled_start_time
            start_time
            end_time
            duration_in_seconds
            scan_failure_code
            scan_metrics {
                crawl_request_count
                unique_location_count
                audit_request_count
                crawl_and_audit_progress_percentage
                scan_phase
                audit_start_time
                current_url
            }
            scan_failure_message
            scan_delta {
                new_issue_count
                repeated_issue_count
                regressed_issue_count
                resolved_issue_count
            }
            issue_counts {
                total
                high {
                    total
                    firm
                    tentative
                    certain
                }
                medium {
                    total
                    firm
                    tentative
                    certain
                }
                low {
                    total
                    firm
                    tentative
                    certain
                }
                info {
                    total
                    firm
                    tentative
                    certain
                }
            }
            
            scanner_version
            scanner_build_number
        }
    }
    '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)
    print(json.dumps(result))

#
# System wide scan configurations
#
def getscanconfigs(APIURL, APIKEY):

    # scan_configurations(): [ScanConfiguration!]

    query = '''
    query GetScanConfigurations{
        scan_configurations {
            id
            name
            built_in
            scan_configuration_fragment_json
            last_modified_time
            last_modified_by{
                username
            }
        }
    }
    '''

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, None)
    print(json.dumps(result))

#
# Issues for a specified scan
#
def getscanissues(APIURL, APIKEY, scan_id):

    # scan(id: ID!): Scan

    # issues(start: 0, count: 44, type_index: "3146256")

    query= '''
    query GetScan ($id: ID!) {
        scan(id: $id ) {

            issues(start: 0, count: 9999){
                issue_type{
                    name
                    description_html
                    remediation_html
                    vulnerability_classifications_html
                    references_html
                }
                confidence
                display_confidence
                serial_number
                severity
                description_html
                remediation_html
                path
                origin
                novelty
                tickets {
                    jira_ticket {
                        id
                        external_key
                        issue_type
                        summary
                        project
                        status
                        priority
                    }
                    gitlab_issue {
                        id
                        project_id
                        issue_details {
                            title
                            state
                        }
                    }
                    trello_card {
                        id
                        card_details {
                            title
                            board_name
                            list_name
                        }
                    }
                    link_url
                    link_id
                    date_added
                }
                generated_by_extension {
                    name
                }

            }
        }
    }
    '''

    variables = {"id": scan_id}

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)
    print(json.dumps(result))


#
# Report for a specific scan
#
def getscanreport(APIURL, APIKEY, scan_id, include_falsepositives, report_type = "detailed", timezone_offset = 0, format="report_html" ):

    # scan_report(scan_id: ID!, timezone_offset: Int, report_type: ScanReportType, include_false_positives: Boolean, severities: [Severity]): ScanReport

    query = '''
    query GetScanReport($id: ID!, $include_false_positives: Boolean, $report_type: ScanReportType!, $timezone_offset: Int) {
        scan_report(scan_id: $id, include_false_positives: $include_false_positives, report_type: $report_type, timezone_offset: $timezone_offset) {
            report_html
        }
    }
    '''

    variables = {"id": scan_id, "include_false_positives": include_falsepositives, "report_type": report_type, "timezone_offset": timezone_offset }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)
    print(json.dumps(result))

#
# Report for a specific scan in XML
#
def getscanreportxml(APIURL, APIKEY, scan_id, include_falsepositives, timezone_offset = 0):
    
    # burp_xml_report(scan_id: ID!, timezone_offset: Int, include_false_positives: Boolean, severities: [Severity], base64_encode_requests_and_responses: Boolean): BurpReport
    
    query = '''
    query GetScanReport($id: ID!, $include_false_positives: Boolean, $timezone_offset: Int) {
        burp_xml_report(scan_id: $id, include_false_positives: $include_false_positives, timezone_offset: $timezone_offset) {
            report_xml
        }
    }
    '''

    variables = {"id": scan_id, "include_false_positives": include_falsepositives, "timezone_offset": timezone_offset }

    result = bseeptgraphql.dographql(APIURL, APIKEY, query, variables)
    print(json.dumps(result))
