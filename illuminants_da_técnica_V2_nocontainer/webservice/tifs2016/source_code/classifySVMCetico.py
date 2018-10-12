import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.grid_search import GridSearchCV
import json
def readTrainingTestFiles(outfile):
    ofid = open(outfile,'rt')
    ofid.seek(0)
    lines = ofid.readlines()
    ofid.close()
    features = []
    labels = []
    for i in lines:
        label = 0
        tmp = i[:-3].split(" ")
        row = []
        for j in tmp:
            if (label != 0):
                tmp2 = j.split(":")
                row.append(tmp2[1])
            else:
                label = j
                labels.append(j)
        features.append(row)
    return(features,labels)


def getSpaceChannelName(space,channel):
    nameSpace = ""
    nameChannel = ""
    if space == 0:
        nameSpace = "HSV"
        if channel == 0:
            nameChannel = "V"
        elif channel == 1:
            nameChannel = "S"
        elif channel == 2:
            nameChannel = "H"
        elif channel == 3:
            nameChannel = "full"
    elif space == 1:
        nameSpace = "RGB"
        if channel == 0:
            nameChannel = "B"
        elif channel == 1:
            nameChannel = "G"
        elif channel == 2:
            nameChannel = "R"
        elif channel == 3:
            nameChannel = "full"
    elif space == 2:
        nameSpace = "YCbCr"
        if channel == 0:
            nameChannel = "Cr"
        elif channel == 1:
            nameChannel = "Cb"
        elif channel == 2:
            nameChannel = "Y"
        elif channel == 3:
            nameChannel = "full"
    elif space == 4:
        nameSpace = "Lab"
        if channel == 0:
            nameChannel = "b"
        elif channel == 1:
            nameChannel = "a"
        elif channel == 2:
            nameChannel = "L"
        elif channel == 3:
            nameChannel = "full"

    return (nameSpace,nameChannel)


def svmTestBySample(imgName,descriptor,space,channel,illuminant="IIC"):
    nameSpace,nameChannel = getSpaceChannelName(space,channel)
    tt = descriptor.upper()
    outfile = "tifs2016/extracted-feature-vectors/" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + "/fv-" + imgName + ".txt"
    ft,lb = readTrainingTestFiles(outfile)
    testMatrixF = np.array(ft)
    testMatrixL = np.array(lb)

    #Scale Train Features
    #testMatrixFScaled = preprocessing.scale(testMatrixF)

    #Scale features between [-1,1]
    max_abs_scaler = preprocessing.MaxAbsScaler()
    testMatrixFScaled = max_abs_scaler.fit_transform(testMatrixF)

    npath = "tifs2016/models/" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + "/"
    modelName = npath + "model-DSO-" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + ".pkl"
    clf = joblib.load(modelName)
    outLabels = clf.predict(testMatrixFScaled)
    scores = clf.score(testMatrixFScaled,testMatrixL)
    return(outLabels,scores)
    #print(outLabels,scores)



def svmTestByImage(imgName,descriptor,space,channel,illuminant="IIC"):
    nameSpace,nameChannel = getSpaceChannelName(space,channel)
    tt = descriptor.upper()
    outfile = "tifs2016/extracted-feature-vectors/" + tt + "-" + illuminant + "-" + nameSpace + "-" + nameChannel + "/fv-" + imgName + ".txt"
    outLabels,scores = svmTestBySample(imgName,descriptor,space,channel,illuminant)
    labelsDefault,imageLables = readTrainingTestFiles(outfile)
    imageClass = 1
    for i in outLabels:
        if i == '-1':
            imageClass = -1
    return imageClass

def fullClassification(imgName, descritores):
    classifiersFake = []
    classifiersNormal = []
    resultados = {'acc': [], 'ccv': [], 'bic': [], 'lch': [], 'sasi': [], 'las': [],'unser': [], 'eoac': [],'spytec': []}
    listOfParams = []
    for descritor in descritores:
        if descritor == "ACC":
            listOfParams.extend([("acc",4,3,"IIC"), ("acc",1,3,"IIC"), ("acc",2,3,"IIC"), ("acc",4,3,"GGE"), ("acc",1,3,"GGE"), ("acc",2,3,"GGE")])
        if descritor == "CCV":
            listOfParams.extend([("ccv",4,3,"IIC"), ("ccv",1,3,"IIC"), ("ccv",2,3,"IIC"), ("ccv",4,3,"GGE"), ("ccv",1,3,"GGE"), ("ccv",2,3,"GGE")])
        if descritor == "BIC":
            listOfParams.extend([("bic",4,3,"IIC"), ("bic",1,3,"IIC"), ("bic",2,3,"IIC"), ("bic",4,3,"GGE"), ("bic",1,3,"GGE"), ("bic",2,3,"GGE")])
        if descritor == "LCH":
            listOfParams.extend([("lch",4,3,"IIC"), ("lch",1,3,"IIC"), ("lch",2,3,"IIC"), ("lch",4,3,"GGE"), ("lch",1,3,"GGE"), ("lch",2,3,"GGE")])
        if descritor == "SASI":
            listOfParams.extend([("sasi",4,2,"IIC"), ("sasi",0,0,"IIC"), ("sasi",2,2,"IIC"), ("sasi",4,2,"GGE"), ("sasi",0,0,"GGE"), ("sasi",2,2,"GGE")])
        if descritor == "LAS":
            listOfParams.extend([("las",4,2,"IIC"), ("las",0,0,"IIC"), ("las",2,2,"IIC"), ("las",4,2,"GGE"), ("las",0,0,"GGE"), ("las",2,2,"GGE")])
        if descritor == "UNSER":
            listOfParams.extend([("unser",4,2,"IIC"), ("unser",0,0,"IIC"), ("unser",2,2,"IIC"), ("unser",4,2,"GGE"), ("unser",0,0,"GGE"), ("unser",2,2,"GGE")])
        if descritor == "EOAC":
            listOfParams.extend([("eoac",4,2,"IIC"), ("eoac",0,0,"IIC"), ("eoac",2,2,"IIC"), ("eoac",4,2,"GGE"), ("eoac",0,0,"GGE"), ("eoac",2,2,"GGE")])
        if descritor == "SPYTEC":
            listOfParams.extend([("spytec",4,2,"IIC"), ("spytec",0,0,"IIC"), ("spytec",2,2,"IIC"), ("spytec",4,2,"GGE"), ("spytec",0,0,"GGE"), ("spytec",2,2,"GGE")])
    outClassification = []
    finalClass = "FAKE"
    votesNormal = 0
    votesFake = 0
    for i in listOfParams:
        desc,space,channel,illumi = i
        classPredic = svmTestByImage(imgName,desc,space,channel,illumi)
        if desc == "acc":
            resultados['acc'].append(classPredic)
        if desc == "ccv":
            resultados['ccv'].append(classPredic)
        if desc == "bic":
            resultados['bic'].append(classPredic)
        if desc == "lch":
            resultados['lch'].append(classPredic)
        if desc == "sasi":
            resultados['sasi'].append(classPredic)
        if desc == "las":
            resultados['las'].append(classPredic)
        if desc == "unser":
            resultados['unser'].append(classPredic)
        if desc == "eoac":
            resultados['eoac'].append(classPredic)
        if desc == "spytec":
            resultados['spytec'].append(classPredic)

        if (classPredic == 1):
            votesNormal += 1
        else:
            votesFake += 1
    if (votesNormal > votesFake):
        finalClass = "NORMAL"
    corNormal, corFake, bordaNormal, bordaFake, texturaNormal, texturaFake = (0,)*6
    accNormal,accFake,ccvNormal,ccvFake,bicNormal,bicFake,lchNormal,lchFake,sasiNormal,sasiFake = (0,)*10
    lasNormal, lasFake, unserNormal,unserFake, eoacNormal,eoacFake, spytecNormal, spytecFake = (0,)*8
    for resultado in resultados['acc']:
        if resultado == 1:
            accNormal += 1
            corNormal += 1
        else:
            accFake +=1
            corFake +=1
    for resultado in resultados['ccv']:
        if resultado == 1:
            ccvNormal += 1
            corNormal += 1
        else:
            ccvFake += 1
            corFake += 1
    for resultado in resultados['bic']:
        if resultado == 1:
            bicNormal += 1
            corNormal += 1
        else:
            bicFake += 1
            corFake += 1
    for resultado in resultados['lch']:
        if resultado == 1:
            lchNormal += 1
            corNormal += 1
        else:
            lchFake += 1
            corFake += 1
    for resultado in resultados['sasi']:
        if resultado == 1:
            sasiNormal += 1
            texturaNormal += 1
        else:
            accFake += 1
            texturaFake += 1
    for resultado in resultados['las']:
        if resultado == 1:
            lasNormal += 1
            texturaNormal += 1
        else:
            lasFake += 1
            texturaFake += 1
    for resultado in resultados['unser']:
        if resultado == 1:
            unserNormal += 1
            texturaNormal += 1
        else:
            unserFake += 1
            texturaFake += 1
    for resultado in resultados['eoac']:
        if resultado == 1:
            eoacNormal += 1
            bordaNormal += 1
        else:
            eoacFake += 1
            bordaFake += 1
    for resultado in resultados['spytec']:
        if resultado == 1:
            spytecNormal += 1
            bordaNormal += 1
        else:
            spytecFake += 1
            bordaFake += 1
    resultadoFinal = {'cor':{'normal':corNormal,'fake':corFake,'acc':{'normal':accNormal,'fake':accFake},'ccv':{'normal':ccvNormal,'fake':ccvFake},
                             'bic':{'normal':bicNormal,'fake':bicFake},'lch':{'normal':lchNormal,'fake':lchFake}},
                      'textura':{'normal':texturaNormal,'fake':texturaFake,'sasi':{'normal':sasiNormal,'fake':sasiFake},
                                 'las':{'normal':lasNormal,'fake':lasFake},'unser':{'normal':unserNormal,'fake':unserFake}},
                      'borda':{'normal':bordaNormal,'fake':bordaFake,'eoac':{'normal':eoacNormal,'fake':eoacFake},'spytec':{'normal':spytecNormal,'fake':spytecFake}},
                      'resultadoFinal':finalClass
                      }
    #return (outClassification,votesNormal,votesFake,finalClass)
    print(resultadoFinal)
    print("Votos Normal: %d\nVotos Fake: %d\nClassificacao Final: %s\n out: %s" %(votesNormal,votesFake,finalClass,outClassification))
    return resultadoFinal


