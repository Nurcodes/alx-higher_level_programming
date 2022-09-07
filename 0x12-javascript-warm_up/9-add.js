#!/usr/bin/node

const one = process.argv[2];
const two = process.argv[3];

function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

if (process.argv.length < 4) {
  console.log('NaN');
} else if (process.argv.length === 4) {
  add(one, two);
}
