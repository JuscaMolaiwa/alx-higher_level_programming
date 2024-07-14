#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request using curl, get body size in bytes
body_size=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')

# Display the size of the body in bytes
echo "$body_size"
