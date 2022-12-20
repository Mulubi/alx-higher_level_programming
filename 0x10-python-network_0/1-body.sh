#!/bin/bash
# Take in the URL as an arg
url=$1

# Send the GET request and store the response
response=$(curl -s -w "%{http_code}\n%{body}" "$url")

# Extract the status code and the body of the response
status_code=$(echo "$response" | awk 'NR==1 {print $0}')
body=$(echo "$response" | awk 'NR>1 {print $0}')

# if the status code is 200, display the body response
if [ "$status_code" -eq 200 ]; then
	echo "$body"
fi
