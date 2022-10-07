#!/usr/bin/python3
"""
    Takes in a URL and an email, sends a POST request to the passed URL with
    the email as a parameter, and displays the body of the
    response (decoded in utf-8)
"""
import sys
from urllib import request, parse


if __name__ == "__name__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        email = sys.argv[2]
        form_data = bytes(parse.urlencode([('email', email)]), 'utf-8')
        with request.urlopen(sys.argv[1], data=form_data) as response:
            print(response.read().decode('utf-8'))
