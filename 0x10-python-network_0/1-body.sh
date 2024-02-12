#!/bin/bash
# sends a GET request to a URL and display the body of the response
curl -sL -w "%{http_code}" -o /dev/null $1 | grep -q 200 && curl -sL $1
