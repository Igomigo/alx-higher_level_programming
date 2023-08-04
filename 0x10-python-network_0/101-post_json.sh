#!/bin/bash
# Sends a JSON POST request with a file content and displays the response body
curl -sX POST -d @"$2" -H "Content-Type: application/json" "$1"
