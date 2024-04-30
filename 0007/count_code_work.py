import os
import re
import fnmatch

def count_line(root, filename,ignore_patterns):
    filepath = os.path.join(root, filename)
    
    count = 0
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#') :
                count += 1
    return count

def count_from_dir(directory, extensions,ignore_patterns):  
    total_lines = 0
    total_files = 0 
    for root, dirs, files in os.walk(directory):  
        for filename in files:  
            if any(fnmatch.fnmatch(filename, "*.{}".format(ext)) for ext in extensions) and not any(fnmatch.fnmatch(root, "*{}*".format(ignores)) for ignores in ignore_patterns):  
                #print(os.path.join(root, filename)  )  
                total_lines += count_line(root, filename,ignore_patterns)
                total_files += 1
    return ((total_lines,total_files))
                

extensions = ["py","lua"]  
CODE_DIR='../../'
ignore_patterns = ["/venv", "/env", "coreruleset", "learning"]
lines, files = count_from_dir(CODE_DIR, extensions,ignore_patterns)
print(f'总代码行数：{lines} 总文件数：{files}')