#!/usr/bin/node
/*
 * This script prints a message
 */
const args = process.argv.length;
if (args < 3) {
  console.log('No argument');
} else if (args === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
