#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (rect) {
    let p = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        p = p + 'X';
      }
      console.log(p);
      p = '';
    }
  }

  rotate (r) {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double (d) {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
