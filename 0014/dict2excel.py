
import json
import pandas as pd

json_string = '''
{
    "1": ["张三", 150, 120, 100],
    "2": ["李四", 90, 99, 95],
    "3": ["王五", 60, 66, 68]
}
'''
student_dict = json.loads(json_string)

df = pd.DataFrame(student_dict)

excel_file_path = "students.xlsx"
df.to_excel(excel_file_path, index=False)

print("Excel文件已保存为:", excel_file_path)