#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.map((elem) => {
    if (elem === searchElement) {
      count++;
    }
    return (elem);
  });
  return (count);
};
