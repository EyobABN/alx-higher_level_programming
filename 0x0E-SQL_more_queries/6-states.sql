-- creates the database hbtn_0d_usa and the table states
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- make hbtn_0d_usa current
USE hbtn_0d_usa;

-- create table
CREATE TABLE IF NOT EXISTS states(
	id INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256)
);
