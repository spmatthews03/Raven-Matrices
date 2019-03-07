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
# from .AgentHelper import *
from AgentHelper import *
import sys
import itertools
import random
import random
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image

MATRIX_SIZE = {
    "small":"2x2",
    "large":"3x3"
}

A = 'A'
B = 'B'
C = 'C'
size = "size"
shape = 'shape'
fill = 'fill'
angle = 'angle'
vertical_flip = 'vertical-flip'

match_scores = {}


def solve2x2(problem):
    figures = ['A', 'B', 'C']
    options = ['1', '2', '3', '4', '5', '6']

    figuresImages = {}
    answerImages = {}
    figureImagesStats = {}
    answerImagesStats = {}
    figureImagesLogic = {}
    answerImagesLogic = {}

    figuresImages, answerImages, figureImagesStats, \
    answerImagesStats, figureImagesLogic, answerImagesLogic = populateDictionaries(figures, options, problem)

    rowOnePixels = rowOrColumnAddition([figureImagesStats['A'], figureImagesStats['B']])
    columnOnePixels = rowOrColumnAddition([figureImagesStats['A'], figureImagesStats['C']])





def solve3x3():
    figures = ['A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H']
    options = ['1', '2', '3', '4',
               '5', '6', '7', '8']
    return -1

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        self.figures = {}
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
        print("=======================================")
        print("Solving " + problem.name)

        if(problem.problemType == MATRIX_SIZE["small"]):
            answer = solve2x2(problem)
        elif problem.problemType == MATRIX_SIZE["large"]:
            answer = solve3x3()

        answer = answer if answer != -1 and answer != None else random.randint(1,6)
        print('My Answer: ' + str(answer))

        return answer