import os
from subprocess import *

# Extract GrayWorldMaps from all images
# IN: 		scale -- image scale folder
#		sigma -- gray-world parameters
#	            n -- gray-world parameters
#	     	    p -- gray-world parameters
# OUT: gray-world maps

def extractNewGrayWorldMaps(sourcefolder, segmentedfolder, outputfolder, sigma,n,p):
    
    command = "rm tifs2016/data-base/GGE/*.png"
    call(command, shell=True)
        
    im = os.listdir("tifs2016/data-base/" + segmentedfolder + "/")
    for i in im:
        try:
            command = "tifs2016/illuminants/build/bin/./vole lgrayworld --img.image tifs2016/data-base/" + str(sourcefolder) + "/" + i + " -S tifs2016/data-base/" + str(segmentedfolder) + "/" + i + " -O "+ "tifs2016/data-base/" + str(outputfolder) + "/" + i[:-4] + "_fhs.png --n " +  str(n) + " --p " + str(p) + " --sigma " + str(sigma)
            call(command, shell=True)
            return "Sucess"
        except:
            return "Error"

extractNewGrayWorldMaps("images","segmented","GGE",1,1,3)
