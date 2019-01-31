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
from PIL import Image
import pprint
import sys
import os
import numpy as np
import math
from random import randint
from RavensObject import RavensObject

MATRIX_SIZE = {
    "small":"2x2",
    "large":"3x3"
}

FIGURE_SIZE = {


}

match_scores = {}

problem_figs = {}
choices = {}

def compareAttributes(attrs1, attrs2):

    if attrs1 == attrs2:
        return 100

    return 0


def calculateScore(obj1, obj2):
    global match_scores
    match_scores = {}

    for object1 in obj1:
        match_scores[object1] = {}
        for object2 in obj2:
            match_scores = compareAttributes(obj1[object1].attributes, obj2[object2].attributes)
    print("SCORE TABLE = ")
    pprint.pprint(match_scores)
    return match_scores



def calculateMSE(fig1, fig2):
    fig1Array = np.array(fig1)
    fig2Array = np.array(fig2)
    mse = np.sum((fig1Array.astype('float') - fig2Array.astype('float')) ** 2)
    mse /= float(fig1Array.shape[0] * fig1Array.shape[1])
    return mse


def solve2x2(problem):

    problemInfo = problem.figures

    # compare A and B, apply to C
    if calculateMSE(problem_figs['A'][1], problem_figs['B'][1]) < 2000:
        for num, (option, image) in choices.items():
            if calculateMSE(problem_figs['C'][1], image) < 2000:
                print("Comparing Horizontal...")

                return int(num)

    # compare A and C, apply to B
    if calculateMSE(problem_figs['A'][1], problem_figs['C'][1]) < 2000:
        for num, (option, image) in choices.items():
            if calculateMSE(problem_figs['B'][1], image) < 2000:
                print("Comparing Vertical...")
                return int(num)

    print("Choosing Random...")

    return -1

def solve3x3():
    return -1

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        self.figures = {}
        self.choices = {}
        self.here = sys.path[0]





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
        hor_vert_score = []
        transform_hor = None
        transform_vert = None
        transform_order = 0
        print("=======================================")
        print("Solving " + problem.name)
        for name, figure in problem.figures.items():
            image = Image.open(figure.visualFilename)
            if name.isdigit():
                choices[name] = (figure, image)
            else:
                problem_figs[name] = (figure, image)


        if(problem.problemType == MATRIX_SIZE["small"]):
            answer = solve2x2(problem)
        elif problem.problemType == MATRIX_SIZE["large"]:
            answer = solve3x3()


        answer = answer if answer != -1 else randint(1,7)
        print('My Answer: ' + str(answer))

        return answer