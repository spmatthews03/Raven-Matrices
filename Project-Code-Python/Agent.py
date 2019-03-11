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

## =================================================================
## =================================================================

PERCENT_THRESHOLD = 0.01
INCREASE_THRESHOLD = 0.07

MATRIX_SIZE = {
    "small":"2x2",
    "large":"3x3"
}



A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'

size = "size"
shape = 'shape'
fill = 'fill'
angle = 'angle'
vertical_flip = 'vertical-flip'

match_scores = {}
## =================================================================
## =================================================================


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





def solve3x3(problem):
    possible_answers = {}
    possible_answers = []

    figures = ['A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H']
    options = ['1', '2', '3', '4',
               '5', '6', '7', '8']

    figuresImages = {}
    answerImages = {}
    figureImagesStats = {}
    answerImagesStats = {}
    figureImagesLogic = {}
    answerImagesLogic = {}

    figuresImages, answerImages, figureImagesStats, \
    answerImagesStats, figureImagesLogic, answerImagesLogic = populateDictionaries(figures, options, problem)

    rowOneDarkPixels = rowOrColumnAddition([figureImagesStats['A'], figureImagesStats['B'], figureImagesStats['C']])
    rowTwoDarkPixels = rowOrColumnAddition([figureImagesStats['D'], figureImagesStats['E'], figureImagesStats['F']])

    columnOneDarkPixels = rowOrColumnAddition([figureImagesStats['A'], figureImagesStats['D'], figureImagesStats['G']])
    columnTwoDarkPixels = rowOrColumnAddition([figureImagesStats['B'], figureImagesStats['E'], figureImagesStats['H']])

    columnsAreSame = False
    rowsAreSame = False

    if(checkIfDarkPixelsEqual(figureImagesStats[B], figureImagesStats[C], figureImagesStats[E], figureImagesStats[F])):
        print('Columns Are the same!')
        columnsAreSame = True
    if(checkIfDarkPixelsEqual(figureImagesStats[D], figureImagesStats[G], figureImagesStats[E], figureImagesStats[H])):
        print('Rows Are the same!')
        rowsAreSame = True

    # horizontal percentages
    abc_percent = calculateIfPixelPercentageEqual(figureImagesStats[A], figureImagesStats[B], figureImagesStats[C])
    def_percent = calculateIfPixelPercentageEqual(figureImagesStats[D], figureImagesStats[E], figureImagesStats[F])

    # vertical percentages
    adg_percent = calculateIfPixelPercentageEqual(figureImagesStats[A], figureImagesStats[D], figureImagesStats[G])
    beh_percent = calculateIfPixelPercentageEqual(figureImagesStats[B], figureImagesStats[E], figureImagesStats[H])



    for option in options:
        # print('Analyzing Option: ' + str(option))

        image = answerImagesLogic[option]


        optionsColumnsAreSame = False
        optionsRowsAreSame = False

        rowThreeDarkPixels = rowOrColumnAddition([figureImagesStats[G], figureImagesStats[H], answerImagesStats[option]])
        columnThreeDarkPixels = rowOrColumnAddition([figureImagesStats[C], figureImagesStats[F], answerImagesStats[option]])

        if(checkIfDarkPixelsEqual(figureImagesStats[E], figureImagesStats[F], figureImagesStats[H], answerImagesStats[option])):
            return option
        if(checkIfDarkPixelsEqual(figureImagesStats[E], figureImagesStats[H], figureImagesStats[F], answerImagesStats[option])):
            return option

        gh_option_percent = calculateIfPixelPercentageEqual(figureImagesStats[G], figureImagesStats[H], answerImagesStats[option])

        # horizontal comparisons
        if gh_option_percent < abc_percent + INCREASE_THRESHOLD and gh_option_percent > abc_percent - INCREASE_THRESHOLD:
            possible_answers.append(option)
        if gh_option_percent < def_percent + INCREASE_THRESHOLD and gh_option_percent > def_percent - INCREASE_THRESHOLD:
            possible_answers.append(option)

        # vertical comparisons
        if gh_option_percent < adg_percent + INCREASE_THRESHOLD and gh_option_percent > adg_percent - INCREASE_THRESHOLD:
            possible_answers.append(option)
        if gh_option_percent < beh_percent + INCREASE_THRESHOLD and gh_option_percent > beh_percent - INCREASE_THRESHOLD:
            possible_answers.append(option)

    print(possible_answers)

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
            answer = solve3x3(problem)

        answer = answer if answer != -1 and answer != None else random.randint(1,6)
        print('My Answer: ' + str(answer))

        return int(answer)