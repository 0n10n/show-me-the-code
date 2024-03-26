use mysql;
delete from user where host='localhost' and user='root';
update user set host='%' where host='localhost';
FLUSH PRIVILEGES;
DROP DATABASE IF EXISTS coupons;
CREATE DATABASE coupons CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE coupons;
CREATE TABLE codes(
   id INT AUTO_INCREMENT PRIMARY KEY,
   code_name VARCHAR(16) NOT NULL,
   discount DECIMAL(10,2)  NULL
);