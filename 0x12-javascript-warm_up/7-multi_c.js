#!/usr/bin/node
/*
script that prints x times “C is fun”
*/
const occurence = parseInt(process.argv[2]);
let i = 0;

if (isNaN(occurence)) {
  console.log('Missing number of occurrences');
} else {
  while (i < parseInt(process.argv[2])) {
    console.log('C is fun');
    i++;
  }
}
