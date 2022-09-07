#!/usr/bin/node

function second (myArray) {
  if (myArray.length === 2 || myArray.length === 3) {
    const o = '0';
    return o;
  }

  myArray.sort();
  const res = myArray[myArray.length - 2];
  return res;
}

console.log(second(process.argv));
