#!/bin/bash
# Displays the response body of a header variable sent in a GET request.
curl -sH "X-School-User-Id: 98" "$1"
