gradeBmis = [
    [("19大数据1班", "王玉梅", 1.6, 50), ("19大数据1班", "张勇", 1.75, 57), ("19大数据1班", "王杰", 1.56, 68), ("19大数据1班", "胡平", 1.67, 87),
     ("19大数据1班", "陈康", 1.78, 73)],
    [("19大数据2班", "杨子", 1.73, 86), ("19大数据2班", "常博", 1.56, 70), ("19大数据2班", "张宇", 1.75, 73), ("19大数据2班", "唐梦", 1.85, 76),
     ("19大数据2班", "王硕", 1.8, 73)]]
# 遍历年级里面的班级信息
for classes in gradeBmis:
    # 获取到班级信息后,遍历班级的学生信息
    print("\n------------班级分割线------------")
    for person in classes:
        className, name, height, weight = person[0], person[1], person[2], person[3]
        bmi = weight / pow(height, 2)
        who, nat = "", ""
        if bmi < 18.5:
            who, nat = "偏瘦", "偏瘦"
        elif 18.5 <= bmi < 24:
            who, nat = "正常", "正常"
        elif 24 <= bmi < 25:
            who, nat = "正常", "偏胖"
        elif 25 <= bmi < 28:
            who, nat = "偏胖", "偏胖"
        elif 28 <= bmi < 30:
            who, nat = "偏胖", "肥胖"
        else:
            who, nat = "肥胖", "肥胖"
        print("{0}{1}的BMI数值为{2},BMI指标为:国际'{3}',国内'{4}'".format(className, name, format(bmi, '.2f'), who, nat))
