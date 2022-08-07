import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from collections import Counter
from matplotlib.font_manager import FontProperties
file=open('C:/Python/2021政府工作报告.txt','r',encoding='gbk')
file_words=file.read()
file.close()
stopfile=open('C:/Python/chineseStopWords.txt','r',encoding='gbk')
stop_words=stopfile.read()
stopfile.close()
cut_words=jieba.lcut(file_words,cut_all=True)
words={}
for word in cut_words:
    if word not in stop_words:
        if word not in words:
            words[word]=1
        else:
            words[word]=words[word]+1
    else:
        pass
#print(words['发展'])
word_count = Counter(words)
print(word_count)
background = Image.open("C:/Python/地图.jpg")
graph = np.array(background)
wordcloud=WordCloud(font_path='‪C:/Windows/Fonts/simsun.ttc',
                    mask=graph,
                    background_color='white',
                    max_font_size=150,
                    random_state=30)
ciyuntu=wordcloud.fit_words(words)
plt.imshow(ciyuntu)
plt.axis('off')
#plt.show()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
font=FontProperties('SimHei',size=11)
x = [x[0] for x in word_count.most_common(10)]
y = [x[1] for x in word_count.most_common(10)]
fig = plt.figure()
plt.grid(False)
# c = np.random.randint(0,1,len(y))
plt.bar(x, y, color='lightskyblue')
#显示每个标签值
for x,y in enumerate(y[0:]):
    plt.text(x,y-8,'%s' %y,ha='center')
plt.xlabel('关键词',FontProperties=font)
plt.ylabel('出现频次',FontProperties=font)
plt.title('2021政府工作报告柱状图',FontProperties=font)
plt.show()
