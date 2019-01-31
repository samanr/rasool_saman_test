import sys
"""This method compares weather two version strings are greater less or equal to each other
params ver1 : version string 1
params ver2 : version string 2
"""
def compareVersion(ver1,ver2):
    verArray1 = ver1.split(".")
    verArray2 = ver2.split(".")
    # internal function checks and raises a red flag when version is not in correct format
    def checkVersionFormat(versionArray):
        for each in versionArray:
            if each.isalpha():
                print('The version format cannot contain alphabet, should be of type ''d.d''')
                sys.exit()

    checkVersionFormat(verArray1)
    checkVersionFormat(verArray2)

    index = 0
    # internal function compare length of the versions
    def compareLength():
        return len(verArray1) if len(verArray1) > len(verArray2) else  len(verArray2)
    longerVersion = compareLength()

    while index < longerVersion:
        try:
            if int(verArray2[index]) > int(verArray1[index]):
                return ver2 + " is greater"
            elif int(verArray1[index]) > int(verArray2[index]):
                return ver1 + " is greater"
            elif int(verArray1[index]) == int(verArray2[index]):
                index += 1
        except:
            return ver1 + " is greater" if len(verArray1) > len(verArray2) else  ver2 + " is greater"
    #     checks if both versions are equal.
    if (index == longerVersion):
        return "both are equal"


print(compareVersion('1.2.3', '1.2.7'))