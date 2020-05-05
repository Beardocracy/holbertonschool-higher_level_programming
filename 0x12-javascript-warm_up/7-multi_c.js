#!/usr/bin/node
/*
 * This script prints a few messages
 */
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(process.argv[2]); i++) {
    console.log('C is fun');
  }
}
