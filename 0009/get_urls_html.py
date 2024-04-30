#############################
# 一个HTML文件，找出里面的链接
# 稍微限定一下，只限找出body内的链接
#############################


import re
import sys

def extract_body_content(file_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 使用正则表达式匹配<body>标签及其属性
    pattern = r'<body[^>]*>'
    match = re.search(pattern, content)
    
    # 提取<body>标签中的内容
    if match:
        start_index = match.end()
        end_index = content.find('</body>')
        if end_index != -1:
            body_content = content[start_index: end_index]
            return body_content
    return "未找到<body>标签之间的内容"

def extract_links_content(content):
    pattern = r'<a\s+[^>]*\bhref\s*=\s*["\']?([^"\'>\s]+)["\']?[^>]*>'
    
    # 使用 findall() 方法查找所有匹配的链接
    links = re.findall(pattern, content)
    
    return links    
    
# 指定文件路径
file_path = '../res/baidu.html' if len(sys.argv)<2 else sys.argv[1]


# 提取<body>标签之间的内容
body_content = extract_body_content(file_path)
links = extract_links_content(body_content)
# 打印提取的内容
# list(map(lambda x: print(x), my_list))
list(map(lambda i_x: print(f"{i_x[0] + 1}: {i_x[1]}"), enumerate(links)))
