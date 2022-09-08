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
}
module.exports = Rectangle;
