#!/usr/bin/node

const x = process.argv[2];

if (process.argv.length === 2) {
  console.log('Missing number of occurencess');
} else if (process.argv.length > 2) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
