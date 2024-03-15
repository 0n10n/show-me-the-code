
#需要的优惠码数量
COUNT=20
WORD_LIST='top_english_words_lower_10000.txt'
TOTAL_LENGTH=10

def get_random_word():
    pass
def get_valid():
    v_words={}
    with open(WORD_LIST, 'r', encoding='utf-8') as file:
        for line in file:
            word=line.strip()
            if word and not word.startswith('#'):
                length=len(word)
                if v_words[length].
                v_words[length].
                
    pass

valid_words=get_valid()

for i in range(COUNT):
    print(i)