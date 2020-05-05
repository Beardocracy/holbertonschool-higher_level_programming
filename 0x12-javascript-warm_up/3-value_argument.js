#!/usr/bin/node
/*
 * This script prints a message
 */
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
