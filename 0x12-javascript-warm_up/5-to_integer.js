#!/usr/bin/node
// Prints the first argument passed to it.
const args = process.argv.slice(2);
const number = isNaN(parseInt(args[0]));

if (number === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[0]));
}
