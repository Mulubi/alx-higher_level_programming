#!/bin/bash
# Take in the URL as an argument
url=$1

# Use curl to send a GET request to the URL
# Store the code in a response
response=$(curl -s -o /dev/null -w "%{http_code}" $url)

# Check the status code of the response
if [ $response -eq 200 ]; then
  # if the status code is 200, dis[lay the body response
  curl -s $url
fi
