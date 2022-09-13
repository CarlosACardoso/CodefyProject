import Code

print('Codefy used')



#Codefy for single arguments
def SingleCodefy(argument):
    return Code.BCode[argument]



#Codefy for a argument list
def ListCodefy(argument):
    result = []

    for i in argument:
        r = SingleCodefy(i)
        result.append(r)

    return result
