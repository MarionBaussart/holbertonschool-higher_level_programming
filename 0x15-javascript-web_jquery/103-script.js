#!/usr/bin/node

/*
JavaScript script that fetches and prints how to say “Hello”
depending on the language
API service: https://www.fourtonfish.com/hellosalut/hello/
language code will be the value entered in the tag INPUT#language_code
translation must be fetched when the user clicks on INPUT#btn_translate
OR presses ENTER when the focus is on INPUT#language_code
translation of “Hello” must be displayed in the HTML tag DIV#hello
use the JQuery API
*/

const $ = window.$;

$().ready(function () {
  $('#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
    $.getJSON(url, function (data) {
      $('#hello').html(data.hello);
    });
  });

  $('#language_code').keypress(function (e) {
    if (e.which === 13) {
      $('#btn_translate').click();
    }
  });
});
