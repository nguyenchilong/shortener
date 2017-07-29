'use strict';

var shortener = require('./shorteners');

// define string
let my_url = 'http://www.lazada.co.th/maybelline-1-maybellinefashion-brow-ultra-fluffy-brown1-7906309.html';
// call hash make shorter string
let url_shorter = shortener.shortener(my_url);

console.log(url_shorter);