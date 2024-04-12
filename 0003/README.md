**第 0003 题：** 将 0001 题生成的 200 个激活码（或者优惠券）保存到 **Redis** 非关系型数据库中。

启动redis服务（docker方式）：

docker-compose -f docker-compose-redis.yml up -d

访问redis服务：

redis-cli -h 127.0.0.1 -p 6379 -a password

参考：https://redis.io/docs/connect/clients/python/

