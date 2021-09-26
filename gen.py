import os
import glob

# regenerate README.md file for all subfolder
# python3 gen.py
for file in os.listdir("./"):
    if os.path.isdir(os.path.join("./", file)):
        folder_name = os.path.basename(file)
        with open("./"+file+"/README.md", "w+") as f:
            f.write("# "+folder_name + "\n\n")
            for img in glob.glob("./"+file+"/*"):
                f.write("![](./"+os.path.basename(img)+")"+"\n")
