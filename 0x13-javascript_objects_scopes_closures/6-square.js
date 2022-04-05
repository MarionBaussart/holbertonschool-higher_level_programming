#!/usr/bin/node

/*
class Square that defines a square and inherits from Rectangle of
4-rectangle.js
*/

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // instance method that print the rectangle using the character c
  charPrint (c) {
    let i = 0;
    let j = 0;
    while (i < this.width) {
      while (j < this.width) {
        if (typeof c === 'undefined') {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
        j++;
      }
      process.stdout.write('\n');
      j = 0;
      i++;
    }
  }
}

module.exports = Square;
