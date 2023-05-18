-- A script that creates the database 'hbtn_0d_usa' and the table states (in the
-- database 'hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS `cities`(
	id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL),
	state_id INTEGER, FOREIGN KEY(state_id) REFERENCES state(id);
