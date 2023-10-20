#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (array, now) {
    array.push(now);
    return array;
  }, []);
};
