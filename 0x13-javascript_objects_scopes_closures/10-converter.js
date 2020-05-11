#!/usr/bin/node
// This function converts a base 10 number to another base

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
