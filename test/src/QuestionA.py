"""This method checks weather two lines are overlaping or not.
params line1 : array of coordinates of line 1, the array size should not be more than 2
params line2 : array of coordinates of line 2, the array size should not be more than 2
"""
def isOverlap(line1, line2):
    return 'Overlap' if line1[1] >= line2[0] and line2[1] >= line1[0] else 'Not Overlap'

print(isOverlap([2,3],[3,5]))