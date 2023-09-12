#!/usr/bin/node
module.exports = {
  callMeMoby: function (count, callback) {
    for (let i = 0; i < count; i++) {
      callback();
    }
  }
};
