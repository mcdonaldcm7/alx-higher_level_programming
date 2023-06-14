#!/usr/bin/node
const dict = require('./101-data.js').dict;
const values = [...new Set(Object.values(dict))];
values.sort();
const newDict = {};
for (const val of values) {
  let arr = [];
  for (const key in dict) {
    if (val === dict[key]) {
      arr.push(key);
    }
  }
  newDict[val] = arr;
  arr = [];
}
console.log(newDict);
