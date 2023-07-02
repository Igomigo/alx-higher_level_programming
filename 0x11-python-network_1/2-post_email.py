#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST request to the
passed URL with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == '__main__':

    url = argv[1]
    email = {'email': argv[2]}

    mail_encoded = urllib.parse.urlencode(email)
    mail_bytes = mail_encoded.encode('ascii')

    req = urllib.request.Request(url, mail_bytes)
    with urllib.request.urlopen(req) as response:
        data = response.read()
    decoded_data = data.decode('utf-8')
    print(f"Your email is: {decoded_data}")
