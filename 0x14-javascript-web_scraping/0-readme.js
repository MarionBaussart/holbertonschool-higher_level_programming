#!/usr/bin/node

/*
Script that reads and prints the content of a file
*/
var fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function(err, content) {
  if (err) {
    return console.log(err);
  }
  console.log(content);
});
