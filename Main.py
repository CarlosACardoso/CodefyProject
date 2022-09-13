#Import Programs
import Codefy as Co
import Decodefy as De
import Writer as Wr
import Reader as Re
from Code import  lenghtC
global lenghtC

#Name of file to Read
FileR = 'ToCode'

#Name of file to Write
FileW = "Results"


#Codefy
def CodefyCode(TextLine):
    B = Co.ListCodefy(TextLine)
    return B

#Decodefy
def DecodefyCode(TextLine):
    B = De.ListDecodefy(TextLine)
    return B

#Reader
def ReaderFile(TextR):
    TextLine = Re.SliceText(TextR)
    return TextLine

#Writer
def WriterFile(TextC):
    Wr.WriteResults(TextC, FileW)
    return

#Agroup the Codefied Code
def Agroup5(TextLine):
    resultagroupi = []
    a = len(TextLine)/lenghtC
    u = 0
    for i in range(int(a)):
        u +=1
        j = u*lenghtC
        r = ""
        for k in reversed(range(lenghtC)):
            r = str(r) + str(TextLine[j-k-1])
        resultagroupi.append(r)
    return resultagroupi


#Codefy and Write Result
def CodefyResult():
    TextLine = ReaderFile(FileR)
    #print(TextLine)
    TextC = CodefyCode(TextLine)
    #print(TextC)
    WriterFile(TextC)
    print("Codefy was sucessful")


#Decodefy and Write Result
def DecodefyResult():
    TextLine = ReaderFile(FileR)
    #print(TextLine)
    TextLine = Agroup5(TextLine)
    TextC = DecodefyCode(TextLine)
    #print(TextC)
    WriterFile(TextC)
    print("Codefy was sucessful")

#Main Program
#DecodefyResult()
#CodefyResult()

exit()