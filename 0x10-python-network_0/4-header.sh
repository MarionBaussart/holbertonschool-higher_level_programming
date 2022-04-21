#!/bin/bash
# displays all HTTP methods the server will accept
curl -sLX GET "$1" -H "X-School-User-Id: 98"
