#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
const o = 'X';
if (!x) {
  console.log('Missing size');
} else if (process.argv.length > 2) {
  for (let i = 0; i < x; i++) {
    console.log(o.repeat(x));
  }
}
