#coding=gbk
import matplotlib.pyplot as plt
import numpy as np
import jieba
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image

with open(r"C:\Users\john\Desktop\jay.txt","r",encoding="utf-8") as f:
    text=f.read()
cut_text=jieba.cut(text)
result=" ".join(cut_text)
image=np.array(Image.open(r"C:\Users\john\Desktop\jay.jpg"))

wc=WordCloud(font_path=r"C:\Windows\Fonts\STZHONGS.TTF",
             background_color="white",
             width=500,
             height=350,
             max_font_size=50,
             min_font_size=10,
             mask=image
             )
wc.generate(result)
image_colors=ImageColorGenerator(image)
plt.show(wc.recolor(color_func=image_colors))
plt.imshow(wc)
plt.axis("off")
plt.show()


wc.to_file(r"C:\Users\john\Desktop\jay1.png")


