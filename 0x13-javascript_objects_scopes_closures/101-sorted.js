#!/usr/bin/node
const dict = require('./101-data').dict;
const sortedDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (value in Object.keys(sortedDict)) {
    sortedDict[value].push(key);
  } else {
    sortedDict[value] = [key];
  }
}
console.log(sortedDict);
