#!/usr/bin/node
// Prints the first argument passed to it.
const Args = process.argv.slice(2);
let len = 0;

Args.forEach(i => { len++; });

if (len === 0) {
  console.log('No argument');
} else {
  console.log(Args[0]);
}
