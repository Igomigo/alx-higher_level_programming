#!/usr/bin/node
/**
 * logMe: function that prints the number of arguments already
 * printed and the new argument value
 */

let count = 0;
exports.logMe = function (item) {
  function inner () {
    return count++ + ': ' + item;
  }
  console.log(inner());
};
