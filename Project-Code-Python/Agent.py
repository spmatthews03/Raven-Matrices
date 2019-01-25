# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.

# Install Pillow and uncomment this line to access image processing.
#from PIL import Image
#import numpy
import copy


from RavensObject import RavensObject

SIZE = {
    "small":"2x2",
    "large":"3x3"
}

def compareFigs(fig1, fig2):
    objects1 = copy.copy(fig1.objects)
    objects2 = copy.copy(fig2.objects)

    if len(objects1) > len(objects2):
        for x in range(0, len(objects1) - len(objects2)):
            name = "_" + str(x)
            objects2[name] = RavensObject(name)
    elif len(objects2) > len(objects1):
        for x in range(0, len(objects2) - len(objects1)):
            name = "_" + str(x)
            objects1[name] = RavensObject(name)

    calculateScore(objects1, objects2)



def calculateScore(obj1, obj2):
    num = {}

    for object1 in obj1:
        num[object1] = {}
        for object2 in obj2:
            num[object1][object2] = compareObjects(obj1[object1].attributes, obj2[object2].attributes)



# def compareObjs(obj1, obj2):




class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass




    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        # print "========================="+problem.name+"=========================="

        problemInfo = problem.figures

        if(problem.problemType == SIZE["small"]):

            print("Comparing Horizontal...")
            horizontal = compareFigs(problemInfo["A"], problemInfo["B"])

            print("Comparing Vertical...")
            for key, value in sorted(problemInfo.iteritems()):
                fig = problemInfo[key]
                objects = fig.objects



        # print('Guess for ' + str(problem.name))
        # print('My Answer: ' + str(guess))
        # print('Actual Answer: ' + str(answer))

        # print()
        return -1