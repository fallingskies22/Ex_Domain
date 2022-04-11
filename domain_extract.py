import re
import sys
import getopt

def main(argv):
    print('''
        ███████╗██╗  ██╗        ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
        ██╔════╝╚██╗██╔╝        ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
        █████╗   ╚███╔╝         ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
        ██╔══╝   ██╔██╗         ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
        ███████╗██╔╝ ██╗███████╗██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
        ╚══════╝╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
        USAGE: python3 test.py -i <inputfile> -o <outputfile>
        ''')
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:")
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i"):
         inputfile = arg
      elif opt in ("-o"):
         outputfile = arg
    print('[+]输入的文件为：', inputfile)
    print('[+]输出的文件为：', outputfile)

    fo = open(outputfile, "w")
    topRootDomain = (
                        'com','cn','edu','gov','org','net','cc','live'
                    )
    with open(inputfile, 'r') as f:
        line = f.readline()
        line_num = 1
        while line: 
            # 去除http[s]头、去除换行符
            line1 = line.replace('http://','').replace('https://','').replace('\n','').replace('\r','')
            # 去除路径
            line2 = line1.split('/')[0]
            # 去除端口号
            domain = line2.split(':')[0]
            # print(domain)
            # 提取根域名
            ip = re.findall(r'\d+\.\d+\.\d+\.\d+', domain)
            if ip:
                fo.write(ip[0])
                fo.write('\n')
            else:
                piece = domain.split('.')
                j = -1
                while piece[j]:
                    if piece[j] in topRootDomain:
                        j -= 1
                    else:
                        break
                list1 = piece[j:]
                domain_root = ".".join(i for i in list1)
                
                # 检查结果，报告异常
                check = re.match('[a-zA-Z0-9][-a-zA-Z0-9]{0,62}(\.[a-zA-Z0-9][-a-zA-Z0-9]{0,62})+\.?',domain_root)
                if check == None:
                    print("[*]异常数据","行数: "+str(line_num)+"\n","原始数据: "+line,"提取数据: "+domain_root)
                
                fo.write(domain_root)
                fo.write('\n')
            line = f.readline()
            line_num += 1


if __name__ == "__main__":
    main(sys.argv[1:])