#!/usr/bin/node
// This script reads and prints the contents of a file

const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) console.log(err);
  if (data) console.log(data);
});
