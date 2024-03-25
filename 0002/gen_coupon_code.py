import mysql.connector

#需要的优惠码数量
COUNT=200
#需要两个单词拼接在一起
NUM=2
WORD_LIST='top_english_words_lower_10000.txt'

def get_random_word():
    pass

#只要长度为4-6的单词，忽略其他的
def get_valid_words():
    with open(WORD_LIST, 'r', encoding='utf-8') as file:
        for line in file:
            word=line.strip()
            if word and not word.startswith('#'):
                length=len(word)
                if 3<length<7:
                    all_words.add(word)

#用了集合来做，反正是随机的
all_words=set()
get_valid_words()

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="coupons"
)
cursor = conn.cursor()

for i in range(COUNT):
    coupon = ""
    for x in range(NUM):
        coupon+=all_words.pop()
    print(f'{i+1} - {coupon.upper()}') 
    sql = "INSERT INTO codes (code_name) VALUES (%s)"
    val = (coupon)
    cursor.execute(sql, val)    