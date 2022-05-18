#!/usr/bin/node

/*
Script that prints the number of movies
where the character “Wedge Antilles” is present
Wedge Antilles is character ID 18
*/

const axios = require('axios').default;

axios({
  method: 'get',
  url: process.argv[2]
})
  .then((res) => {
    let nbMovies = 0;
    for (const movie of res.data.results) {
      for (const character of movie.characters) {
        if (character.endsWith('18/')) {
          nbMovies++;
        }
      }
    }
    console.log(nbMovies);
  });
