#!/usr/bin/node
// This function converts a base 10 number to another base

exports.converter = function (base) {
  const customConv = function (number) {
    return number.toString(base);
  };
  return customConv;
};
