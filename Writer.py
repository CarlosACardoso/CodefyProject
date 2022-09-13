#Register the Codefy or Decofy

print('Writer used')


def WriteResults(TextC, FileW):
    #print(TextC)
    file = open(FileW + ".txt", "w")
    for i in TextC:
        file.write(str(i))
    file.close()


    return

