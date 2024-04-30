# 输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights
# 当用户输入敏感词语，则用 星号 * 替换

def read_lines_from_file(file_path):
    lines = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip()) 
    return lines


filtered_word_file = '../res/filtered_words.txt'
filtered_words = read_lines_from_file(filtered_word_file)
while True:
    try:
        user_input = input("请输入内容：").encode('utf-8').decode('utf-8')
    except UnicodeDecodeError:
        print("输入包含了无法解码的字符，请重新输入。")
    is_matched = any(item in user_input for item in filtered_words)
    if is_matched:
        for word in filtered_words:
            if word in user_input:
                print(user_input.replace(word, "*"*len(word)))
                break
    else:
        print(user_input)
    if user_input == '88' :
        print("退出程序")
        break