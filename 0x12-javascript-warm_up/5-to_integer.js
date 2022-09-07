#!/usr/bin/node

const myVar = parseInt(process.argv[2], 10);
if (!myVar) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Number(process.argv[2]));
}
