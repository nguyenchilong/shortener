'use strict';

var ORIGINAL = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-';

/**
 *
 * @param string string want hash
 * @returns {number}
 */
function getCharCodeFromString(string){
	let charCode = 0;
	if(string.length == 0){ return charCode; }
	for (let i = 0; i < string.length; i++) {
		// get charCode from a character
		let ch = string.charCodeAt(i);
		charCode = ((charCode << 5) - charCode) + ch;
		// make sure converted to 32 bit integer
		charCode = charCode & charCode;
	}
	return charCode;
}

/**
 * get a character from string
 * @param index int number index in string need get
 * @returns {*}
 */
function getChar(index) {
	return ORIGINAL[index];
}

/**
 *
 * @param charcode
 * @param length
 * @returns {string}
 */
function generateString(charcode, length) {
	length = length || 64;
	let stack = [], index, result = '', sign = charcode < 0 ? '-' : '';
	// get total charCode value Non-negative integer from string
	charcode = Math.abs(charcode);
	while (charcode >= length) {
		// get index string from string ORIGINAL variable
		index = charcode % length;
		// down total number charCode and limit characters output
		charcode = Math.floor(charcode / length);
		// add char to stack for return
		stack.push(getChar(index));
	}
	// get one more a character from string ORIGINAL variable
	if (charcode > 0) {
		stack.push(getChar(charcode));
	}
	// read all characters from stack with inverse array
	for (let i = (stack.length - 1); i >= 0; i--) {
		result += stack[i];
	}
	return sign + result;
}

/**
 * length is 63 so need replace a char with '-'
 * example: -4aB76 to H4aB76
 *
 * @param text string want hash or make shorter
 * @returns {string|XML|*|void}
 */
function shortener(text) {
	let shorter = generateString(getCharCodeFromString(text), 63);
	return shorter.replace('-', 'H');
}

module.exports.shortener = shortener;