#!/usr/bin/node
module.exports = {
  addMeMaybe: function (number, callback) {
    number++;
    callback(number);
  }
}
