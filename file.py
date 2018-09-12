#coding: utf-8
import os


#函数功能：
#遍历文件夹中所有文件，如果是文件夹则继续遍历直至完全遍历，将文件的绝对路径名保存在txt文件中
#参数说明： f，需要遍历的文件夹
#result，保存文件绝对路径名的文件，.txt文件
def traverse(f,result):
    fs = os.listdir(f)
    file_path = open(result,'a')
    for f1 in fs:
        tmp_path = os.path.join(f,f1)
        if not os.path.isdir(tmp_path):
            print('file: %s' % tmp_path)
            file_path.write(tmp_path +'\n')
        else:
            print('dir: %s' % tmp_path)
            traverse(tmp_path,result)
    file_path.close()



    



source = 'D:\\@mmg\\GEI_CASIA_B\\gei'
source_path = 'D:\\@mmg\\result\\source_path.txt'
result = 'D:\\@mmg\\result\\result_path.txt'
tmp_path = 'D:\\@mmg\\result'


#os.remove(source_path)
#traverse(source,source_path)



my_file = open(source_path)
first = my_file.readlines()

result_file = open(result,'w')

for i in range(len(first)):
    split_result = first[i].split('\\',4)
    result_path = tmp_path + '\\aei\\' + split_result[4]
    result_file.write(result_path)


#split_result = first.split('\\',4)
#print split_result
#
#result_path = tmp_path + '\\aei\\' + split_result[4]
#print result_path


result_file.close()

    
    







    
