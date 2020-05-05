#!/usr/bin/node
/*
 * This script searches for the second biggest integer in the list of args
 */
const numArgs = process.argv.length;
if (numArgs < 4) {
  console.log(0);
}
let big1 = Number(process.argv[2]);
let big2;
if (Number(process.argv[3]) > big1) {
  big2 = big1;
  big1 = Number(process.argv[3]);
} else {
  big2 = Number(process.argv[3]);
}
for (let i = 4; i < numArgs; i++) {
  if (Number(process.argv[i]) > big1) {
    big2 = big1;
    big1 = Number(process.argv[i]);
  } else if (Number(process.argv[i]) > big2) {
    big2 = Number(process.argv[i]);
  }
}
if (numArgs >= 4) {
  console.log(big2);
}
