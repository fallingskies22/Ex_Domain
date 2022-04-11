# Ex_Domain
按行提取根域名

USAGE: python3 test.py -i <inputfile> -o <outputfile>
  
<img width="945" alt="image" src="https://user-images.githubusercontent.com/34068130/162720225-dd2eb32c-713d-4e09-a410-0944fb1ca1d9.png">

输入文件示例
```
http://www.baidu.com
http://www.baidu.com.cn/12312/jfdkf
https://www.google.com/123
http//123.com
你好
```
  
输出文件示例
<img width="945" alt="image" src="https://user-images.githubusercontent.com/34068130/162720861-5c673146-72c5-404c-9251-49eba1fc05c7.png">
```
baidu.com
baidu.com.cn
google.com
http
你好  
```
