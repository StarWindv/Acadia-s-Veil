#!/usr/bin/env python3
import os
import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <dir path>")
        sys.exit(1)
    
    target_dir = sys.argv[1]
    
    if not os.path.isdir(target_dir):
        print(f"错误: 目录 '{target_dir}' 不存在")
        sys.exit(1)
    
    for filename in os.listdir(target_dir):
        filepath = os.path.join(target_dir, filename)
        
        # 只处理文件，跳过目录
        if not os.path.isfile(filepath):
            continue
        
        # 条件：不以 .png 结尾 且 不包含 "log"
        if filename.endswith('.png') and 'log' in filename: continue
        else:
            print(f"删除: {filepath}")
            os.remove(filepath)

if __name__ == "__main__":
    main()

