#!/usr/bin/node
const args = process.argv;
let num = args[2];
if (args.length === 3) {
  num = parseInt(args[2]);
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
