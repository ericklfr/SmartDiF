import shutil
import os
import glob

src_dir = "/home/erick/nome_da_técnica/webservice/tifs2016/data-base/IIC/"
dst_dir = "/home/erick/nome_da_técnica/webservice/static/IIC/"

for pngfile in glob.iglob(os.path.join(src_dir, "*.png")):
    shutil.copy(jpgfile, dst_dir)




