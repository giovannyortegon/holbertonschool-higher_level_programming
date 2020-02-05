#!/usr/bin/node
// Prints the first argument passed to it.
const args = process.argv.slice(2);
let number = 0;
let i = 0;
let j = 0;
let x = '';

if (args.length === 0) {
  console.log('Missing size');
} else if (isNaN(parseInt(args[0]))) {
  console.log('Missing size');
} else {
  number = parseInt(args[0]);
  if (number > 0) {
    for (; i < number; i++) {
      for (; j < number; j++) {
        x = x + 'X';
      }
      console.log(x);
    }
  }
}
