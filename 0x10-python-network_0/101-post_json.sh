#!/bin/bash
# sends a POST request with a file contents
curl -s -X POST -d @$2 $1
