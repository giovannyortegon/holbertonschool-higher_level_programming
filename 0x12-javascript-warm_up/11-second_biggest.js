#!/usr/bin/node
// Prints the first argument passed to it.
const args = process.argv.slice(2);
const len = args.length;
const array = [];
let i = 0;

if (len === 0 || len === 1) {
  console.log('0');
} else {
  for (; i < len; i++) {
    array.push(parseInt(args[i], 10));
  }
  array.sort(function fact (a, b) {
    return a - b;
  });
  console.log(array[array.length - 2]);
}
