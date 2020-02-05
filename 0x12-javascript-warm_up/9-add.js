#!/usr/bin/node
// Prints the first argument passed to it.
const args = process.argv.slice(2);
const len = args.length;
let x, y;

if (len < 2) {
  console.log('NaN');
} else {
  x = parseInt(args[0]);
  y = parseInt(args[1]);
  add(x, y);
}

function add (a, b) { console.log(a + b); }
