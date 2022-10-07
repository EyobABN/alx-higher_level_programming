#!/usr/bin/python3
"""
    Takes in a URL and an email address, sends a POST request to
    the passed URL with the email as a parameter, and finally
    displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        response = requests.get(url)
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
