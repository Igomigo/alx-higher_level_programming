#!/usr/bin/node
/**
 * Script that writes a string to a file.
 * Args: Two command line arguments.
 *     args[2] is the file path while args[3] is the file content, a string.
 * Return: Nothing or error object if an error occurred.
 */

const fs = require('fs');
const args = process.argv;

if (args.length < 4) {
  console.log('Usage: node <file_name> <file_path> <string>');
} else {
  fs.writeFile(`${args[2]}`, `${args[3]}`, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
}
