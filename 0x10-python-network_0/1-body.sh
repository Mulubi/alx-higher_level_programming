#!/bin/bash

# Take in the URL as an arg
url=$1

# Use curl to send a GET request to the URL
# Store the status code in a variable
status=$(curl -sL -o /dev/null -w "%{http_code}" "$url")

# Check the status code
if [ $status -eq 200 ]; then
	# If the status code is 200, display the body of the
	# response
	response=$(curl -sL "$url")
	echo "$response"
fi
