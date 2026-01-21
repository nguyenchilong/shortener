# Shortener
A mini Node.js module for make string shorter, url-friendly, can't decrypt.
Use this module when you want to encrypt any string shorter for devices limit characters, unique and url friendly.
Easy for use without any setup, without put any options, only require then call now

## Install 

Run with npm installed

```bash
npm install shorteners
```

## Usage

**NodeJS** Version
```js
'use strict';

var shortener = require('shorteners');

// define string
let my_url = 'http://www.lazada.co.th/maybelline-1-maybellinefashion-brow-ultra-fluffy-brown1-7906309.html';
// call hash make shorter string
let url_shorter = shortener.shortener(my_url);

console.log(url_shorter);
// 1XpN4z
```

**Python** Version
```python

from .python.v1.shortener import v1 # or v2

priif __name__ == "__main__":
	print(shortener("http://www.lazada.co.th/maybelline-1-maybellinefashion-brow-ultra-fluffy-brown1-7906309.html"))
```