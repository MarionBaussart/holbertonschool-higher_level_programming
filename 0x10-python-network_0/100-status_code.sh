#!/bin/bash
# displays only the status code of the response
curl -s "$1" -IL | grep "HTTP/1.0" | cut -d " " -f 2
