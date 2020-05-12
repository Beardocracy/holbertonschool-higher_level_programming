#!/usr/bin/node
// This script writes the first argument to the file that is second argument
const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (err) => {
  if (err) console.log(err);
});
