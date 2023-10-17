#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((tot, now) => tot === searchElement ? tot + 1 : tot, 0);
};
