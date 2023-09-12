#!/usr/bin/node
const fs = require('fs');
const filepath1 = process.argv[2];
const filepath2 = process.argv[3];
const destination = process.argv[4];

// Read and write from the first file
fs.readFile(filepath1, 'utf8', (err, data) => {
  if (err) return;
  fs.writeFile(destination, data, (err) => {
    if (err) return (null);
  });
});

// Append from the second file
fs.readFile(filepath2, 'utf8', (err, data) => {
  if (err) return;
  fs.appendFile(destination, data, (err) => {
    if (err) return (null);
  });
});
