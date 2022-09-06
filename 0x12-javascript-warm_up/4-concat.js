#!/usr/bin/node
const args = process.argv;
const len = args.length;
let one;
let two;
if (len > 2 && len <= 4) {
  one = args[2];
  two = args[3];
  console.log(one + ' is ' + two);
} else if (len > 2 && len < 3) {
  one = args[2];
  two = 'undefined';
  console.log(one + ' is ' + 'undefined');
} else {
  console.log('undefined is undefined');
}
