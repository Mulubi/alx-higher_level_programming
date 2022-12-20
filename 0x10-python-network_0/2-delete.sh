#!/bin/bash
# This bash script sends a DELETE request to the URL
# passed as the first argument and displays the body
# of the response

# Store the URL in a variable
url=$1

# Send a DELETE request and store the response
response=$(curl -X DELETE -s "$url")

# Display the body of the response
echo "$response"
