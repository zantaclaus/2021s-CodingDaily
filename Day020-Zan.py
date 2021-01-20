def convertCharactor(string):
    convertString = ""
    for item in string:
        if(item.islower()):
            convertString += item.upper()
        else:
            convertString += item.lower()
    return convertString

# print(convertCharactor("ConvertCHARACTOR"))