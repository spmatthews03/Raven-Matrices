
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image
import math, operator
from AgentHelper import *
import statistics

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
        global image_a, image_b, image_c, image_d, image_e, image_f, image_g, image_h, image_1, image_2, image_3, image_4, image_5, image_6, image_7, image_8
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

    def not_quite_random_solver(self, problem):
        c_pixel = helper.get_num_pixels(image_c)
        f_pixel = helper.get_num_pixels(image_f)
        g_pixel = helper.get_num_pixels(image_g)
        h_pixel = helper.get_num_pixels(image_h)

        if c_pixel == -1 or f_pixel == -1 or g_pixel == -1 or h_pixel == -1:
            return -1

        mean_diff = ((c_pixel - f_pixel) + (g_pixel - h_pixel)) / 2
        mean_pixel = (f_pixel + h_pixel) / 2

        pixel_array = []

        for i in range(1, 9):
            option_image = Image.open(problem.figures[str(i)].visualFilename)
            pixel_count = helper.get_num_pixels(option_image)
            pixel_array.append(abs(mean_pixel - pixel_count - mean_diff))

        if min(pixel_array) < 200:
            return pixel_array.index(min(pixel_array)) + 1
        else:
            return -1

    def object_fill_solver(self, problem):
        c_width = helper.get_bounding_box(image_c)[2] - helper.get_bounding_box(image_c)[0]
        g_width = helper.get_bounding_box(image_g)[2] - helper.get_bounding_box(image_g)[0]

        scale = c_width / float(g_width)

        scale_tuple = int(scale * image_b.size[0]), int(scale * image_b.size[1])
        resized_g = image_g.resize(scale_tuple)
        resized_b = image_b.resize(scale_tuple)
        scaled_width, scaled_height = resized_g.size

        margin_L = (scaled_width - image_b.size[0]) / 2
        margin_R = scaled_width - margin_L
        margin_Up = (scaled_height - image_a.size[1]) / 2
        margin_Low = scaled_height - margin_Up
        crop_box = margin_L, margin_Up, margin_R, margin_Low

        cropped_g = resized_g.crop(crop_box)
        diff = helper.difference(cropped_g, helper.get_difference(image_c, image_e))

        cropped_b = resized_b.crop(crop_box)
        sol_image = helper.get_difference(cropped_b, image_d)

        diff_score_array = []
        if diff < 4:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = helper.difference(sol_image, option_image)
                diff_score_array.append(diff_score)

            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1
        else:
            return -1

    def rolling_transformation_solver(self, problem):
        try:
            intersect = helper.get_intersection(image_a, image_c)
            a_new = ImageChops.invert(ImageChops.difference(image_a, intersect))
            b_new = ImageChops.invert(ImageChops.difference(image_b, intersect))
            c_new = ImageChops.invert(ImageChops.difference(image_c, intersect))

            sol_intersect = helper.get_intersection(image_g, image_h)
            g_new = ImageChops.invert(ImageChops.difference(image_g, sol_intersect))
            h_new = ImageChops.invert(ImageChops.difference(image_h, sol_intersect))

            diff_list = []
            match_list = []
            diff_list.append(helper.difference(a_new, g_new))
            diff_list.append(helper.difference(image_b, g_new))
            diff_list.append(helper.difference(image_c, g_new))

            for index in range(len(diff_list)):
                if diff_list[index] < 3:
                    match_list.append(index)

            del diff_list[:]

            diff_list.append(helper.difference(a_new, h_new))
            diff_list.append(helper.difference(b_new, h_new))
            diff_list.append(helper.difference(c_new, h_new))

            for index in range(len(diff_list)):
                if diff_list[index] < 3:
                    match_list.append(index)

            if match_list[0] == 0 and match_list[1] == 1:
                sol_img = c_new
            elif match_list[0] == 0 and match_list[1] == 2:
                sol_img = b_new
            else:
                sol_img = a_new

            if diff_list[match_list[1]] < 3:
                diff_score_array = []
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    sol_new = ImageChops.invert(ImageChops.difference(result_option, sol_intersect))
                    diff_score = helper.difference(sol_img, sol_new)
                    diff_score_array.append(diff_score)
                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1
        except BaseException:
            pass
        return -1

    def roll_extract_solver(self, problem):
        try:
            rotated_square = helper.get_intersection(image_b, image_f)
            four_squares = helper.get_difference(rotated_square, image_f)
            rotated_lines = helper.get_difference(rotated_square, image_b)
            circle = helper.get_intersection(image_c, image_d)
            square = helper.get_difference(four_squares, image_a)
            straight_lines = helper.get_difference(circle, image_c)

            shape_array = [square, rotated_square, circle, four_squares, rotated_lines, straight_lines]

            diff_array = []
            index_array = []

            for i in range(len(shape_array)):
                for j in range(i + 1, len(shape_array), 1):
                    temp_image = helper.union(shape_array[i], shape_array[j])
                    diff = helper.difference(temp_image, image_g)
                    diff_array.append(diff)
                    index_array.append((i, j))

            diff_1 = min(diff_array)
            index_a, index_b = index_array[diff_array.index(min(diff_array))]

            shape_a = shape_array[index_a]
            shape_b = shape_array[index_b]
            shape_array.remove(shape_a)
            shape_array.remove(shape_b)

            del diff_array[:]
            del index_array[:]

            for i in range(len(shape_array)):
                for j in range(i + 1, len(shape_array), 1):
                    temp_image = helper.union(shape_array[i], shape_array[j])
                    diff = helper.difference(temp_image, image_h)
                    diff_array.append(diff)
                    index_array.append((i, j))

            diff_2 = min(diff_array)
            index_c, index_d = index_array[diff_array.index(min(diff_array))]

            shape_c = shape_array[index_c]
            shape_d = shape_array[index_d]
            shape_array.remove(shape_c)
            shape_array.remove(shape_d)

            sol_new = helper.union(shape_array[0], shape_array[1])

            diff_score_array = []

            if diff_1 < 6 and diff_2 < 6:
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(sol_new, option_image)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 2.5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass

        return -1

    # solve by calculating the approximation of how much the answer image should increase in dark pixels
    def percent_increase_solver(self):
        hor_possible_answers = []
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

        possible_answers = set()

        for answer in hor_possible_answers:
            possible_answers.add(answer)

        if len(possible_answers) == 1:
            return possible_answers.pop()
        else:
            return -1

    def another_diff_solver(self, problem):
        diff_ac = ImageChops.invert(ImageChops.difference(image_a, image_c))
        diff_score_array = []
        for i in range(1, 9):
            result_option = Image.open(problem.figures[str(i)].visualFilename)
            g_diff_sol = ImageChops.invert(ImageChops.difference(image_g, result_option))
            diff_score = helper.difference(diff_ac, g_diff_sol)
            diff_score_array.append(diff_score)

        if min(diff_score_array) < 3.0:
            return diff_score_array.index(min(diff_score_array)) + 1
        else:
            return -1

    def crop_solver(self, problem):
        width_a = image_a.size[0]
        height_a = image_a.size[1]

        width_b = image_b.size[0]
        height_b = image_b.size[1]

        crop_box_a_1 = 0, 0, width_a, height_a / 2
        crop_box_a_2 = 0, height_a/2, width_a, height_a
        crop_box_a_3 = 0, 0, width_a/2, height_a
        crop_box_a_4 = width_a/2, 0, width_a, height_a
        crop_box_b_1 = 0, height_b / 2, width_b, height_b
        crop_box_b_2 = 0, 0, width_b, height_b/2
        crop_box_b_3 = width_b/2, 0, width_b, height_b
        crop_box_b_4 = 0, 0, width_b/2, height_b

        cropped_a_1 = image_a.crop(crop_box_a_1)
        cropped_a_2 = image_a.crop(crop_box_a_2)
        cropped_a_3 = image_a.crop(crop_box_a_3)
        cropped_a_4 = image_a.crop(crop_box_a_4)
        cropped_b_1 = image_b.crop(crop_box_b_1)
        cropped_b_2 = image_b.crop(crop_box_b_2)
        cropped_b_3 = image_b.crop(crop_box_b_3)
        cropped_b_4 = image_b.crop(crop_box_b_4)

        c_new_1 = image_a.copy()
        c_new_2 = image_a.copy()
        c_new_3 = image_a.copy()
        c_new_4 = image_a.copy()
        c_new_1.paste(cropped_a_1, (0, 0, width_a, height_a / 2))
        c_new_1.paste(cropped_b_1, (0, height_b / 2, width_b, height_b))
        c_new_2.paste(cropped_a_2, (0, height_a/2, width_a, height_a))
        c_new_2.paste(cropped_b_2, (0, 0, width_b, height_b/2))
        c_new_3.paste(cropped_a_3, (0, 0, width_a/2, height_a))
        c_new_3.paste(cropped_b_3, (width_b/2, 0, width_b, height_b))
        c_new_4.paste(cropped_a_4, (width_a/2, 0, width_a, height_a))
        c_new_4.paste(cropped_b_4, (0, 0, width_b/2, height_b))

        diff_1 = helper.difference(image_c, c_new_1)
        diff_2 = helper.difference(image_c, c_new_2)
        diff_3 = helper.difference(image_c, c_new_3)
        diff_4 = helper.difference(image_c, c_new_4)

        width_g = image_g.size[0]
        height_g = image_g.size[1]

        width_h = image_h.size[0]
        height_h = image_h.size[1]

        crop_box_g_1 = 0, 0, width_g, height_g / 2
        crop_box_g_2 = 0, height_g/2, width_g, height_g
        crop_box_g_3 = 0, 0, width_g/2, height_g
        crop_box_g_4 = width_g/2, 0, width_g, height_g
        crop_box_h_1 = 0, height_h / 2, width_h, height_h
        crop_box_h_2 = 0, 0, width_h, height_h/2
        crop_box_h_3 = width_h/2, 0, width_h, height_h
        crop_box_h_4 = 0, 0, width_h/2, height_h

        cropped_g_1 = image_g.crop(crop_box_g_1)
        cropped_g_2 = image_g.crop(crop_box_g_2)
        cropped_g_3 = image_g.crop(crop_box_g_3)
        cropped_g_4 = image_g.crop(crop_box_g_4)
        cropped_h_1 = image_h.crop(crop_box_h_1)
        cropped_h_2 = image_h.crop(crop_box_h_2)
        cropped_h_3 = image_h.crop(crop_box_h_3)
        cropped_h_4 = image_h.crop(crop_box_h_4)

        sol_new_1 = image_g.copy()
        sol_new_2 = image_g.copy()
        sol_new_3 = image_g.copy()
        sol_new_4 = image_g.copy()

        sol_new_1.paste(cropped_g_1, (0, 0, width_g, height_g / 2))
        sol_new_1.paste(cropped_h_1, (0, height_h / 2, width_h, height_h))
        sol_new_2.paste(cropped_g_2, (0, height_g/2, width_g, height_g))
        sol_new_2.paste(cropped_h_2, (0, 0, width_h, height_h/2))
        sol_new_3.paste(cropped_g_3, (0, 0, width_g/2, height_g))
        sol_new_3.paste(cropped_h_3, (width_h/2, 0, width_h, height_h))
        sol_new_4.paste(cropped_g_4, (width_g/2, 0, width_g, height_g))
        sol_new_4.paste(cropped_h_4, (0, 0, width_h/2, height_h))

        diff_score_array_1 = []
        diff_score_array_2 = []
        diff_score_array_3 = []
        diff_score_array_4 = []
        if diff_1 < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = helper.difference(sol_new_1, option_image)
                diff_score_array_1.append(diff_score)

            if min(diff_score_array_1) < 5:
                return diff_score_array_1.index(min(diff_score_array_1)) + 1
            else:
                return -1

        if diff_2 < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = helper.difference(sol_new_2, option_image)
                diff_score_array_2.append(diff_score)

            if min(diff_score_array_2) < 5:
                return diff_score_array_2.index(min(diff_score_array_2)) + 1
            else:
                return -1

        if diff_3 < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = helper.difference(sol_new_3, option_image)
                diff_score_array_3.append(diff_score)

            if min(diff_score_array_3) < 5:
                return diff_score_array_3.index(min(diff_score_array_3)) + 1
            else:
                return -1

        if diff_4 < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = helper.difference(sol_new_4, option_image)
                diff_score_array_4.append(diff_score)

            if min(diff_score_array_4) < 5:
                return diff_score_array_4.index(min(diff_score_array_4)) + 1
            else:
                return -1

    def extract_inner_solver(self, problem):
        try:
            union_ab = helper.union(image_a, image_b)
            union_de = helper.union(image_d, image_e)
            row_a = helper.union(union_ab, image_c)
            row_b = helper.union(union_de, image_f)

            diff = ImageChops.invert(ImageChops.difference(row_a, row_b))

            g_union_h = helper.union(image_g, image_h)
            diff_score_array = []
            for i in range(1, 9):
                if i == 1:
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    row_c = helper.union(g_union_h, result_option)
                    sol_diff = ImageChops.invert(ImageChops.difference(row_b, row_c))
                    temp_img = helper.union(diff, sol_diff)
                    a1 = ImageChops.invert(ImageChops.difference(image_a, temp_img))
                    b1 = ImageChops.invert(ImageChops.difference(image_b, temp_img))
                    c1 = ImageChops.invert(ImageChops.difference(image_c, temp_img))

                    diff_list = []
                    match_list = []
                    diff_list.append(helper.difference(a1, image_g))
                    diff_list.append(helper.difference(b1, image_g))
                    diff_list.append(helper.difference(c1, image_g))

                    for index in range(len(diff_list)):
                        if diff_list[index] < 2.5:
                            match_list.append(index)

                    del diff_list[:]

                    diff_list.append(helper.difference(a1, image_h))
                    diff_list.append(helper.difference(b1, image_h))
                    diff_list.append(helper.difference(c1, image_h))

                    for index in range(len(diff_list)):
                        if diff_list[index] < 2.5:
                            match_list.append(index)

                    if match_list[0] == 0 and match_list[1] == 1:
                        sol_img = c1
                    elif match_list[0] == 0 and match_list[1] == 2:
                        sol_img = b1
                    else:
                        sol_img = a1

                    if diff_list[match_list[1]] < 2.5:
                        diff_score = helper.difference(sol_img, result_option)
                        diff_score_array.append(diff_score)
                        return diff_score_array.index(min(diff_score_array)) + 1
                    else:
                        return -1
        except BaseException:
            pass
        return -1

    def pixel_solver(self, problem):
        try:
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_c))
            union = helper.union(image_diff, image_a)
            diff = helper.difference(union, image_c)

            if diff <= 1:
                diff_score_array = []
                if helper.difference(image_diff, image_g) < 1:
                    return -1

                final_transform = helper.union(image_diff, image_g)
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(final_transform, result_option)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 1.5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1

        except BaseException:
            pass

        return -1

    def reflection_solver(self, problem):
        try:
            transpose_a = image_a.transpose(Image.FLIP_LEFT_RIGHT)
            diff = helper.difference(transpose_a, image_c)

            if diff < 2:
                value_array = []
                transpose_g = image_g.transpose(Image.FLIP_LEFT_RIGHT)
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    option_diff = math.fabs(helper.difference(transpose_g, option_image) - diff)
                    value_array.append(option_diff)

                return value_array.index(min(value_array)) + 1
            else:
                return -1

        except BaseException:
            pass

        return -1

    def get_dark_pixel_total(self, img1, img2, img3):
        return sum(img1.histogram()[:-1]) + sum(img2.histogram()[:-1]) + sum(img3.histogram()[:-1])

    def check_option_for_dark_row_total(self, option, total):
        row_total = self.get_dark_pixel_total(image_g.convert("1"), image_h.convert("1"), option)
        if row_total == total:
            return True
        else:
            return -1

    def shift_solver(self, problem):
        try:
            dim_a = helper.get_bounding_box(image_a)
            width_a = dim_a[2] - dim_a[0]
            offset_b = ImageChops.offset(image_b, -width_a / 3, 0)
            image_diff_1 = ImageChops.invert(ImageChops.difference(image_a, offset_b))
            row_a_offset = ImageChops.offset(image_diff_1, int(-width_a / 6), 0)
            diff = helper.difference(row_a_offset, image_c)

            dim_g = helper.get_bounding_box(image_g)
            width_g = dim_g[2] - dim_g[0]
            offset_h = ImageChops.offset(image_h, -width_g / 3, 0)
            image_diff_2 = ImageChops.invert(ImageChops.difference(image_g, offset_h))
            row_c_offset = ImageChops.offset(image_diff_2, int(-width_g / 6), 0)

            diff_score_array = []

            if diff < 1:
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(row_c_offset, option_image)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass

        return -1

    def reverse_solver(self, problem):
        # TODO: Generalize by adding center aligning code
        try:
            dim_a = helper.get_bounding_box(image_a)
            width_a = dim_a[2] - dim_a[0]
            dim_b = helper.get_bounding_box(image_b)
            width_b = dim_b[2] - dim_b[0]
            # print width_a, width_b
            transpose_b = image_b.transpose(Image.FLIP_TOP_BOTTOM)
            offset_b = ImageChops.offset(transpose_b, int(-width_a / 3), 0)
            image_diff_1 = ImageChops.invert(ImageChops.difference(image_a, offset_b))
            c_new = ImageChops.offset(image_diff_1, int(-width_a / 6), 0)
            diff_1 = helper.difference(image_c, c_new)

            dim_d = helper.get_bounding_box(image_d)
            width_d = dim_a[2] - dim_d[0]
            dim_e = helper.get_bounding_box(image_e)
            width_e = dim_e[2] - dim_e[0]
            # print width_d, width_e
            transpose_e = image_e.transpose(Image.FLIP_TOP_BOTTOM)
            offset_e = ImageChops.offset(transpose_e, int(-width_d / 6), 0)
            image_diff_2 = ImageChops.invert(ImageChops.difference(image_d, offset_e))
            f_new = ImageChops.offset(image_diff_2, int(-width_d / 3), 0)
            diff_2 = helper.difference(image_f, f_new)

            dim_g = helper.get_bounding_box(image_g)
            width_g = dim_g[2] - dim_g[0]
            dim_h = helper.get_bounding_box(image_h)
            width_h = dim_h[2] - dim_h[0]
            # print width_g, width_h
            transpose_h = image_h.transpose(Image.FLIP_TOP_BOTTOM)
            offset_h = ImageChops.offset(transpose_h, int(-width_h / 2), 0)
            image_diff_3 = ImageChops.invert(ImageChops.difference(image_g, offset_h))
            sol_new = ImageChops.offset(image_diff_3, int(-width_h / 2), 0)

            diff_score_array = []
            if diff_1 < 1 or diff_2 < 1:
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(sol_new, option_image)
                    diff_score_array.append(diff_score)
                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass

        return -1

    def diff_solver(self, problem):
        # TODO: fix 7 and 8 for Set E
        try:
            image_diff_1 = ImageChops.invert(ImageChops.difference(image_a, image_b))
            diff = helper.difference(image_diff_1, image_c)
            image_diff_2 = ImageChops.invert(ImageChops.difference(image_g, image_h))

            diff_score_array = []
            if diff < 2:
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(image_diff_2, option_image)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass

        return -1

    def intersection_solver(self, problem):
        union_ab = helper.get_intersection(image_a, image_b)
        union_gh = helper.get_intersection(image_g, image_h)
        diff = helper.difference(union_ab, image_c)
        diff_score_array = []

        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = helper.difference(union_gh, option_image)
                diff_score_array.append(diff_score)

            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

    def scaling_solver(self, problem):
        try:
            dim_a = helper.get_bounding_box(image_a)
            dim_b = helper.get_bounding_box(image_b)
            dim_c = helper.get_bounding_box(image_c)

            length_a = dim_a[2] - dim_a[0]
            length_b = dim_b[2] - dim_b[0]
            length_c = dim_c[2] - dim_c[0]

            scalex_ba = length_b / float(length_a)

            scalex_cb = length_c / float(length_b)
            scale_tuple = int(scalex_cb * scalex_ba * image_a.size[0]), int(scalex_cb * scalex_ba * image_a.size[1])

            # find intersection between a & c
            diff_ac = ImageChops.invert(ImageChops.difference(image_a, image_c))
            ac_intersect_a = helper.get_intersection(diff_ac, image_a)

            # resize the image
            resized_a = ac_intersect_a.resize(scale_tuple)

            scaled_width = resized_a.size[0]
            scaled_length = resized_a.size[1]

            # find the crop box tuple
            left_margin = (scaled_width - image_a.size[0]) / 2
            right_margin = scaled_width - left_margin
            upper_margin = (scaled_length - image_a.size[1]) / 2
            lower_margin = scaled_length - upper_margin
            crop_box = left_margin, upper_margin, right_margin, lower_margin

            a_intersect_c = helper.get_intersection(image_a, image_c)
            cropped_a = resized_a.crop(crop_box)

            final_transform = helper.union(a_intersect_c, cropped_a)

            diff = helper.difference(final_transform, image_c)

            # now apply the transformation to solution set and check
            scale_factor = length_c / float(length_a)
            result_scale = int(scale_factor * image_a.size[0]), int(scale_factor * image_a.size[1])
            # 97 percent similarity
            if diff < 3:
                g_intersect_a = ImageChops.difference(image_g, image_a)
                g_intersect_a = ImageChops.invert(g_intersect_a)
                ga_intersect_g = helper.get_intersection(g_intersect_a, image_g)
                ga_intersect_g_resize = ga_intersect_g.resize(result_scale)

                scaled_width = ga_intersect_g_resize.size[0]
                scaled_length = ga_intersect_g_resize.size[1]

                left_margin = (scaled_width - image_a.size[0]) / 2
                right_margin = scaled_width - left_margin
                upper_margin = (scaled_length - image_a.size[1]) / 2
                lower_margin = scaled_length - upper_margin
                crop_box = left_margin, upper_margin, right_margin, lower_margin

                cropped_g = ga_intersect_g_resize.crop(crop_box)
                result_final_transform = helper.union(a_intersect_c, cropped_g)

                diff_score_array = []
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(result_final_transform, result_option)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 7:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1

        except BaseException:
            pass

        return -1

    def offset_solve(self, problem, flag):
        try:
            dim_a = helper.get_bounding_box(image_a)
            dim_c = helper.get_bounding_box(image_c)

            left_image = ImageChops.offset(image_a, dim_c[0] - dim_a[0], dim_c[1] - dim_a[1])
            right_image = ImageChops.offset(image_a, dim_c[2] - dim_a[2], dim_c[3] - dim_a[3])
            if flag == 0:
                left_intersect_a = helper.union(left_image, image_a)
                final_intersect = helper.union(left_intersect_a, right_image)
            elif flag == 1:
                final_intersect = helper.union(left_image, right_image)
            else:
                return -1

            diff = helper.difference(final_intersect, image_c)

            if diff <= 3:
                left_image_g = ImageChops.offset(image_g, dim_c[0] - dim_a[0], dim_c[1] - dim_a[1])
                right_image_g = ImageChops.offset(image_g, dim_c[2] - dim_a[2], dim_c[3] - dim_a[3])
                if flag == 0:
                    left_intersect_g = helper.union(left_image_g, image_g)
                    final_transform = helper.union(left_intersect_g, right_image_g)
                elif flag == 1:
                    final_transform = helper.union(left_image_g, right_image_g)
                else:
                    return -1

                diff_score_array = []
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(final_transform, result_option)
                    diff_score_array.append(diff_score)
                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                if flag == 1:
                    return -1
                else:
                    return self.offset_solve(problem, 1)

        except BaseException:
            pass

        return -1

    def roller_solver(self, problem):
        try:
            width, length = image_a.size[0], image_a.size[1]

            left_half = image_a.crop((0, 0, width / 2, length))
            right_half = image_a.crop((width / 2, 0, width, length))

            final_image = image_a.copy()
            final_image.paste(right_half, (5, 0, width / 2 + 5, length))
            final_image.paste(left_half, (width / 2 - 5, 0, width - 5, length))

            diff = helper.difference(final_image, image_c)

            diff_list = []
            match_list = []
            diff_list.append(helper.difference(image_a, image_g))
            diff_list.append(helper.difference(image_b, image_g))
            diff_list.append(helper.difference(image_c, image_g))

            diff_list.append(helper.difference(image_a, image_h))
            diff_list.append(helper.difference(image_b, image_h))
            diff_list.append(helper.difference(image_c, image_h))

            for index in range(len(diff_list)):
                if diff_list[index] < 1:
                    match_list.append(index)

            if match_list[0] == 0 and match_list[1] == 1:
                sol_img = image_c
            elif match_list[0] == 0 and match_list[1] == 2:
                sol_img = image_b
            else:
                sol_img = image_a

            for index in range(len(diff_list)):
                if diff_list[index] < 1:
                    match_list.append(index)

            del diff_list[:]



            if diff <= 2:
                width, length = image_g.size[0], image_g.size[1]

                left_half = image_g.crop((0, 0, width / 2, length))
                right_half = image_g.crop((width / 2, 0, width, length))

                final_transform = image_g.copy()
                final_transform.paste(right_half, (0, 0, width / 2, length))
                final_transform.paste(left_half, (width / 2, 0, width, length))

                diff_score_array = []
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(final_transform, result_option)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1

            if diff_list[match_list[1]] < 1:
                diff_score_array = []
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(sol_img, result_option)
                    diff_score_array.append(diff_score)
                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass

        return -1

    def diagonal_solver(self, problem):
        try:
            plus = helper.get_intersection(image_f, image_h)
            circle = helper.get_difference(plus, image_f)
            four_dots = helper.get_difference(image_a, plus)
            square = helper.get_difference(circle, image_b)
            bigger_square = helper.get_difference(square, image_d)
            heart = helper.get_difference(four_dots, image_e)

            diff_1 = helper.difference(helper.union(plus, four_dots), image_a)
            diff_2 = helper.difference(helper.union(heart, four_dots), image_e)
            sol_image = helper.union(square, four_dots)

            diff_score_array = []
            if diff_1 < 2 and diff_2 < 2:
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = helper.difference(sol_image, option_image)
                    diff_score_array.append(diff_score)

                if min(diff_score_array) < 5:
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1
            else:
                return -1

        except BaseException:
            pass

        return -1

    def and_solver(self, problem):
        threshold = 120
        image_a_mode_1 = image_a.convert("1")
        image_b_mode_1 = image_b.convert("1")
        image_c_mode_1 = image_c.convert("1")
        image_d_mode_1 = image_d.convert("1")
        image_e_mode_1 = image_e.convert("1")
        image_f_mode_1 = image_f.convert("1")
        image_g_mode_1 = image_g.convert("1")
        image_h_mode_1 = image_h.convert("1")
        and_problem = False

        if abs(helper.calculate_percent_difference(ImageChops.logical_and(image_a_mode_1, image_b_mode_1), image_c_mode_1)) < .005:
            and_problem = True
        temp = helper.calculate_percent_difference(ImageChops.logical_and(image_d_mode_1, image_e_mode_1), image_f_mode_1)
        if abs(helper.calculate_percent_difference(ImageChops.logical_and(image_d_mode_1, image_e_mode_1), image_f_mode_1)) < .005:
            and_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_and(image_a_mode_1, image_d_mode_1), image_g_mode_1)) < .005:
            and_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_and(image_b_mode_1, image_f_mode_1), image_h_mode_1)) < .005:
            and_problem = True

        gh_img = ImageChops.logical_and(image_g_mode_1, image_h_mode_1)
        gh_img = gh_img.convert("L")

        cf_img = ImageChops.logical_and(image_c_mode_1, image_f_mode_1)
        cf_img = cf_img.convert("L")

        if and_problem:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename).convert("L")
                gh_option = ImageChops.difference(gh_img.filter(ImageFilter.BLUR), option_image.filter(ImageFilter.BLUR))
                cf_option = ImageChops.difference(cf_img.filter(ImageFilter.BLUR), option_image.filter(ImageFilter.BLUR))
                diff_gh = gh_option.point(lambda p: p > threshold)
                diff_cf = cf_option.point(lambda p: p > threshold)
                if diff_gh.getbbox() is None or diff_cf.getbbox() is None:
                    return i

        return -1

    def or_solver(self, problem):
        threshold = 120
        image_a_mode_1 = image_a.convert("1")
        image_b_mode_1 = image_b.convert("1")
        image_c_mode_1 = image_c.convert("1")
        image_d_mode_1 = image_d.convert("1")
        image_e_mode_1 = image_e.convert("1")
        image_f_mode_1 = image_f.convert("1")
        image_g_mode_1 = image_g.convert("1")
        image_h_mode_1 = image_h.convert("1")
        or_problem = False

        if abs(helper.calculate_percent_difference(ImageChops.logical_or(image_a_mode_1, image_b_mode_1), image_c_mode_1)) < .005:
            or_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_or(image_d_mode_1, image_e_mode_1), image_f_mode_1)) < .005:
            or_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_or(image_a_mode_1, image_d_mode_1), image_g_mode_1)) < .005:
            or_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_or(image_b_mode_1, image_f_mode_1), image_h_mode_1)) < .005:
            or_problem = True

        gh_img = ImageChops.logical_or(image_g_mode_1, image_h_mode_1)
        gh_img = gh_img.convert("L")

        cf_img = ImageChops.logical_or(image_c_mode_1, image_f_mode_1)
        cf_img = cf_img.convert("L")

        if or_problem:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename).convert("L")
                gh_option = ImageChops.difference(gh_img.filter(ImageFilter.BLUR), option_image.filter(ImageFilter.BLUR))
                cf_option = ImageChops.difference(cf_img.filter(ImageFilter.BLUR), option_image.filter(ImageFilter.BLUR))
                diff_gh = gh_option.point(lambda p: p > threshold)
                diff_cf = cf_option.point(lambda p: p > threshold)
                if diff_gh.getbbox() is None or diff_cf.getbbox() is None:
                    return i
        return -1

    def xor_solver(self, problem):
        threshold = 120
        xor_problem = False
        image_a_mode_1 = image_a.convert("1")
        image_b_mode_1 = image_b.convert("1")
        image_c_mode_1 = image_c.convert("1")
        image_d_mode_1 = image_d.convert("1")
        image_e_mode_1 = image_e.convert("1")
        image_f_mode_1 = image_f.convert("1")
        image_g_mode_1 = image_g.convert("1")
        image_h_mode_1 = image_h.convert("1")

        if abs(helper.calculate_percent_difference(ImageChops.logical_xor(image_a_mode_1, image_b_mode_1), image_c_mode_1)) < 1:
            xor_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_xor(image_d_mode_1, image_e_mode_1), image_f_mode_1)) < 1:
            xor_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_xor(image_a_mode_1, image_d_mode_1), image_g_mode_1)) < 1:
            xor_problem = True
        if abs(helper.calculate_percent_difference(ImageChops.logical_xor(image_b_mode_1, image_f_mode_1), image_h_mode_1)) < 1:
            xor_problem = True

        cf_img = ImageChops.invert(ImageChops.difference(image_c_mode_1, image_f_mode_1))
        cf_img = cf_img.convert("L")

        gh_img = ImageChops.invert(ImageChops.difference(image_c_mode_1, image_f_mode_1))
        gh_img = gh_img.convert("L")

        if xor_problem:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename).convert("L")
                gh_option = ImageChops.difference(gh_img.filter(ImageFilter.BLUR), option_image.filter(ImageFilter.BLUR))
                cf_option = ImageChops.difference(cf_img.filter(ImageFilter.BLUR), option_image.filter(ImageFilter.BLUR))
                diff_gh = gh_option.point(lambda p: p > threshold)
                diff_cf = cf_option.point(lambda p: p > threshold)
                if diff_gh.getbbox() is None or diff_cf.getbbox() is None:
                    return i

        return -1

    def diff_union_solver(self, problem):
        mean = statistics.mean([helper.get_num_pixels(image_a), helper.get_num_pixels(image_b), helper.get_num_pixels(image_c)])
        a_union_b = helper.union(image_a, image_b)
        d_union_e = helper.union(image_d, image_e)
        g_union_h = helper.union(image_g, image_h)

        diff_1 = helper.difference(a_union_b, image_c)
        diff_2 = helper.difference(d_union_e, image_f)
        diff_score_array = []
        if diff_1 < 5 and diff_2 < 7 and mean > 1000 and helper.get_num_pixels(image_c) > 1300:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score_array.append(helper.difference(g_union_h, option_image))
            if min(diff_score_array) < 6:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

