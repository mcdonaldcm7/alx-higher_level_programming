#!/usr/bin/node
const Parent = require('./5-square.js');

class Square extends Parent {
  charPrint (c) {
    let square = '';
    for (let y = 0; y < this.width; y++) {
      for (let x = 0; x < this.width; x++) {
        square += c === undefined ? 'X' : c;
      }
      if (y + 1 < this.width) square += '\n';
    }
    console.log(square);
  }
}

module.exports = Square;
