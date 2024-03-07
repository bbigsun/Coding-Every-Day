#!/bin/bash

root_path=`pwd`

# 获取当前日期 2024/03/06
year=`date "+%Y"`
month=`date "+%m"`
day=`date "+%d"`

# 创建目录结构
cd ${root_path} && mkdir -p ${year}/${month}/${day}

# 创建README文件
cd ${year}/${month}/${day}
touch README.md

# 自动提交代码
git add .
git commit -m "Auto Update"
git push origin main