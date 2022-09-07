#!/usr/bin/node

const arg = parseInt(process.argv[2]);

const x = function factorial (a) {
  if (!a || a < 1) {
    return 1;
  } else if (a === 0) {
    return 1;
  } else {
    return (a * factorial(a - 1));
  }
};
console.log(x(arg));
