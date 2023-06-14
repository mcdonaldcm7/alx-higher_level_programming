#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rect = '';
    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        rect += 'X';
      }
      if (y + 1 < this.height) rect += '\n';
    }
    console.log(rect);
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  'double' () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
