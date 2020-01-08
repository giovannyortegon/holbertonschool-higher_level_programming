#!/bin/bash
# Script that sends a request to a URL passed as an argument, and displays.
curl -s -o /dev/null -sIw "%{http_code}" "$1"
