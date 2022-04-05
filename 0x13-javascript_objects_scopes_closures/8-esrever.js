#!/usr/bin/node

/*
function that returns the reversed version of a list
*/

exports.esrever = function (list) {
  let i = 0;
  let tmp;
  let size = list.length - 1;

  while (i <= size) {
    tmp = list[i];
    list[i] = list[size];
    list[size] = tmp;
    i++;
    size--;
  }

  return list;
};
