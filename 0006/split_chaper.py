import re
import os

def split_document_by_chapters(input_file, output_folder):
    # 读取输入文档
    with open(input_file, 'r', encoding='utf-8') as file:
        document_content = file.read()
    
    # 使用正则表达式找到章节标题的位置
    chapter_positions = [match.start() for match in re.finditer(r'CHAPTER ', document_content)]
    
    # 添加文档末尾作为最后一个章节的位置
    chapter_positions.append(len(document_content))
    print(chapter_positions)
    # 分割文档并保存成独立的文件
    for i in range(len(chapter_positions) - 1):
        start_index = chapter_positions[i]
        end_index = chapter_positions[i + 1]
        chapter_content = document_content[start_index:end_index].strip()
        
        # 提取章节标题作为文件名
        #chapter_title = re.search(r'CHAPTER ', chapter_content).group()
        chapter_title = f'Chapter {i+1}'
        chapter_filename = f"{chapter_title}.txt"
        
        # 创建输出文件夹（如果不存在）
        os.makedirs(output_folder, exist_ok=True)
        
        # 写入章节内容到文件
        with open(os.path.join(output_folder, chapter_filename), 'w', encoding='utf-8') as chapter_file:
            chapter_file.write(chapter_content)

# 指定输入文档和输出文件夹
input_file = 'input_document.txt'  # 更改为你的输入文件路径
output_folder = 'output_chapters'  # 更改为你想要保存章节文件的文件夹路径

# 执行分割文档的函数
split_document_by_chapters('pandp.txt', 'chapters')
