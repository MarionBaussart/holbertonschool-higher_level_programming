#!/usr/bin/node

/*
Script that display the status code of a GET request
*/

const axios = require('axios').default;

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((res) => {
    console.log('code: ' + res.status);
  })
  .catch((error) => {
    console.log('code: ' + error.response.status);
  });
