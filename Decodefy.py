import Code

print('DeCodefy used')

#Decodefy for single arguments
def SingleDecodefy(argument):

    return Code.BCodeInvert[argument]

#Decodefy for a argument list
def ListDecodefy(argument):
    result = []
    argument = TransformInt(argument)
    for i in argument:
        r = SingleDecodefy(i)
        result.append(r)

    return result

#Transform arguments of list in Int
def TransformInt(argument):
    result = []
    for i in range(int(len(argument))):
        r = int(argument[i])
        result.append(r)

    return result