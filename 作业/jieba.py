# -*- coding:utf-8 -*-
import jieba


char_x2="考勤机分两大类：第一类是简单打印类，打卡时，原始记录数据通过考勤机直接打印在卡片上，卡片上的记录时间即为原始的考勤信息，对初次使用者无需做任何事先的培训即可立即使用；第二类是存储类，打卡时，原始记录数据直接存储在考勤机内，然后通过计算机采集汇总，再通过软件处理，最后形成所需的考勤信息或查询或打印，其考勤信息灵活丰富，对初次使用者需做一些事先培训才能逐渐掌握其全部使用功能。"
test1 = jieba.cut(char_x2, cut_all=True)
print("全模式: " + "| ".join(test1))

test2 = jieba.cut(char_x2, cut_all=False)
print("精确模式: " + "| ".join(test2))

test3= jieba.cut_for_search(char_x2)
print("搜索引擎模式:" + "| ".join(test3))
