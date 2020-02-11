#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i, j;
    let x = '';

    for (i = 0; i < this.width; i++) {
      x = x + 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(x);
    }
  }
};
