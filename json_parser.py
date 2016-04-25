import json
from pprint import pprint

def parse_event_data(event_json):
    '''
    Modify the code below to capture the remaining parameters listed in the
    `parsed_event_data`-dictionary from the webhook event.  Once you've
    finished, print out the results with the `print_results()`-function
    provided.

    Inputs:
        event_json - (String)
            The raw JSON string that was delivered to the webhook endpoint.
    '''

    # Convert JSON to Python Object
    event = json.loads(event_json)

    # Fill in the following
    parsed_event_data = {
        'timestamp': event.get("created"),
        'event_type': None,
        'event_id': None,
        'object_type': None,
        'object_id': None,
    }

    # Print the results using the premade method
    print_results(event, parsed_event_data)


def print_results(event, parsed_event_data):
    '''
    Prints the results from the `parse_event_data()`-function.

    Input:
        event - (Dictionary)
            The decoded JSON object.
        parsed_event_data - (Dictionary)
            The parameters that were parsed from the raw data.
    '''

    print ''
    print 'Received JSON:'
    print '-' * 80
    print pprint(event)
    print ''

    print 'Parsed Event Data:'
    print '-' * 80
    for k, v in parsed_event_data.items():
        print "{0:>11} => {1}".format(k, str(v))
    print ''
