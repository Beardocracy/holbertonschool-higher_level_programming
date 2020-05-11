#!/usr/bin/node
// This function returns the reversed version of a list

exports.esrever = function (list) {
  const tsil = [];
  let i = 0;
  let j = list.length - 1;
  for (i, j; i < list.length; i++, j--) {
    tsil[i] = list[j];
  }
  return tsil;
};
