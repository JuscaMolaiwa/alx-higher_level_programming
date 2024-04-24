#!/usr/bin/node
// This script  executes x times a function.

exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
