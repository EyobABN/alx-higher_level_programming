-- creates user_0d_1 and gives it privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'host' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'host';


