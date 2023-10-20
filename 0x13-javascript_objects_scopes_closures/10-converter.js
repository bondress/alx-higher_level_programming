#!/usr/bin/node
exports.converter = function (base) { return ns => ns.toString(base); };
