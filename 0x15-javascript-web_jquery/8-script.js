#!/usr/bin/node

/*
JavaScript script that fetches and lists the title for all movies
by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
use the JQuery API
*/

const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.getJSON(url, function (data) {
  for (const movie of data.results) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  }
});
