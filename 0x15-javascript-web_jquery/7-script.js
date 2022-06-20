#!/usr/bin/node

/*
JavaScript script that fetches the character name
from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json
use the JQuery API
*/

const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
$.getJSON(url, function (data) {
  $('#character').text(data.name);
});
