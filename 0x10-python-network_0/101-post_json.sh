#!/bin/bash
# sends a POST request with a file contents
curl -sL -X POST -d @$2 -H "Content-Type: application/json" $1
