#!/usr/bin/node
// Prints the first argument passed to it.
const args = process.argv.slice(2);
let number = 0;
let len = 0;

if (args.length === 0) {
  console.log('Missing number of occurrences');
} else {
  number = parseInt(args[0]);
  if (number > 0) {
    for (; len < number; len++) {
      console.log('C is fun');
    }
  }
}
