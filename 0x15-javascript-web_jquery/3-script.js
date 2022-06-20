#!/usr/bin/node

/*
avaScript script that updates the text color of the <header> element
to red (#FF0000) when the user clicks on the tag DIV#red_header
use the JQuery API
*/

window.$('#red_header').click(function () {
  window.$('header').addClass('red');
});
