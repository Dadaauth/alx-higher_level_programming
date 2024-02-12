#!/bin/bash
# sends a GET request to a URL and display the body of the response
curl -sL -w "%{http_code}" $1 -o - | awk '/^200$/{p=1}p'
