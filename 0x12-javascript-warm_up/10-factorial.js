#!/usr/bin/node
/*
 * This script prints a factorial
 */
const arg = Number(process.argv[2]);
function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}
if (isNaN(arg)) {
  console.log('1');
} else {
  console.log(factorial(arg));
}
