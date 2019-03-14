
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image
import math
from AgentHelper import *

INCREASE_THRESHOLD = 9


A = 'A'
B = 'B'
C = 'C'
D = 'D'
E = 'E'
F = 'F'
G = 'G'
H = 'H'

class Solvers:

    def __init__(self, problem):
        global helper

        for key, val in sorted(problem.figures.items()):
            self.setup_image(key, problem.figures[key].visualFilename)

        helper = AgentHelper(problem)


    def setup_image(self, key, image):
        global image_a, image_b, image_c, image_d, image_e, image_f, image_g, image_h
        if key == 'A':
            image_a = Image.open(image)
        if key == 'B':
            image_b = Image.open(image)
        if key == 'C':
            image_c = Image.open(image)
        if key == 'D':
            image_d = Image.open(image)
        if key == 'E':
            image_e = Image.open(image)
        if key == 'F':
            image_f = Image.open(image)
        if key == 'G':
            image_g = Image.open(image)
        if key == 'H':
            image_h = Image.open(image)
        if key == '1':
            image_1 = Image.open(image)
        if key == '2':
            image_2 = Image.open(image)
        if key == '3':
            image_3 = Image.open(image)
        if key == '4':
            image_4 = Image.open(image)
        if key == '5':
            image_5 = Image.open(image)
        if key == '6':
            image_6 = Image.open(image)
        if key == '7':
            image_7 = Image.open(image)
        if key == '8':
            image_8 = Image.open(image)

    def union(self, image_1, image_2):
        return ImageChops.lighter(image_1, image_2)

    def difference(self, image_1, image_2):
        pairs = zip(image_1.getdata(), image_2.getdata())
        if len(image_1.getbands()) == 1:
            dif = sum(abs(p1 - p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1,c2 in zip(p1,p2))

        num_components = image_1.size[0] * image_1.size[1] * 3
        return (dif / 255.0 * 100 ) / num_components


    # solve by calculating the approximation of how much the answer image should increase in dark pixels
    def percent_increase_solver(self):
        hor_possible_answers = {}
        hor_possible_answers = []
        ver_possible_answers = {}
        ver_possible_answers = []
        figures = ['A', 'B', 'C', 'D',
                   'E', 'F', 'G', 'H']
        options = ['1', '2', '3', '4',
                   '5', '6', '7', '8']

        figures_images, answer_images, figure_images_stats, \
        answer_images_stats, figure_images_logic, answer_images_logic = helper.populate_dictionaries(figures, options)

        # horizontal percentages
        ab_percent, bc_percent, ac_percent = helper.calculateIfPixelPercentageEqual(figure_images_stats[A],
                                                                                    figure_images_stats[B],
                                                                                    figure_images_stats[C])
        de_percent, ef_percent, df_percent = helper.calculateIfPixelPercentageEqual(figure_images_stats[D],
                                                                                    figure_images_stats[E],
                                                                                    figure_images_stats[F])

        # vertical percentages
        ad_percent, dg_percent, ag_percent = helper.calculateIfPixelPercentageEqual(figure_images_stats[A],
                                                                                    figure_images_stats[D],
                                                                                    figure_images_stats[G])
        be_percent, eh_percent, bh_percent = helper.calculateIfPixelPercentageEqual(figure_images_stats[B],
                                                                                    figure_images_stats[E],
                                                                                    figure_images_stats[H])

        a_b_c_percent = helper.check_percentage_change(ab_percent, bc_percent)
        d_e_f_percent = helper.check_percentage_change(de_percent, ef_percent)
        a_d_g_percent = helper.check_percentage_change(ad_percent, dg_percent)
        b_e_h_percent = helper.check_percentage_change(be_percent, eh_percent)

        for option in options:
            if helper.checkIfDarkPixelsEqual(figure_images_stats[E], figure_images_stats[F],
                                             figure_images_stats[H], answer_images_stats[option]):
                return option

            if helper.checkIfDarkPixelsEqual(figure_images_stats[E], figure_images_stats[H],
                                             figure_images_stats[F], answer_images_stats[option]):
                return option

            gh_percent, h_option_percent, g_option_percent = helper.calculateIfPixelPercentageEqual(
                figure_images_stats[G],
                figure_images_stats[H],
                answer_images_stats[option])

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

        if len(possible_answers) == 1:
            return possible_answers.pop()
        else:
            return -1

    def pixel_solver(self, problem):
        try:
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_c))
            union = self.union(image_diff, image_a)
            diff = self.difference(union, image_c)

            if diff <= 1:
                diff_score_array = []
                if self.difference(image_diff, image_g) < 1:
                    return -1

                final_transform = self.union(image_diff, image_g)
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = self.difference(final_transform, result_option)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 1.5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1

        except BaseException:
            pass

        return -1


    def get_intersection(self, image_1, image_2):
        return ImageChops.lighter(image_1, image_2)


    def reflection_solver(self, problem):
        try:
            transpose_a = image_a.transpose(Image.FLIP_LEFT_RIGHT)
            diff = self.difference(transpose_a, image_c)

            if diff < 2:
                value_array = []
                transpose_g = image_g.transpose(Image.FLIP_LEFT_RIGHT)
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    option_diff = math.fabs(self.difference(transpose_g, option_image) - diff)
                    value_array.append(option_diff)

                return value_array.index(min(value_array)) + 1
            else:
                return -1

        except BaseException:
            pass

        return -1


    def rms_solver(self, possible_answers):
        rms_images = helper.get_rms(helper.convert_images())
        return helper.choose_answer(rms_images, possible_answers)


    def get_bounding_box(self, image):
        org_image = image.convert(mode='L')
        inv_image = ImageChops.invert(org_image)
        return inv_image.getbbox()