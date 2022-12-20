#!/bin/bash
# This bash script sends a DELETE request to the URL
# passed as the first argument and displays the body
# of the response

# Send a DELETE request and store the response
curl -X DELETE -s "${1}"
