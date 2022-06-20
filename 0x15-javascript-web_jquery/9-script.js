#!/usr/bin/node

/*
avaScript script that fetches from https://fourtonfish.com/hellosalut/?lang=fr
and displays the value of hello from that fetch in the HTML tag DIV#hello
use the JQuery API
*/

const $ = window.$;
const url = 'https://fourtonfish.com/hellosalut/?lang=fr';
$.getJSON(url, function (data) {
  $('#hello').html(data.hello);
});
