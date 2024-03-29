import redis

# 这个版本和gen_coupon_code.py的差异是，这个是单行写入数据库的
#需要的优惠码数量
COUNT=200
#需要两个单词拼接在一起
NUM=2
WORD_LIST='../res/top_english_words_lower_10000.txt'

def remove_special_characters(text):
    special_characters = ['.', '_']
    for char in special_characters:
        text = text.replace(char, '')
    return text

#只要长度为4-6的单词，忽略其他的
def get_valid_words():
    with open(WORD_LIST, 'r', encoding='utf-8') as file:
        for line in file:
            word=remove_special_characters(line.strip())
            if word and not word.startswith('#'):
                length=len(word)
                if 3<length<7:
                    all_words.add(word)

#用了集合来做，反正是随机的
all_words=set()
get_valid_words()
list_name  ='coupon'
redis_host = 'localhost'
redis_port = 6379
redis_auth = 'password'


r = redis.Redis(host=redis_host, port=redis_port, db=0, password=redis_auth)
r.delete(list_name)

for i in range(COUNT):
    coupon = ""
    for x in range(NUM):
        coupon+=all_words.pop()
    val = coupon.upper()
    #print(f'{i+1} - {val}') 
    r.rpush(list_name, val)
    
codes_list = r.lrange(list_name, 0, -1)

# 打印列表中的所有元素
i=0
for coupon in codes_list:
    i+=1
    print("{} - {}".format(i, coupon.decode('utf-8')))   