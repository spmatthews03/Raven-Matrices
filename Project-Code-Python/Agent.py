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
# from PIL import Image
import pprint
import sys
import itertools
import os
# import numpy as np
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
vertical_flip = 'vertical-flip'

match_scores = {}

problem_figs = {}
choices = {}

def createFrames(fig1, fig2, problem):

    a_objs = fig1.objects
    b_objs = fig2.objects

    # a_objs_list = [a_objs[obj] for obj in a_objs]
    # b_objs_list = [b_objs[obj] for obj in b_objs]
    # a_objs_list.sort(key=lambda x: a_objs_list[x])
    # b_objs_list.sort(key='name')
    a_names = []
    b_names = []
    a_objs_list = []
    b_objs_list = []
    for obj in a_objs:
        a_objs_list.append(a_objs[obj])
        a_names.append(obj)

    for obj in b_objs:
        b_objs_list.append(b_objs[obj])
        b_names.append(obj)


    while len(a_names) != len(b_names):
        if len(a_names) > len(b_names):
            b_names.append(None)
        if len(b_names) > len(a_names):
            a_names.append(None)

    # in the case of multiple objects in an image,
    # this will calulculate which object the previous
    # object should be mapped too
    b_perm = list(itertools.permutations(b_objs_list))

    for b_names in b_perm:
        relationship = {}

        for a_name, b_name in zip(a_objs_list,b_names):
            a_obj_atts = {}
            b_obj_atts = {}
            # relationship[a_obj] = {}
            # relationship[b_obj] = {}

            if a_name == None:
                relationship[b_name] = []
                relationship[b_name].append("Added")
            elif b_name == None:
                relationship[a_name] = []
                relationship[a_name].append("Deleted")
            else:
                relationship[b_name] = []

                # have to check before doing this
                # A may be added or deleted and vis versa for b
                for a_obj_att in a_name.attributes:
                    a_obj_atts[a_obj_att] = a_name.attributes[a_obj_att]


                for b_obj_att in b_name.attributes:
                    b_obj_atts[b_obj_att] = b_name.attributes[b_obj_att]




                try:
                    if a_obj_atts[size] == b_obj_atts[size]:
                        relationship[b_name].append("SameSize")
                    else:
                        relationship[b_name].append("DifferentSize")
                except KeyError:
                    pass


                try:
                    if a_obj_atts[shape] == b_obj_atts[shape]:
                        relationship[b_name].append("SameShape")
                    else:
                        relationship[b_name].append("DifferentShape")
                except KeyError:
                    pass

                try:
                    if a_obj_atts[fill] == b_obj_atts[fill]:
                        relationship[b_name].append("SameFill")
                    else:
                        relationship[b_name].append("DifferentFill")
                except KeyError:
                    pass


                # TODO: fix whatever is wrong with this
                try:
                    a_obj_atts[angle]
                except KeyError:
                    a_obj_atts[angle] = 0

                try:
                    b_obj_atts[angle]
                except KeyError:
                    b_obj_atts[angle] = 0

                try:
                    if a_obj_atts[angle] == b_obj_atts[angle]:
                        relationship[b_name].append("SameAngle")
                    else:
                        relationship[b_name].append("DifferentAngle")
                        relationship[b_name].append(abs(int(a_obj_atts[angle]) - int(b_obj_atts[angle])))
                except KeyError:
                    # relationship[b_obj]["SameAngle"]
                    pass

                try:
                    a_obj_atts[vertical_flip]
                except KeyError:
                    a_obj_atts[vertical_flip] = "no"

                try:
                    b_obj_atts[vertical_flip]
                except KeyError:
                    b_obj_atts[vertical_flip] = "no"

                if a_obj_atts[vertical_flip] == b_obj_atts[vertical_flip]:
                    relationship[b_name].append("VerticalFlip")
                else:
                    relationship[b_name].append("NotFlipped")

    return relationship


def compareFrames(frame1, frame2):
    score = 0

    for obj1 in frame1:
        for obj2 in frame2:
            for att1, att2 in zip(obj1.attributes, obj2.attributes):
                if obj1.attributes[att1] == obj2.attributes[att2]:
                    score += 1

    return score



def solve2x2(problem):

    # res = compareShape(problem_figs['A'][1], problem_figs['B'][1])

    # horizontal and vertical comparisons
    A_B_rel = createFrames(problem.figures[A], problem.figures[B], problem)
    A_C_rel = createFrames(problem.figures[A], problem.figures[C], problem)

    # create a list of relationships between C and choices
    C_i_relationship = {}
    for i in range(1,7):
        C_i_relationship[i] = []
        C_i_relationship[i] = createFrames(problem.figures[C], problem.figures[str(i)], problem)

    # create a list of relationships between B and choices
    B_i_relationship = {}
    for i in range(1,7):
        B_i_relationship[i] = []
        B_i_relationship[i] = createFrames(problem.figures[B], problem.figures[str(i)], problem)

    # compare lists A -> B ( horizontal )
    answer_scores_hor = {}
    for answer, rel in C_i_relationship.items():
        answer_scores_hor[answer] = 0
        for a_b, rels in zip(A_B_rel.values(),rel.values()):
            answer_scores_hor[answer] += len(set(a_b).intersection(rels))

    # compare lists A -> C ( vertical )
    answer_scores_ver = {}
    for answer, rel in B_i_relationship.items():
        answer_scores_ver[answer] = 0
        for a_c, rels in zip(A_B_rel.values(),rel.values()):
            answer_scores_ver[answer] += len(set(a_c).intersection(rels))

    possible_answers = []
    max_hor = max(answer_scores_hor.values())
    max_ver = max(answer_scores_ver.values())
    # possible_answers[max_hor]

    for name, value in answer_scores_hor.items():
        if value == max(iter(answer_scores_hor.values())):
            possible_answers.append(name)

    for name, value in answer_scores_ver.items():
        if value == max(iter(answer_scores_ver.values())):
            possible_answers.append(name)

    counts = {}
    for val in possible_answers:
        counts[val] = counts.get(val, 0) + 1

    print(counts)

    for val in counts:
        if counts[val] == 2:
            return val
        else:
            return val

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
        # for name, figure in problem.figures.items():
        #     image = Image.open(figure.visualFilename)
        #     if name.isdigit():
        #         choices[name] = (figure, image)
        #     else:
        #         problem_figs[name] = (figure, image)


        if(problem.problemType == MATRIX_SIZE["small"]):
            answer = solve2x2(problem)
        elif problem.problemType == MATRIX_SIZE["large"]:
            answer = solve3x3()



        answer = answer if answer != -1 and answer != None else randint(1,6)
        print('My Answer: ' + str(answer))

        return answer