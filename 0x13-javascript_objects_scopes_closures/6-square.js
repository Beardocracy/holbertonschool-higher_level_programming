#!/usr/bin/node
// This module contains the class description for class Square
const SquareOne = require('./5-square.js');

class Square extends SquareOne {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let widthString = '';
    for (let w = 0; w < this.width; w++) {
      widthString += c;
    }
    for (let h = 0; h < this.height; h++) {
      console.log(widthString);
    }
  }
}

module.exports = Square;
