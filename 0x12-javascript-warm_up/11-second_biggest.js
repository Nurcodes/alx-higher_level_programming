#!/usr/bin/node

const args = process.argv;

args.sort();
for (let x = args.length - 2; x >= 0; x--) {
  if (args.length <= 2) {
    console.log(1);
    break;
  }
  if (args[x] !== args[args.length - 1]) {
    console.log(args[x]);
    break;
  }
}
