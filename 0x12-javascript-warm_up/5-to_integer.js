#!/usr/bin/node
/*
 * This script tries to convert an argument to integer
 */
const arg = Number(process.argv[2]);
if (isNaN(arg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + arg);
}
