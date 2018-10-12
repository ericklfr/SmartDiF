import sys
import os
from subprocess import *

config = "config.txt"

# Extract IlluminantMaps from all images
# IN: 		scale -- image scale folder
#		configFile -- illuminants config parameters file
# OUT: illuminant maps

def extractIlluminantMaps(sourcefolder, segmentedfolder, outputfolder):
    
    command = "rm tifs2016/data-base/IIC/*.png"
    call(command, shell=True)

    im = os.listdir("tifs2016/data-base/" + str(segmentedfolder) + "/")
    for i in im:
        try:
            command = "tifs2016/illuminants/build/bin/./vole liebv --img.image tifs2016/data-base/" + str(sourcefolder) + "/" + i + " -S tifs2016/data-base/" + str(segmentedfolder) + "/" + i + " -O tifs2016/data-base/" + str(outputfolder) + "/" + i[:-4] + "_fhs.png --iebv_config "+"tifs2016/illuminants/build/bin/" + config
            print("antes /n")
            call(command,shell=True)
            print(command)
            return "Sucess"
        except:
            return "Error"

extractIlluminantMaps("images","segmented","IIC")

