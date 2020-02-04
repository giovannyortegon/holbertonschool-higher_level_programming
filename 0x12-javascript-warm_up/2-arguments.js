#!/usr/bin/node
// prints a message depending of the number of arguments passed
const Args = process.argv.slice(2);
const len = Args.length;

if (len === 0) {
  console.log('No argument');
} else if (len === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
