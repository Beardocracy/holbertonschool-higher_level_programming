#!/usr/bin/node
// This module describes the Rectangle class
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let widthString = '';
    for (let w = 0; w < this.width; w++) {
      widthString += 'X';
    }
    for (let h = 0; h < this.height; h++) {
      console.log(widthString);
    }
  }
}

module.exports = Rectangle;
