#!/usr/bin/node
let arg =  process.argv.length;
if (arg < 3) {
	console.log('No argument');
} else if (arg > 3) {
	console.log('Arguments found');
} else {
	console.log('Argument found');
}
