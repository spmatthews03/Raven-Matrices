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
from AgentP1 import *
import sys
import itertools
import random
import random
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image

## =================================================================
## =================================================================

# PERCENT_THRESHOLD =
INCREASE_THRESHOLD = 10

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
    helper = AgentP1()
    figures = ['A', 'B', 'C']
    options = ['1', '2', '3', '4', '5', '6']
    global problem_figures
    problem_figures = problem.figures

    return helper.solve2x2(problem)



def solve3x3(problem):
    helper = AgentHelper(problem)
    hor_possible_answers = {}
    hor_possible_answers = []
    ver_possible_answers = {}
    ver_possible_answers = []

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
    answerImagesStats, figureImagesLogic, answerImagesLogic = helper.populate_dictionaries(figures, options)

    rowOneDarkPixels = helper.rowOrColumnAddition([figureImagesStats['A'], figureImagesStats['B'], figureImagesStats['C']])
    rowTwoDarkPixels = helper.rowOrColumnAddition([figureImagesStats['D'], figureImagesStats['E'], figureImagesStats['F']])

    columnOneDarkPixels = helper.rowOrColumnAddition([figureImagesStats['A'], figureImagesStats['D'], figureImagesStats['G']])
    columnTwoDarkPixels = helper.rowOrColumnAddition([figureImagesStats['B'], figureImagesStats['E'], figureImagesStats['H']])

    columnsAreSame = False
    rowsAreSame = False

    if(helper.checkIfDarkPixelsEqual(figureImagesStats[B], figureImagesStats[C], figureImagesStats[E], figureImagesStats[F])):
        print('Columns Are the same!')
        columnsAreSame = True
    if(helper.checkIfDarkPixelsEqual(figureImagesStats[D], figureImagesStats[G], figureImagesStats[E], figureImagesStats[H])):
        print('Rows Are the same!')
        rowsAreSame = True

    # horizontal percentages
    ab_percent, bc_percent, ac_percent = helper.calculateIfPixelPercentageEqual(figureImagesStats[A], figureImagesStats[B], figureImagesStats[C])
    de_percent, ef_percent, df_percent = helper.calculateIfPixelPercentageEqual(figureImagesStats[D], figureImagesStats[E], figureImagesStats[F])

    # vertical percentages
    ad_percent, dg_percent, ag_percent = helper.calculateIfPixelPercentageEqual(figureImagesStats[A], figureImagesStats[D], figureImagesStats[G])
    be_percent, eh_percent, bh_percent = helper.calculateIfPixelPercentageEqual(figureImagesStats[B], figureImagesStats[E], figureImagesStats[H])


    if rowsAreSame:
        for option in options:
            if helper.checkIfDarkPixelsEqual_for2(figureImagesStats[H], answerImagesLogic[option]):
                return option

    a_b_c_percent = helper.check_percentage_change(ab_percent, bc_percent)
    d_e_f_percent = helper.check_percentage_change(de_percent, ef_percent)
    a_d_g_percent = helper.check_percentage_change(ad_percent, dg_percent)
    b_e_h_percent = helper.check_percentage_change(be_percent, eh_percent)

    for option in options:

        if helper.checkIfDarkPixelsEqual(figureImagesStats[E], figureImagesStats[F],
                                         figureImagesStats[H], answerImagesStats[option]):
            return option

        if helper.checkIfDarkPixelsEqual(figureImagesStats[E], figureImagesStats[H],
                                         figureImagesStats[F], answerImagesStats[option]):
            return option

        gh_percent, h_option_percent, g_option_percent = helper.calculateIfPixelPercentageEqual(figureImagesStats[G],
                                                                                                figureImagesStats[H],
                                                                                                answerImagesStats[option])

        g_h_option_percent = helper.check_percentage_change(gh_percent, h_option_percent)

        # horizontal comparisons
        if a_b_c_percent - INCREASE_THRESHOLD <= g_h_option_percent <= a_b_c_percent + INCREASE_THRESHOLD:
            hor_possible_answers.append(option)

        if d_e_f_percent - INCREASE_THRESHOLD <= g_h_option_percent <= d_e_f_percent + INCREASE_THRESHOLD:
            hor_possible_answers.append(option)

        # vertical comparisons
        if a_d_g_percent - INCREASE_THRESHOLD <= g_h_option_percent <= a_d_g_percent + INCREASE_THRESHOLD:
            ver_possible_answers.append(option)
        if b_e_h_percent - INCREASE_THRESHOLD <= g_h_option_percent <= b_e_h_percent + INCREASE_THRESHOLD:
            ver_possible_answers.append(option)

    print(hor_possible_answers)
    print(ver_possible_answers)


    possible_answers = set()

    for answer in hor_possible_answers:
        possible_answers.add(answer)
    # for answer in ver_possible_answers:
    #     possible_answers.add(answer)

    # print(possible_answers)

    rms_images = helper.get_rms(helper.convert_images())

    return helper.choose_answer(rms_images, possible_answers)


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

        if problem.problemType == MATRIX_SIZE["small"]:
            answer = solve2x2(problem)
        elif problem.problemType == MATRIX_SIZE["large"]:
            answer = solve3x3(problem)

        answer = answer if answer != -1 and answer != None else random.randint(1,6)
        print('My Answer: ' + str(answer))

        return int(answer)