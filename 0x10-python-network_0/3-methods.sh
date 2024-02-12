#!/bin/bash
# Displays all the http methods a server will accept on a given url
curl -sI $1 | grep -oP 'Allow: \K.*'
