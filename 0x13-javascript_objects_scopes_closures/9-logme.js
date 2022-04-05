#!/usr/bin/node

/*
function that prints the number of arguments already printed
and the new argument value
<number arguments already printed>: <current argument value>
*/
let counter = -1;

exports.logMe = function (item) {
  const currentArgValue = item;

  counter += 1;

  return console.log(counter + ': ' + currentArgValue);
};
