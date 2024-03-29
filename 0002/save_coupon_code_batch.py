import mysql.connector

# 这个版本和gen_save_coupon_code.py的差异是，这个是用cursor.executemany()一次性把优惠码写入数据库的
# 定义需要的优惠码数量
COUNT=200
# 需要把两个单词拼接在一起，每个单词4-6个字符长
NUM=2
WORD_LIST='../res/top_english_words_lower_10000.txt'


def remove_special_characters(text):
    special_characters = ['.', '_']
    for char in special_characters:
        text = text.replace(char, '')
    return text

#只要长度为4-6的单词，忽略其他的
def get_valid_words():
    valid_words=set()
    with open(WORD_LIST, 'r', encoding='utf-8') as file:
        for line in file:
            word=remove_special_characters(line.strip())
            if word and not word.startswith('#'):
                length=len(word)
                if 3<length<7:
                    valid_words.add(word)
    return valid_words

def get_all_codes(words_len46):
    all_codes = []
    for i in range(COUNT):
        coupon = ""
        for x in range(NUM):
            coupon+=words_len46.pop()
        #print(f'{i+1} - {coupon.upper()}') 
        #下面这句注意要添加逗号，才是添加了一个元组，每个元组只有一个元素。如果漏了逗号，后面的cursor.executemany会出错。
        all_codes.append((coupon.upper(),))
    return all_codes

def insert_codes(all_words):
    conn = mysql.connector.connect(
        host="192.168.99.12",
        user="root",
        password="12345678",
        database="coupons"
    )
    conn.connect()

    sql = "INSERT INTO codes (code_name) VALUES (%s)"
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, all_words)
        conn.commit()
        cursor.close()
        conn.close()
    except mysql.connector.Error as error:
        print(error)    

def write_to_file(array, filename):
    print(f'把集合写入到文件 {filename}')
    with open(filename, 'w') as file:
        for item in array:
            file.write(str(item) + '\n')
                
#用了集合来做，反正是随机的
all_codes=[]
words_len46 = get_valid_words()
#write_to_file(words_len46, './words_list.txt')
all_codes=get_all_codes(words_len46)
# 把返回的全部优惠码，一次性写入数据库：
insert_codes(all_codes)
