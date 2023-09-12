#!/usr/bin/node
const list = require('./100-data').list;

const listDup = list.map((elem, idx) => {
  return (elem * idx);
});
console.log(list);
console.log(listDup);
