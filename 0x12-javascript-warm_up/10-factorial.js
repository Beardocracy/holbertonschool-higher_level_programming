#!/usr/bin/node
/*
 * This script prints a factorial
 */
const arg1 = Number(process.argv[2]);
const arg2 = Number(process.argv[3]);
const facto = arg1 ** arg2;
if (isNaN(facto)) {
  console.log('1');
} else {
  console.log(facto);
}
