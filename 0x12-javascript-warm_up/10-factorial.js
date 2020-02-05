#!/usr/bin/node
// Prints the first argument passed to it.
const args = process.argv.slice(2);
const len = args.length;
let	factorial;

if (len === 0) {
  console.log('1');
} else {
  factorial = fact(args[0]);
  console.log(factorial);
}

function fact (a) {
  if (a ===  0) {
    return 1;
  } else {
    return fact(a - 1) * a;
  }
}
