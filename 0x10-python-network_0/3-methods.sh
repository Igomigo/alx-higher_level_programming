#!/bin/bash
# Bash script that displays all HTTP methods the server will accept
curl -sX OPTION "$1"
