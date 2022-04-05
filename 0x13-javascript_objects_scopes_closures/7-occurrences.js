#!/usr/bin/node

/*
function that returns the number of occurrences in a list
*/

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let nbOccur = 0;

  while (list[i]) {
    if (list[i] === searchElement) {
      nbOccur++;
    }
    i++;
  }
  return nbOccur;
};
