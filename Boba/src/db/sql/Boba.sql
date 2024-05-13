
-- for local sqlite3 it's not needed
-- CREATE DATABASE Boba_Config;
-- USE Boba_Config;

-- Create Software Table
CREATE TABLE software (
    id INT PRIMARY KEY AUTO_INCREMENT,
    version VARCHAR(20) NOT NULL,
    default_database VARCHAR(20) NOT NULL
);

-- Create Language Versions Table
CREATE TABLE language_versions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    software_id INT,
    language_name VARCHAR(20) NOT NULL,
    version VARCHAR(20) NOT NULL,
    is_installed BOOLEAN NOT NULL,
    FOREIGN KEY (software_id) REFERENCES software(id)
);

-- Create Time Format Table
CREATE TABLE time_format (
    id INT PRIMARY KEY AUTO_INCREMENT,
    software_id INT,
    format VARCHAR(2) NOT NULL,
    FOREIGN KEY (software_id) REFERENCES software(id)
);

-- Create Projects Path Table
CREATE TABLE projects_path (
    id INT PRIMARY KEY AUTO_INCREMENT,
    software_id INT,
    path VARCHAR(255) NOT NULL,
    FOREIGN KEY (software_id) REFERENCES software(id)
);

-- Create Domains Table
CREATE TABLE domains (
    id INT PRIMARY KEY AUTO_INCREMENT,
    software_id INT,
    domain VARCHAR(255) NOT NULL,
    route VARCHAR(255) NOT NULL,
    FOREIGN KEY (software_id) REFERENCES software(id)
);
