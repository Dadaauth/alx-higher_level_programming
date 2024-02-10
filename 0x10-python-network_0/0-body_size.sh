#!/bin/bash
# Using curl, displays the size of the body of the response message sent from a server.
curl -s -I $1 | grep -oP 'Content-Length: \K\d+'
