import os
import jieba
import string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

def load_stopwords(stopwords_file):
    # 从文本文件中读取停用词
    with open(stopwords_file, 'r', encoding='utf-8') as f:
        stopwords = set(f.read().splitlines())
    return stopwords

def custom_tokenizer(text, stopwords):
    # 分词
    tokens = jieba.cut(text)
    
    # 移除停用词
    tokens = [token.strip() for token in tokens if token.strip() and token.strip() not in stopwords]
    
    return tokens

def calculate_top_tfidf_words(documents_folder, stopwords_file, top_n=5):
    # 加载停用词
    stopwords = load_stopwords(stopwords_file)
    
    # 存储每个文件的内容
    document_contents = []
    file_names = []
    
    # 读取每个文件的内容
    for filename in os.listdir(documents_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(documents_folder, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                document_contents.append(content)
                file_names.append(filename)
    
    # 初始化TF-IDF向量化器
    tfidf_vectorizer = TfidfVectorizer(tokenizer=lambda text: custom_tokenizer(text, stopwords))
    
    # 对文档进行TF-IDF向量化
    tfidf_matrix = tfidf_vectorizer.fit_transform(document_contents)
    
    # 获取所有词的列表
    feature_names = tfidf_vectorizer.get_feature_names_out()
    
    # 获取每个文件中TF-IDF值最高的词语
    top_words_per_document = []
    for i, filename in enumerate(file_names):
        # 获取当前文件对应的TF-IDF向量
        tfidf_vector = tfidf_matrix[i]
        
        # 获取TF-IDF值最高的词语的索引
        top_word_indices = tfidf_vector.indices[np.argsort(tfidf_vector.data)[-top_n:]]
        
        # 获取对应的词语
        top_words = [feature_names[index] for index in top_word_indices]
        top_words_per_document.append(top_words)
    
    return dict(zip(file_names, top_words_per_document))

# 指定文件夹路径和停用词文件路径
documents_folder = 'your_documents_folder'  # 更改为你的文件夹路径
stopwords_file = 'stopwords.txt'  # 停用词文件路径

# 计算每个文件里TF-IDF值最高的5个词
top_words_per_document = calculate_top_tfidf_words(documents_folder, stopwords_file)

# 打印结果
for filename, top_words in top_words_per_document.items():
    print(f"Top 5 words in {filename}: {', '.join(top_words)}")
