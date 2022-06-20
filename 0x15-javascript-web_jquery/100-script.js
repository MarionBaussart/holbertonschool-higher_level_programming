#!/usr/bin/node

/*
JavaScript script that updates the text color
of the <header> element to red (#FF0000)
use document.querySelector to select the HTML tag
*/

document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
