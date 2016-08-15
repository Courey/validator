#!/usr/bin/env python3

import urllib.request
from urllib.parse import urlparse

def handle_cli_query(user_input):
    results = validate_urls(user_input)
    pretty_print(results)

def validate_urls(urls):
    results = []

    for url in urls:
        url = url.strip()
        valid_syntax = syntax_check(url)

        if valid_syntax:
            status_error = status_check(url)
            if status_error:
                results.append(status_error)
        else:
            results.append(handle_status_failure(url, "invalid syntax"))

    return results

def syntax_check(url):
    try:
        parsed_url = urlparse(url)
        return True if parsed_url.scheme and parsed_url.netloc else False
    except:
        return False

def status_check(url):
    req = urllib.request.Request(url)

    try:
        call = urllib.request.urlopen(req)

    except urllib.request.HTTPError as http_error:
        status_error = "http status is {}".format(http_error.code)
        return handle_status_failure(url, status_error)

    except urllib.request.URLError as url_error:
        return handle_status_failure(url, url_error.reason)

def handle_status_failure(url, error):
    failure = {}
    failure['url'] = url
    failure['success'] = False
    failure['reason'] = error
    return failure

def pretty_print(results):
    for result in results:
        print("_____________________")
        print("")
        print("Url: {}".format(result['url']))
        print("Success: {}".format(result['success']))
        if not result['success']:
            print("Reason for failure: {}".format(result['reason']))

# enable use of the validate_urls function from the command line
while True:
    print("\nPlese enter a comma separated list. type quit to exit the program.")

    try:
        user_input = input("> ").lower().split(",")

    except EOFError as exc:
        break
    if user_input[0] == "quit":
        quit()
    if user_input != "":
        handle_cli_query(user_input)

# This code could be improved for scalability by storing successes and failures in separate arrays.
# A check for the given url could be made to these arrays before running it through validation.
# This would prevent work when the same url is given several times during the same session.

# The validate_urls function could be used by an API endpoint. An endpoint would be created on the app layer
# and either the cotroller (not preferable) or domain entity could utilize this function to validate URLs and pass data forward.
# It would accept a CSV of URLs and would return an array containing dictionaries describing failures.
# If possible, I would place these functions in a domain repo