# -*- codeing = utf-8 -*-
# @Time : 2022-07-28 上午 9:56
# @Author : fengzhanwei
# @File : testXwlt.py
# @Software : PyCharm

import xlwt

wookbook=xlwt.Workbook(encoding="utf-8") #创建workbook对象
worksheet=wookbook.add_sheet('sheet1') #创建工作表
worksheet.write(0,0,'hello')           #写入数据，第一行参数“行”，第二行参数“列”，第三个参数“内容”
wookbook.save('student.xls')           #保存数据表

# # 小练习：将九九乘法表写入到xls文件
# wookbook=xlwt.Workbook(encoding="utf-8") #创建workbook对象
# worksheet=wookbook.add_sheet('sheet1') #创建工作表
# for i in range(1,10):
#     for j in range(1,i+1):
#         worksheet.write(i-1,j-1,'{0}*{1}={2}'.format(j,i,i*j))
# wookbook.save('99乘法表.xls')