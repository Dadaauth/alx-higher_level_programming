#!/bin/bash
# sends a GET requwst to a URL and assigns a header variable to the request. It displays the body of the response
curl -sH "X-School-User-Id: 98" $1
