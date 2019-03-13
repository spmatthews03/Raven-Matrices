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
import sys
import itertools
import random

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


class AgentP1:

    def __init__(self):
        pass

    def createFrames(self, fig1, fig2, relationship_to_match):
        all_rels = []
        a_objs = fig1.objects
        b_objs = fig2.objects

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
        b_perm = list(itertools.permutations(b_names))
        bestrels = {}
        bestweight = 0
        for b_names in b_perm:
            relationship = {}
            wt = 0

            for a_name, b_name in zip(a_names,b_names):
                a_obj_atts = {}
                b_obj_atts = {}

                if a_name == None:
                    relationship[b_name] = []
                    relationship[b_name].append("Added")
                elif b_name == None:
                    relationship[a_name] = []
                    relationship[a_name].append("Deleted")
                else:
                    relationship[b_name] = []

                    for obj in a_objs:
                        if a_objs[obj].name == a_name:
                            a_obj = obj
                    for obj in b_objs:
                        if b_objs[obj].name == b_name:
                            b_obj = obj

                    # have to check before doing this
                    # A may be added or deleted and vis versa for b
                    for a_obj_att in a_objs[a_obj].attributes:
                        a_obj_atts[a_obj_att] = a_objs[a_obj].attributes[a_obj_att]


                    for b_obj_att in b_objs[b_obj].attributes:
                        b_obj_atts[b_obj_att] = b_objs[b_obj].attributes[b_obj_att]




                    try:
                        if a_obj_atts[size] == b_obj_atts[size]:
                            relationship[b_name].append("SameSize")
                            wt += 5
                        else:
                            relationship[b_name].append("DifferentSize")
                    except KeyError:
                        pass


                    try:
                        if a_obj_atts[shape] == b_obj_atts[shape]:
                            relationship[b_name].append("SameShape")
                            wt += 5
                        else:
                            relationship[b_name].append("DifferentShape")
                            wt += 2
                    except KeyError:
                        pass

                    try:
                        if a_obj_atts[fill] == b_obj_atts[fill]:
                            relationship[b_name].append("SameFill")
                            wt += 4
                        else:
                            relationship[b_name].append("DifferentFill")
                            wt += 2
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
                            wt += 5
                        else:
                            relationship[b_name].append("DifferentAngle")
                            relationship[b_name].append(abs(int(a_obj_atts[angle]) - int(b_obj_atts[angle])))
                            wt += 2
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
            if relationship == relationship_to_match:
                wt += 100
            if wt > bestweight:
                bestrels = relationship
                bestweight = wt

        return bestrels


    def addToPossibleAnswers(self, answers):
        possible_answers = []
        for name, value in answers.items():
            if value == max(iter(answers.values())):
                possible_answers.append(name)

        return possible_answers


    def addAnswerScores(self, rel_1, rel_2):
        answer_scores = {}
        for answer, rel in rel_2.items():
            answer_scores[answer] = 0
            for a_b, rels in zip(rel_1.values(),rel.values()):
                answer_scores[answer] += len(set(a_b).intersection(rels))

        return answer_scores


    def createGuessFrames(self, problem):
        X_i_relationship = {}
        for i in range(1,7):
            X_i_relationship[i] = []
            X_i_relationship[i] = self.createFrames(problem.figures[C], problem.figures[str(i)], problem)

        return X_i_relationship

    def solve2x2(self, problem):

        # horizontal and vertical comparisons
        A_B_rel = self.createFrames(problem.figures[A], problem.figures[B], problem)
        A_C_rel = self.createFrames(problem.figures[A], problem.figures[C], problem)

        # create a list of relationships between C and choices
        C_i_relationship = self.createGuessFrames(problem)
        B_i_relationship = self.createGuessFrames(problem)

        # compare lists A -> B ( horizontal )
        answer_scores_hor = self.addAnswerScores(A_B_rel, C_i_relationship)

        # compare lists A -> C ( vertical )
        answer_scores_ver = self.addAnswerScores(A_C_rel, B_i_relationship)

        possible_answers_hor = self.addToPossibleAnswers(answer_scores_hor)
        possible_answers_ver = self.addToPossibleAnswers(answer_scores_ver)

        counts = {}
        for val in possible_answers_hor:
            counts[val] = counts.get(val, 0) + 1

        if len(counts) == 1:
            print(counts)
            return list(counts.keys())[0]

        for val in possible_answers_ver:
            counts[val] = counts.get(val, 0) + 1
        print(counts)


        # TODO: fix
        if len(counts) > 1:
            for val in counts:
                if counts[val] == 2:
                    return val

        return random.choice(list(counts))