#!/usr/bin/node
/*
script that searches the second biggest integer in the list of arguments
*/

let secondBiggest = 0;
let biggest = 0;
let i = 2;

while (process.argv[i]) {
  if (biggest < parseInt(process.argv[i])) {
    secondBiggest = biggest;
    biggest = parseInt(process.argv[i]);
  }
  if (biggest > parseInt(process.argv[i]) && secondBiggest < parseInt(process.argv[i])) {
    secondBiggest = parseInt(process.argv[i]);
  }
  i++;
}
console.log(secondBiggest);
