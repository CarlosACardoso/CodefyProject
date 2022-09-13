#We have two lists. The first is to represent the text file to Codefy or Decodefy.
#The second is inside this first list and represent the text of each line.

print('Reader used')

#I'll make a routine for read the text of a file

#Routine for read a file
def ReadT(FileR):
    file = open(FileR + ".txt", "r")
    TextLine = file.read()
    file.close()
    return(TextLine)

#Subroutine for slice a line of text
def SliceText(TextR):
    TextLine = ReadT(TextR)
    result = []
    for i in TextLine:
        result.append(i)
    return result
