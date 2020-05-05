#!/usr/bin/node
// Replace value inside const obj
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89;
console.log(myObject);
