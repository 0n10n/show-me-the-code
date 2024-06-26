import mysql.connector

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

conn = mysql.connector.connect(
    host="192.168.99.12",
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
    sql = "INSERT INTO codes (code_name) VALUES(%s)"
    val = [coupon.upper()]
    cursor.execute(sql, val)
    conn.commit()

cursor.close()
conn.close()
