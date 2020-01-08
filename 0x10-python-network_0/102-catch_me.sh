#!/bin/bash
# Script that makes a request that causes the server to respond with a message.
curl -sLX PUT -H "origin:HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
