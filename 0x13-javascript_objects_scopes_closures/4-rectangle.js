#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }

  rotate () {
    let aux = 0;

    aux = this.width;
    this.width = this.height;
    this.height = aux;
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
