
#------------------------------------------------------------------------------
# 1.1 write code to calculate the volume of a cube
#------------------------------------------------------------------------------

# volume for a cube is V = a^3 where a is the edge length
# As you're asking for the volume of a cube and not a rectangular prism
# I am assuming this is what you're asking for

def cubeVolume(edgeLength):
    if isinstance(edgeLength, (int, float)) == False:
        return "Error: Invalid edge length provided."

    return abs(edgeLength) ** 3


#------------------------------------------------------------------------------
# 2.1 Write code to calculate the average of elements in a list
#------------------------------------------------------------------------------

# average of elements in list = sum of all elements / number of elements

def listAverage(myList):
    if isinstance(myList, list) == False or len(myList) == 0:
        return "Error: Invalid list provided."

    listSum = 0
    for x in myList:
        listSum += x

    else:
        return listSum / len(myList)

#------------------------------------------------------------------------------
# 3.1 Write code that generates a full name when you provide the first and
# last name as inputs
#------------------------------------------------------------------------------

def fullName(firstName, lastName):
    if firstName == None or isinstance(firstName, str) == False:
        return "Error: Invalid first name provided"

    if lastName == None or isinstance(lastName, str) == False:
        return "Error: Invalid last name provided"

    return firstName + " " + lastName
