#!/usr/bin/node
// Prints the number of args already printed, and the new arg

exports.logMe = function (item) {
  this.count = (this.count || 0);
  console.log(this.count + ': ' + item);
  this.count++;
};
