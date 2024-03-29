import re
from collections import Counter

def count_words(file_path):
    # 读取文档内容
    with open(file_path, 'r') as file:
        content = file.read()
    stop_words = get_stop_words()
    words = list(filter(lambda x: len(x) > 3, re.findall(r'\b\w+\b', content.lower())))
    filtered_list = [word for word in words if word not in stop_words]
    word_counts = Counter(filtered_list)

    return word_counts

def get_stop_words():
    file_path = '../res/stop_words.txt'
    with open(file_path, 'r') as file:
        content = file.read()    
    stop_words = re.findall(r'\b\w+\b', content.lower())
    return stop_words
# 调用函数并打印结果
file_path = '../res/Pride_and_prejudice.txt'  # 替换为实际的文档路径
word_counts = count_words(file_path)
for word, count in word_counts.most_common():
    #pass
    print(f'{word}: {count}')
