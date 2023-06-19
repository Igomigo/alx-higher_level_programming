#!/usr/bin/node
/**
 * esrever: function that returns the reversed version of a list
 */

exports.esrever = function (list) {
  const len = list.length - 1;
  const newlist = [];
  for (let i = len; i >= 0; i--) {
    newlist.push(list[i]);
  }
  return newlist;
};
