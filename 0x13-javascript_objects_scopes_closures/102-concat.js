#!/usr/bin/node

/*
script that concats 2 files
*/
const fs = require('fs');
const fileSourceOne = process.argv[2];
const fileSourceTwo = process.argv[3];
const fileDestination = process.argv[4];

fs.readFile(fileSourceOne, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileSourceTwo, 'utf8', (err, dataTwo) => {
    if (err) {
      console.error(err);
      return;
    }
    fs.writeFile(fileDestination, data + '\n' + dataTwo, function (err) {
      if (err) {
        return console.log(err);
      }
    });
  });
});
