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

match_scores = {}

problem_figs = {}
choices = {}

def compareAttributes(attrs1, attrs2):

    if attrs1 == attrs2:
        return 100

    return 0


def compareShape(shape1, shape2):
    im = [None, None]
    for i, f in enumerate([shape1,shape2]):
        im[i] = (np.array(f
                          .convert('L')
                          .resize((32,32),resample=Image.BICUBIC))
                 ).astype(np.int)
    return np.abs(im[0] - im[1]).sum()




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


def createFrames(fig1, fig2):

    fig2_relationship = {}

    for fig1_obj, fig2_obj in zip(fig1.objects,fig2.objects):
        # fig2_relationship[fig2_obj] = []
        obj1 = fig1.objects[fig1_obj]
        obj2 = fig2.objects[fig2_obj]
        fig1_atts = {}
        fig2_atts = {}
        for fig1_att, fig2_att in zip(obj1.attributes,obj2.attributes):
            fig1_atts[fig1_att] = obj1.attributes[fig1_att]
            fig2_atts[fig2_att] = obj2.attributes[fig2_att]


        try:
            if fig1_atts[size] == fig2_atts[size]:
                fig2_relationship["SameSize"] = []
                fig2_relationship["SameSize"].append(True)
            else:
                fig2_relationship["SameSize"] = []
                fig2_relationship["SameSize"].append(False)
        except KeyError:
            pass


        try:
            if fig1_atts[shape] == fig2_atts[shape]:
                fig2_relationship["SameShape"] = []
                fig2_relationship["SameShape"].append(True)
            else:
                fig2_relationship["SameShape"] = []
                fig2_relationship["SameShape"].append(False)
        except KeyError:
            pass

        try:
            if fig1_atts[fill] == fig2_atts[fill]:
                fig2_relationship["SameFill"] = []
                fig2_relationship["SameFill"].append(True)
            else:
                fig2_relationship["SameFill"] = []
                fig2_relationship["SameFill"].append(False)
        except KeyError:
            pass

        try:
            if fig1_atts[angle] == fig2_atts[angle]:
                fig2_relationship["SameAngle"] = []
                fig2_relationship["SameAngle"].append(True)
            else:
                fig2_relationship["SameAngle"] = []
                fig2_relationship["SameAngle"].append(False)
        except KeyError:
            pass

    return fig2_relationship


def compareFrames(frame1, frame2):
    score = 0

    for frame1_item, frame2_item in zip(frame1, frame2):
        if frame1_item == frame2_item and frame1[frame1_item] == frame2[frame2_item]:
            score += 1

    return score



def solve2x2(problem):

    # res = compareShape(problem_figs['A'][1], problem_figs['B'][1])

    # horizontal and vertical comparisons
    A_B_rel = createFrames(problem.figures[A], problem.figures[B])
    A_C_rel = createFrames(problem.figures[A], problem.figures[C])

    # create a list of relationships between C and choices
    C_i_relationship = {}
    for i in range(1,7):
        C_i_relationship[i] = []
        C_i_relationship[i] = createFrames(problem.figures[C], problem.figures[str(i)])

    # create a list of relationshipt between B and choices
    B_i_relationship = {}
    for i in range(1,7):
        B_i_relationship[i] = []
        B_i_relationship[i] = createFrames(problem.figures[B], problem.figures[str(i)])

    # compare lists A -> B ( horizontal )
    answer_scores_hor = {}
    for answer in C_i_relationship:
        answer_scores_hor[answer] = []
        answer_scores_hor[answer] = compareFrames(A_B_rel, C_i_relationship[answer])

    # compare lists A -> C ( vertical )
    answer_scores_ver = {}
    for answer in B_i_relationship:
        answer_scores_ver[answer] = []
        answer_scores_ver[answer] = compareFrames(A_C_rel, B_i_relationship[answer])


    possible_answers = {}
    possible_answers = set()
    max_hor = max(answer_scores_hor.values())
    max_ver = max(answer_scores_ver.values())

    if max_hor > max_ver or max_hor == max_ver:
        return answer_scores_hor.get(max(answer_scores_hor.values()))
    elif max_ver < max_hor:
        return answer_scores_ver.get(max(answer_scores_hor.values()))

    # possible_answers.add(max(answer_scores_hor))
    # answer_list





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



        answer = answer if answer != -1 and answer != None else randint(1,7)
        print('My Answer: ' + str(answer))

        return answer