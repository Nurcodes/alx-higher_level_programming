#!/usr/bin/node
// Store the contents of a body response to a file

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
