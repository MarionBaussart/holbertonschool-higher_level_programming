#!/bin/bash
# display Content-Length
curl -s "$1" | wc -c
