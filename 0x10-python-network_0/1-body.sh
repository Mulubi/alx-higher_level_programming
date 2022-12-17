#!/bin/bash

# Take in the URL as an argument
url=$1

# Use curl to send a GET request to the URL and store the response
response=$(curl -s -o /dev/null -w "%{http_code}" $url)

# Check the status code of the response
if [ $response -eq 200 ]; then
	  # If the status code is 200, display the body of the response
	    curl -s $url
fi
