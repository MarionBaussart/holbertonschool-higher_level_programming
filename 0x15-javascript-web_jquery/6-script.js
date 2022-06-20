#!/usr/bin/node

/*
JavaScript script that updates the text of the <header> element
to New Header!!! when the user clicks on DIV#update_header
use the JQuery API
*/

const $ = window.$;
$('#update_header').click(function () {
  $('header').html('New Header!!!');
});
