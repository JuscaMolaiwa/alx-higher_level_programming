#!/bin/bash
# Send GET request with silent mode and capture response including headers and Check if Content-Length exists
curl -sX GET $1 -L
