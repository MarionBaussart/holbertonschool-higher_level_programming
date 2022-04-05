#!/usr/bin/node
/*
class Rectangle that defines a rectangle
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w; // Initialize the instance attribute width
      this.height = h;
    }
  }

  // instance method that print the rectangle using the character X
  print () {
    let i = 0;
    let j = 0;
    while (i < this.height) {
      while (j < this.width) {
        process.stdout.write('X');
        j++;
      }
      process.stdout.write('\n');
      j = 0;
      i++;
    }
  }

  // instance method that exchanges the width and the height of rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // instance method that multiples the width and the height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
