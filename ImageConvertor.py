#python program to convert png file to jpg
import os
import sys
#Python Imaging Library (PIL)
# all about PIL here.. https://wp.stolaf.edu/it/installing-pil-pillow-cimage-on-windows-and-mac/
#pip install pillow
from PIL import Image
if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        im = Image.open(sys.argv[1])
        target_name = sys.argv[1] + ".jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print("Saved as " + target_name)
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: convert2jpg.py <file>")