-- Creates database and table in MySQL server
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
--use the database
USE hbtn_0d_usa;
--to create the table
CREATE TABLE IF NOT EXISTS `states` (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
	);
