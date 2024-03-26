## 题目

将 0001 题生成的 200 个激活码（或者优惠券）保存到 **MySQL** 关系型数据库中。 

## 安装

早期 Debian/Ubuntu：
```
sudo apt-get install libmysqlclient-dev
```
2018年后的debian/ubuntu (as of 2018) ：
```
sudo apt install default-libmysqlclient-dev
```
再安装python3需要的mysql库：
```
pip3 install mysql mysql.connector
```
## 一点说明：

- 用docker-compose.yml来启动MySQL服务：docker-compose up -d

