#!/usr/bin/node
/*
 * This script prints a square the size of the input
 */
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  let xString = '';
  for (let i = 0; i < arg; i++) {
    xString = xString + 'X';
  }
  for (let i = 0; i < arg; i++) {
    console.log(xString);
  }
}
