#!/bin/bash
# Makes a request to trigger the server response "You got me!"
curl -s -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" http://0.0.0.0:5000/catch_me
