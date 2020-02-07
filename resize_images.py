import os
from PIL import Image
import glob
from tqdm import tqdm

def resize(dir_name):
    file_names = glob.glob("data/"+dir_name+"/*.png")
    for i, file_name in tqdm(enumerate(file_names)):
        title, ext = os.path.splitext(file_name)
        img = Image.open(file_name)
        img_resize = img.resize((256, 256))
        img_resize.save(title+'.png')
        #img_resize.save(title+'.jpg', quality=95)
        #os.remove(file_name)

for i in range(22,30):
    resize("{:05d}".format(i*1000))