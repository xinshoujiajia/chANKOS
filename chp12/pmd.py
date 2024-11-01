import os  
import re  
  
# 指定要处理的目录  
directory = "./"  # 替换为你的目录路径  
assets_dir = "assets/p"  # 资产目录路径  
  
# 遍历目录下的每一个.md文件  
for filename in os.listdir(directory):  
    if filename.endswith(".md"):  
        file_path = os.path.join(directory, filename)  
          
        # 读取文件内容  
        with open(file_path, 'r', encoding='utf-8') as file:  
            lines = file.readlines()  
          
        # 删除第二行和最后四行  
        if len(lines) > 5:  
            lines.pop(1)  # 删除第二行（索引从0开始，所以第二行是索引1）  
            lines = lines[:-4]  # 删除最后四行  
          
        # 将列表重新组合成字符串，并处理换行符  
        content = ''.join(lines)  
          
        # 进行第一次正则替换，将所有的“\n \n”替换为"\n![](assets/p)\n>"  
        content = re.sub(r'\n \n', f'\n![]({assets_dir})\n>', content)  
          
        # 进行第二次正则替换，将所有的“\n”替换为"\n\n"（注意：这可能会引入额外的空行）  
        content = re.sub(r'\n', '\n\n', content)  
          
        # 将处理后的内容写回原文件  
        with open(file_path, 'w', encoding='utf-8') as file:  
            file.write(content)  
          
        print(f"Processed {filename}")  
  
print("All files processed.")