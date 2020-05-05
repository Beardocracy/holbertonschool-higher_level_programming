#!/usr/bin/node
/*
 * This script prints a message
 */
const args = process.argv.length;
if (args < 3) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
