#!/usr/bin/node
// This module contains the function nbOccurences

exports.nbOccurences = function (arr, element) {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === element) {
      count++;
    }
  }
  return count;
};
