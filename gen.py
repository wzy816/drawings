import os
import glob
import random

# regenerate README.md file for all subfolders and root folder
# python3 gen.py

imgs = []
for file in os.listdir("./"):
    if os.path.isdir(os.path.join("./", file)):
        folder_name = os.path.basename(file)
        with open("./"+file+"/README.md", "w+") as f:
            f.write("# "+folder_name + "\n\n")
            for img in glob.glob("./"+file+"/*"):
                bn = os.path.basename(img)
                f.write("!["+os.path.splitext(bn)[0]+"](<"
                        + bn+">)"+"\n")
                imgs.append(img)
            f.close()
random.shuffle(imgs)

with open("./README.md", "w+") as f:
    f.write("# drawings\n\n")
    f.write("architecture image collection\n\n")
    for i in range(4):
        bn = os.path.basename(imgs[i])
        f.write("!["+os.path.splitext(bn)[0]+"](<"
                + imgs[i]+">)"+"\n")
    f.close()
