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
}

module.exports = Rectangle;
