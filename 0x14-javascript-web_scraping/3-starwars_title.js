#!/usr/bin/node

/*
Script that prints the title of a Star Wars movie
where the episode number matches a given integer
*/

const axios = require('axios').default;

axios({
  method: 'get',
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
})
  .then((res) => {
    console.log(res.data.title);
  });
