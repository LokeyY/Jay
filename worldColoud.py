#coding=gbk
import matplotlib.pyplot as plt
import numpy as np
import jieba
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
#打开歌词并进行分词
with open(r"C:\Users\john\Desktop\jay.txt","r",encoding="utf-8") as f:
    text=f.read()
cut_text=jieba.cut(text)
result=" ".join(cut_text)
#选用背景图片
image=np.array(Image.open(r"C:\Users\john\Desktop\jay.jpg"))
#设置参数
wc=WordCloud(font_path=r"C:\Windows\Fonts\STZHONGS.TTF",
             background_color="white",
             width=500,
             height=350,
             max_font_size=50,
             min_font_size=10,
             mask=image
             )
wc.generate(result)
#设置背景颜色随图片颜色改变
image_colors=ImageColorGenerator(image)
plt.show(wc.recolor(color_func=image_colors))
#展示图片
plt.imshow(wc)
plt.axis("off")
plt.show()
#保存图片
wc.to_file(r"C:\Users\john\Desktop\jay1.png")


