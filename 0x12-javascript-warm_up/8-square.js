#!/usr/bin/node
/*
script that prints a square
*/
const size = parseInt(process.argv[2]);// convert to int
let column = 0;
let line = 0;

if (isNaN(size)) { // size isn't an int
  console.log('Missing size');
} else {
  while (line < size) {
    while (column < size) {
      process.stdout.write('X');
      column++;
    }
    process.stdout.write('\n');
    column = 0;
    line++;
  }
}
