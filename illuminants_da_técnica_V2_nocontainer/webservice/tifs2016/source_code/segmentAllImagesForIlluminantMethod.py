import os
from subprocess import *

max_intensity=0.98823529411764705882
min_intensity=.05882352941176470588


def segmentAllImagesForIlluminantMethod(database, segmentedDBOutput, sigma,k,min_size, maxintensity, minintensity):
    
    command = "rm tifs2016/data-base/segmented/*.png"
    call(command, shell=True)

    im = os.listdir("tifs2016/data-base/" + str(database) + "/")
    for i in im:
        try:
            tt = i.split(".")
            newname = i
            if (tt[1] != "png"):
                cmd = "convert tifs2016/data-base/" + str(database) + "/" + i + " tifs2016/data-base/" + str(database) + "/" + tt[0] + ".png"
                os.system(cmd)
                newname = tt[0] + ".png"
            print(newname)
            #command = "../illuminants/build/bin/./vole felzenszwalb -I ../data-base/" + str(database) + "/" + newname + " --deterministic_coloring -O ../data-base/" + str(segmentedDBOutput)+ "/" + newname + " --sigma " + str(sigma) + " --k " + str(k) + " --min_size " + str(min_size) + " --max_intensity " + str(maxintensity) + " --min_intensity " + str(minintensity)
            command = "tifs2016/illuminants/build/./vole felzenszwalb -I tifs2016/data-base/" + str(database) + "/" + newname + " --deterministic_coloring -O tifs2016/data-base/" + str(segmentedDBOutput)+ "/" + newname + " --sigma " + str(sigma) + " --k " + str(k) + " --min_size " + str(min_size) + " --max_intensity " + str(maxintensity) + " --min_intensity " + str(minintensity)
            print(command)
            call(command, shell=True)
        except:
            print("Erro ao processar imagem \n")





segmentAllImagesForIlluminantMethod("images","segmented",0.2,300,15,max_intensity,min_intensity)
