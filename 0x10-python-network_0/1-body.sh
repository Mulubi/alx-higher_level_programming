#!/bin/bash

# Take in the URL as an argument
url=$1

# Use curl to send a GET request to the URL
# Store the status code in a variable
status=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Check the status code
if [ $status -eq 200 ]; then
	  # If the status code is 200, display the body of the response
	    response=$(curl -s "$url")
	      echo "$response"
fi
