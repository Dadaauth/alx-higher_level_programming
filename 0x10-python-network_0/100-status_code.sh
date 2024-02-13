#!/bin/bash
# sends a request to a url and retrieves its status code
curl -s -o /dev/null -w %{http_code} $1
