#!/usr/bin/node
// This script import a dictionary of and prints in a rearranged way
const dict = require('./101-data.js').dict;

const newDict = {};
let key;
let value;
for (key in dict) {
  value = dict[key];
  if (newDict[value] === undefined) {
    newDict[value] = [];
    newDict[value].push(key);
  } else {
    newDict[value].push(key);
  }
}
console.log(newDict);
