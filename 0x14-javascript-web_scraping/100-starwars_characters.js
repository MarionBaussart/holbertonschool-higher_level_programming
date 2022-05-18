#!/usr/bin/node

/*
prints all characters of a Star Wars movie
*/

const axios = require('axios').default;

axios({
  method: 'get',
  url: 'https://swapi-api.hbtn.io/api/people/'
})
  .then((res) => {
    for (const people of res.data.results) {
      for (const movie of people.films) {
        if (movie.endsWith(process.argv[2] + '/')) {
          console.log(people.name);
        }
      }
    }
  });
