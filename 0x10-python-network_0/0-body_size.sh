#!/bin/bash
#check if a URL was provided as an argument
if [ -z "$1" ]; then
	echo "Error: No URL provided"
	exit 1
fi

# Send a request to the URL and get a response
response=$(curl -s -l "$1")
