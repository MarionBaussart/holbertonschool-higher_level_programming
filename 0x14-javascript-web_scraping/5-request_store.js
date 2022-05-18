#!/usr/bin/node

/*
Script that gets the contents of a webpage and stores it in a file
*/

const axios = require('axios').default;
const fs = require('fs');

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((res) => {
    fs.writeFile(process.argv[3], res.data, err => {
      if (err) {
        return console.log(err);
      }
    });
  });
