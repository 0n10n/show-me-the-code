import os
import re
import fnmatch

def count_lines(root, filename,ignore_patterns):
    filepath = os.path.join(root, filename)
    
    code_lines, blank_lines, comment_lines = 0,0,0 
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line and line.startswith('#') :
                comment_lines += 1
            elif line and not line.startswith('#') :
                code_lines += 1
            elif not line:
                 blank_lines += 1
    return (code_lines, blank_lines, comment_lines)

def code_static(directory, extensions,ignore_patterns):  
    total_files = 0 
    total_count = []
    for root, dirs, files in os.walk(directory):  
        for filename in files:  
            if any(fnmatch.fnmatch(filename, "*.{}".format(ext)) for ext in extensions) and not any(fnmatch.fnmatch(root, "*{}*".format(ignores)) for ignores in ignore_patterns):  
                #print(os.path.join(root, filename)  )  
                code_lines, blank_lines, comment_lines = count_lines(root, filename,ignore_patterns)
                total_files += 1
                total_count.append((code_lines, blank_lines, comment_lines ))
    sum_code,sum_blank,sum_comment = 0,0,0  
    for code_lines, blank_lines, comment_lines in total_count:
        sum_code+=code_lines
        sum_blank+=blank_lines
        sum_comment+=comment_lines
        
    print(f'有效代码行数：{sum_code} 空行数：{sum_blank} 注释行数：{sum_comment}')    

extensions = ["py","lua"]  
CODE_DIR='../../'
ignore_patterns = ["/venv", "/env", "coreruleset", "learning"]
counts=[]
code_static(CODE_DIR, extensions,ignore_patterns)
