#!/usr/bin/node
/*
script that returns the addition of 2 integers
*/

exports.callMeMoby = function (x, theFunction) {
  let i = 0;

  while (i < x) {
    theFunction();
    i++;
  }
};
