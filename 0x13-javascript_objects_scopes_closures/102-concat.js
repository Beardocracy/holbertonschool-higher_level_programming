#!/usr/bin/node
// Concats 2 files
const fs = require('fs');

const a = fs.readFileSync(process.argv[2]);
const b = fs.readFileSync(process.argv[3]);
fs.writeFileSync(process.argv[4], a + b);
