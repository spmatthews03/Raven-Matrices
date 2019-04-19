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
from Solvers import *

import sys
import itertools
import random
import random
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image

## =================================================================
## =================================================================

# PERCENT_THRESHOLD =
INCREASE_THRESHOLD = 15

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

def solve_D_3_x_3(problem):
    answer = solver.reflection_solver(problem)
    if answer == -1:
        answer = solver.offset_solve(problem, 0)
        if answer == -1:
            answer = solver.scaling_solver(problem)
            if answer == -1:
                answer = solver.roller_solver(problem)
                if answer == -1:
                    answer = solver.extract_inner_solver(problem)
                    if answer == -1:
                        answer = solver.rolling_transformation_solver(problem)
                        if answer == -1:
                            answer = solver.another_diff_solver(problem)
                            if answer == -1:
                                answer = solver.roll_extract_solver(problem)
                                if answer == -1:
                                    answer = solver.diagonal_solver(problem)
                                    if answer == -1:
                                        answer = solver.object_fill_solver(problem)
                                        if answer == -1:
                                            answer = solver.not_quite_random_solver(problem)
                                            if answer == -1:
                                                answer = solver.percent_increase_solver()
    return answer


def solve_E_3_x_3(problem):
    answer = solver.reflection_solver(problem)
    if answer == -1:
        answer = solver.offset_solve(problem, 0)
        if answer == -1:
            answer = solver.roller_solver(problem)
            if answer == -1:
                answer = solver.and_solver(problem)
                if answer == -1:
                    answer = solver.or_solver(problem)
                    if answer == -1:
                        answer = solver.xor_solver(problem)
                        if answer == -1:
                            answer = solver.diff_union_solver(problem)
                            if answer == -1:
                                answer = solver.shift_solver(problem)
                                if answer == -1:
                                    answer = solver.diff_solver(problem)
                                    if answer == -1:
                                        answer = solver.intersection_solver(problem)
                                        if answer == -1:
                                            answer = solver.reverse_solver(problem)
                                            if answer == -1:
                                                answer = solver.crop_solver(problem)
    return answer

def solve2x2(problem):
    global options
    helper = AgentP1()
    figures = ['A', 'B', 'C']
    options = ['1', '2', '3', '4', '5', '6']
    global problem_figures
    problem_figures = problem.figures

    return helper.solve2x2(problem)


def solve3x3(problem):
    answer = -1
    if 'C-' in problem.name:
        answer = solver.reflection_solver(problem)
        if answer == -1:
            answer = solver.pixel_solver(problem)
            if answer == -1:
                answer = solver.percent_increase_solver()
    elif 'D-' in problem.name:
        answer = solve_D_3_x_3(problem)
    elif 'E-' in problem.name:
        answer = solve_E_3_x_3(problem)

    return answer


class Agent:

    def __init__(self):
        self.figures = {}
        self.here = sys.path[0]

    def Solve(self, problem):
        print("=======================================")
        print("Solving " + problem.name)
        global solver
        solver = Solvers(problem)

        if problem.problemType == MATRIX_SIZE["small"]:
            answer = solve2x2(problem)
        elif problem.problemType == MATRIX_SIZE["large"]:
            answer = solve3x3(problem)

        answer = answer if answer != -1 and answer != None else random.randint(1,6)
        print('My Answer: ' + str(answer))

        return int(answer)