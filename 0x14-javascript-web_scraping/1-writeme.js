#!/usr/bin/node
const args = process.argv.slice(2);
const fs = require('fs');

try {
  fs.writeFileSync(args[0], args[1], 'utf-8');
} catch (err) {
  console.error(err);
}
