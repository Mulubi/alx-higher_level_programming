#!/bin/bash
# Take in the URL as an arg
url=$1

# Send the GET request and store the response
response=$(curl -s -w "%{http_code}\n%{size_download}\n%{body}" "$url")

# Extract the status code and the body of the response
status_code=$(echo "$response" | awk 'NR==1 {print $0}')
size=$(echo "$response" | awk 'NR==2 {print $0}')
body=$(echo "$response" | awk 'NR>2 {print $0}')

# if the status code is 200 and size > 0, display the body response
if [ "$status_code" -eq 200 ] && [ "$size" -gt 0 ]; then
	echo "$body"
fi
