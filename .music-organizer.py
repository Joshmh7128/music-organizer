import os;
from tinytag import TinyTag;
import shutil;
# organizes music by artist -> album -> track, from the directory it is placed in
# our directory
listdir = os.listdir()
srel = '//DESKTOP-QKU72AM/Media Server/Music/'
lrel = 'D:/Media Server/Music/'
rel = lrel # directory to work with
print(rel)

def organize():
    for d in listdir:
        if validType(d):
                tag = TinyTag.get(d)

                # album strange character handling
                taralb = tag.album

                if taralb != None and ':' in taralb:
                    taralb = taralb.replace(':','-')
                
                if taralb != None and '&' in taralb:
                    taralb = taralb.replace('&','and')

                if taralb != None and '/' in taralb:
                    taralb = taralb.replace('/','-')

                if taralb != None and '”' in taralb:
                    taralb = taralb.replace('”',' ')

                if taralb != None and '“' in taralb:
                    taralb = taralb.replace('“',' ')

                if taralb != None and '"' in taralb:
                    taralb = taralb.replace('"',' ')

                # artist strange character handling
                tarart = tag.artist

                if tarart != None and':' in tarart:
                    tarart = tarart.replace(':','-')
                    
                if tarart != None and'/' in tarart:
                    tarart = tarart.replace('/','-')
                
                if tarart != None and';' in tarart:
                    tarart = tarart.replace(';','-')

                if tarart != None and '&' in tarart:
                    tarart = tarart.replace('&','and')

                if tarart != None and'*' in tarart:
                    tarart = tarart.replace('*','-')

                if (tarart == None):
                    tarart = ''

                if (taralb == None):
                    taralb = ''

                print(taralb + " | " + tarart)

                tarpath = rel + tarart + "/" + taralb + "/"

                if os.path.exists(tarpath) == False:
                    print("making new directory: " + tarpath)
                    # check the path to the arist
                    if (os.path.exists(rel + tarart) == False):
                        os.mkdir(rel + tarart)
                    os.mkdir(tarpath)
                shutil.move(rel + d, tarpath)

# opens a directory and scans files
def openDir(d):
    print("Scanning: " + d)
    if (os.path.isdir(d)):
        for x in os.listdir(d):
            openDir(d + "/" + x)
            checkFile(d)
    else:
        checkFile(d)

def validType(d):
    return TinyTag.is_supported(d)


lqsongs = []

def checkFile(d):
    if (os.path.isfile(d) & validType(d)):
        tag = TinyTag.get(d)
        if (tag.bitrate == None): 
            return
        if (tag.bitrate < 200): 
            ar = tag.artist or "NONE"
            al = tag.album or "NONE"
            ti = tag.title or "NON"
            lqsongs.append(ar +  " | " + al + " | " + ti + " | " + str(int(tag.bitrate)))
            return

def makeReport():
    # checks songs for low quality
    for x in listdir:
        # do we have a directory?
        if os.path.isdir(x):
            openDir(rel + x)

    f = open(rel + "report.txt", "w")
    f.write("")
    f.close()

    f = open(rel + "report.txt", "a")
    f.write("~~~~~~~~ Low Quality Song Report: ~~~~~~~~" + "\n")
    for x in lqsongs:
        z = str(x.encode('utf-8'))
        f.write(z + "\n")
    f.close()

        
# run here
organize()
# makeReport()
