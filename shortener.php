<?php
/**
 *
 * @Project: social_listening
 * @Filename: shortener.php
 * @Author: longnc <nguyenchilong90@gmail.com>
 * @Created Date: 07/30/17 3:32 PM
 *
 * @Description: create short url from real url
 */

class Shortener {

	public function __construct() {}

	/**
	 * length is 63 so need replace a char with '-'
	 * example: -4aB76 to H4aB76
	 *
	 * @param text string want hash or make shorter
	 * @returns {string|XML|*|void}
	 */
	public static function shorterString($string) {
		$charCode = self::getCharCodeFromString($string);
		$shorter = self::generateString($charCode);
		return str_replace('-', 'H', $shorter);
	}

	/**
	 * get charCode from each characters in string input
	 * @param string $string
	 *
	 * @return int|number
	 */
	public static function getCharCodeFromString($string){
		$charCode = 0;
		if(strlen($string) == 0){ return $charCode; }
		for ($i = 0; $i < strlen($string); $i++) {
			// get charCode from a character
			$ch = ord(substr($string, $i, 1));
			// remove this line for use 64 bit length
			$charCode = self::leftShift32($charCode, 0);
			$charCode = (($charCode << 5) - $charCode) + $ch;
			$charCode = $charCode & $charCode;
		}
		return $charCode;
	}

	/**
	 * convert binary from 64 to 32 bit length
	 * @param int $number
	 * @param int $steps
	 *
	 * @return number
	 */
	public static function leftShift32($number, $steps){
		$binary = decbin($number).str_repeat("0", $steps);
		$binary = str_pad($binary, 32, "0", STR_PAD_LEFT);
		$binary = substr($binary, strlen($binary) - 32);
		return $binary{0} == "1" ? -(pow(2, 31) - bindec(substr($binary, 1))) : bindec($binary);
	}

	/**
	 * get a character from index
	 * @param int $index
	 *
	 * @return bool|string
	 */
	public static function getChar($index) {
		$chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-';
		return substr($chars, $index, 1);
	}

	/**
	 * generate string from total charCode from input
	 * @param int $charcode
	 * @param int $length
	 *
	 * @return string
	 */
	public static function generateString($charcode, $length = 63) {
		$length = (empty($length) || !is_numeric( $length)) ? 64 : $length;
		$stack = array();
		$sign = ($charcode < 0) ? '-' : '';
		$charcode = abs($charcode);
		while ($charcode >= $length) {
			$index = ($charcode % $length);
			$charcode = floor($charcode / $length);
			$stack[] = self::getChar($index);
		}
		if ($charcode > 0) {
			$stack[] = self::getChar($charcode);
		}
		$result = array_reverse( $stack);
		return $sign.implode( '', $result);
	}




}
