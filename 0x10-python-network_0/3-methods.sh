#!/bin/bash
# This bash script takes in URL and displays
# all HTTP methods that the server will accept

# Store the URL in a variable
url=$1

# Send an OPTIONS request to the server and store the response
response=$(curl -X OPTIONS -s "$url")

# Extract the Allow header from the response
allow_header=$(echo "$response" | grep -i 'allow:')

# Extract the list of allowed methods from the Allow header
allowed_methods=$(echo "$allow_header" | awk -F':' '{print $2}' | tr -d ' ')

# Display the list of allowed methods
echo "Allowed methods: $allowed_methods"
