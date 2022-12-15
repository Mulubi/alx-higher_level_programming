#!/bin/bash
#check if a URL was provided as an argument
if [ -z "$1" ]; then
	echo "Error: No URL provided"
	exit 1
fi

# Send a request to the URL and get a response
response=$(curl -s -l "$1")

# Get the size of the response body ftrom the header
size=$(echo "$response" | grep -i "Content-Length" | cut -d '' -f 2)

# Check if the size was found
if [ -z "$size" ]; then
	echo "Error: Could not get size of response body"
	exit 1
fi

#Display the size of the response body
echo "Size of response body: $size bytes"
