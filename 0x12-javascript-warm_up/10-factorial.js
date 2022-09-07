#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

function factorial (num) {
  if (!num || num > 0) {
    return (1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
console.log(factorial(arg));
