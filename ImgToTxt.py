# coding:utf-8 #
from PIL import Image
import time

char_list=list('*&%$')
def img_to_text(r,g,b,a=256):
    if a==0:
        return " "
    gray = int(0.299 * r+0.587 * g+0.114 * b)
    index=257/len(char_list)
    return char_list[int(gray/index)]

if __name__=='__main__':
    time_start = time.time()
    for index in range(5496,5545):
        IMG="Img/png0"+str(index)+".png"
        im=Image.open(IMG)
        im=im.resize((160,90),Image.NEAREST)
        txt=""
        for i in range(90):
            for j in range(160):
                txt += img_to_text(*im.getpixel((j, i)))
            txt+='\n'
        with open("char/"+str(index)+'.txt','w') as f:
            f.write(txt)
            f.close()
    time_end=time.time()
    print ("共用时%s秒" %(time_end-time_start))
