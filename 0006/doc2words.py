import string

def preprocess_document(document_path,stop_words):
    # 打开文件并读取内容
    with open(document_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 移除标点符号
    content_no_punctuation = content.translate(str.maketrans('', '', string.punctuation + '“”’‘' ))
    
    # 分词并移除停用词
    stop_words = set(open(stop_words, 'r', encoding='utf-8').read().splitlines())
    words = [word.lower() for word in content_no_punctuation.split() if word.lower() not in stop_words]
    
    return words

# 指定文档路径
document_path = 'your_document.txt'  # 更改为你的文档路径

# 预处理文档
preprocessed_content = preprocess_document('chapters/Chapter 1.txt','../res/stop_words.txt')

# 打印处理后的内容
print(len(preprocessed_content))
print(preprocessed_content)
