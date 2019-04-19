# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.
# __author__ = 'Bhanu Verma'
# Install Pillow and uncomment this line to access image processing.

from PIL import Image, ImageChops
from itertools import izip
import math

__author__ = "Bhanu Verma"

image_a = None
image_b = None
image_c = None
image_d = None
image_e = None
image_f = None
image_g = None
image_h = None
image_1 = None
image_2 = None
image_3 = None
image_4 = None
image_5 = None
image_6 = None
image_7 = None
image_8 = None

objectlist_A = []
objectlist_B = []
objectlist_C = []
objectlist_D = []
objectlist_E = []
objectlist_F = []
objectlist_G = []
objectlist_H = []
objectlist_1 = []
objectlist_2 = []
objectlist_3 = []
objectlist_4 = []
objectlist_5 = []
objectlist_6 = []
objectlist_7 = []
objectlist_8 = []


def init_objects():
    global objectlist_A, objectlist_B, objectlist_C, objectlist_1, objectlist_2, objectlist_3, \
        objectlist_4, objectlist_5, objectlist_6
    del objectlist_A[:]
    del objectlist_B[:]
    del objectlist_C[:]
    del objectlist_D[:]
    del objectlist_E[:]
    del objectlist_F[:]
    del objectlist_G[:]
    del objectlist_H[:]
    del objectlist_1[:]
    del objectlist_2[:]
    del objectlist_3[:]
    del objectlist_4[:]
    del objectlist_5[:]
    del objectlist_6[:]
    del objectlist_7[:]
    del objectlist_8[:]


def parse_problem(key_value, object_list):
    for object_name, object_value in sorted(object_list.iteritems()):
        pairs = object_value.attributes
        dict_objects = {}
        for attr_name, attr_value in pairs.iteritems():
            dict_objects[attr_name] = attr_value
            dict_objects['name'] = object_name
        store_attributes(key_value, dict_objects)


def load_image(key_value, file_name):
    global image_a, image_b, image_c, image_d, image_e, image_f, image_g, \
        image_h, image_1, image_2, image_3, image_4, image_5, image_6, \
        image_7, image_8
    if key_value == 'A':
        image_a = Image.open(file_name)
    if key_value == 'B':
        image_b = Image.open(file_name)
    if key_value == 'C':
        image_c = Image.open(file_name)
    if key_value == 'D':
        image_d = Image.open(file_name)
    if key_value == 'E':
        image_e = Image.open(file_name)
    if key_value == 'F':
        image_f = Image.open(file_name)
    if key_value == 'G':
        image_g = Image.open(file_name)
    if key_value == 'H':
        image_h = Image.open(file_name)
    if key_value == '1':
        image_1 = Image.open(file_name)
    if key_value == '2':
        image_2 = Image.open(file_name)
    if key_value == '3':
        image_3 = Image.open(file_name)
    if key_value == '4':
        image_4 = Image.open(file_name)
    if key_value == '5':
        image_5 = Image.open(file_name)
    if key_value == '6':
        image_6 = Image.open(file_name)
    if key_value == '7':
        image_7 = Image.open(file_name)
    if key_value == '8':
        image_8 = Image.open(file_name)


def store_attributes(key_value, dict_objects):
    global objectlist_A, objectlist_B, objectlist_C, objectlist_D, objectlist_E, objectlist_F, objectlist_G, \
        objectlist_H, objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6, \
        objectlist_7, objectlist_8
    if key_value == 'A':
        objectlist_A.append(dict_objects)
    if key_value == 'B':
        objectlist_B.append(dict_objects)
    if key_value == 'C':
        objectlist_C.append(dict_objects)
    if key_value == 'D':
        objectlist_D.append(dict_objects)
    if key_value == 'E':
        objectlist_E.append(dict_objects)
    if key_value == 'F':
        objectlist_F.append(dict_objects)
    if key_value == 'G':
        objectlist_G.append(dict_objects)
    if key_value == 'H':
        objectlist_H.append(dict_objects)
    if key_value == '1':
        objectlist_1.append(dict_objects)
    if key_value == '2':
        objectlist_2.append(dict_objects)
    if key_value == '3':
        objectlist_3.append(dict_objects)
    if key_value == '4':
        objectlist_4.append(dict_objects)
    if key_value == '5':
        objectlist_5.append(dict_objects)
    if key_value == '6':
        objectlist_6.append(dict_objects)
    if key_value == '7':
        objectlist_7.append(dict_objects)
    if key_value == '8':
        objectlist_8.append(dict_objects)

        # Check A & C and apply to B and solution set


# Code for problems using visual approach


def solve_by_horizontal_rotation(problem):
    angles = [45, 90, 135, 180, 225, 270, 315]
    for i in range(0, len(angles), 1):
        rotate_a = image_a.rotate(angles[i])
        diff = find_difference(rotate_a, image_b)
        if diff < 1:
            value_array = []
            rotate_c = image_c.rotate(angles[i])
            for j in range(1, 7):
                option_image = Image.open(problem.figures[str(j)].visualFilename)
                option_diff = find_difference(rotate_c, option_image)
                value_array.append(option_diff)
            if min(value_array) < 5:
                return value_array.index(min(value_array)) + 1

    return -1


def solve_by_vertical_rotation(problem):
    angles = [45, 90, 135, 180, 225, 270, 315]
    for i in range(0, len(angles), 1):
        rotate_a = image_a.rotate(angles[i])
        diff = find_difference(rotate_a, image_c)
        if diff < 3:
            value_array = []
            rotate_b = image_b.rotate(angles[i])
            for j in range(1, 7):
                option_image = Image.open(problem.figures[str(j)].visualFilename)
                option_diff = find_difference(rotate_b, option_image)
                value_array.append(option_diff)
            if min(value_array) < 5:
                return value_array.index(min(value_array)) + 1

    return -1


def solve_by_horizontal_reflection(problem, flag):
    try:
        if flag == 0:
            transpose_a = image_a.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            transpose_a = image_a.transpose(Image.FLIP_TOP_BOTTOM)

        diff = find_difference(transpose_a, image_b)

        if diff < 2:
            value_array = []
            if problem.problemType == '2x2':
                if flag == 0:
                    transpose_c = image_c.transpose(Image.FLIP_LEFT_RIGHT)
                else:
                    transpose_c = image_c.transpose(Image.FLIP_TOP_BOTTOM)
                for i in range(1, 7):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    option_diff = math.fabs(find_difference(transpose_c, option_image) - diff)
                    value_array.append(option_diff)

                if min(value_array) < 10:
                    return value_array.index(min(value_array)) + 1
                else:
                    return -1
        else:
            if flag == 1:
                return -1
            else:
                return solve_by_horizontal_reflection(problem, 1)

    except BaseException:
        pass

    return -1


def solve_by_vertical_reflection(problem, flag):
    try:
        if flag == 0:
            transpose_a = image_a.transpose(Image.FLIP_LEFT_RIGHT)
        else:
            transpose_a = image_a.transpose(Image.FLIP_TOP_BOTTOM)
        diff = find_difference(transpose_a, image_c)

        if diff < 2:
            value_array = []
            if flag == 0:
                transpose_b = image_b.transpose(Image.FLIP_LEFT_RIGHT)
            else:
                transpose_b = image_b.transpose(Image.FLIP_TOP_BOTTOM)
            for i in range(1, 7):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                option_diff = math.fabs(find_difference(transpose_b, option_image) - diff)
                value_array.append(option_diff)

            if min(value_array) < 10:
                return value_array.index(min(value_array)) + 1
            else:
                return -1
        else:
            if flag == 1:
                return -1
            else:
                return solve_by_vertical_reflection(problem, 1)

    except BaseException:
        pass

    return -1


def solve_by_and(problem):
    dim_a = get_bounding_box(image_a)
    side_length = dim_a[2] - dim_a[0]
    shape_length = side_length / 2
    area = (shape_length ** 2) * 1.5 * math.sqrt(3)
    pixel_a = get_pixel_count(image_b)
    diff = abs(pixel_a - area)

    value_array = []
    for i in range(1, 7):
        option_image = Image.open(problem.figures[str(i)].visualFilename)
        dim = get_bounding_box(option_image)
        side_length = dim[2] - dim[0]
        option_area = side_length ** 2
        pixel_count = get_pixel_count(option_image)
        option_diff = abs(pixel_count - option_area)
        value_array.append(option_diff)

    if min(value_array) < 500:
        return value_array.index(min(value_array)) + 1
    else:
        return -1


def solve_by_reflection(problem):
    try:
        transpose_a = image_a.transpose(Image.FLIP_LEFT_RIGHT)

        if problem.problemType == '2x2':
            diff = find_difference(transpose_a, image_b)
        else:
            diff = find_difference(transpose_a, image_c)

        if diff < 2:
            value_array = []
            if problem.problemType == '2x2':
                transpose_c = image_c.transpose(Image.FLIP_LEFT_RIGHT)
                for i in range(1, 7):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    option_diff = math.fabs(find_difference(transpose_c, option_image) - diff)
                    value_array.append(option_diff)

                if min(value_array) < 5:
                    return value_array.index(min(value_array)) + 1
                else:
                    return -1
            else:
                transpose_g = image_g.transpose(Image.FLIP_LEFT_RIGHT)
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    option_diff = math.fabs(find_difference(transpose_g, option_image) - diff)
                    value_array.append(option_diff)

                if min(value_array) < 5:
                    return value_array.index(min(value_array)) + 1
                else:
                    return -1
        else:
            return -1

    except BaseException:
        pass

    return -1


def solve_by_pixel_diff(problem):
    try:
        if problem.problemType == '2x2':
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_b))
            union = get_union(image_diff, image_a)
            diff = find_difference(union, image_b)
        else:
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_c))
            union = get_union(image_diff, image_a)
            # union.show()
            diff = find_difference(union, image_c)

        # print diff
        if diff <= 1:
            diff_score_array = []
            if problem.problemType == '2x2':
                if find_difference(image_diff, image_c) < 1:
                    return -1

                final_transform = get_union(image_diff, image_c)
                for i in range(1, 7):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = find_difference(final_transform, result_option)
                    diff_score_array.append(diff_score)
            else:
                if find_difference(image_diff, image_g) < 1:
                    return -1

                final_transform = get_union(image_diff, image_g)
                for i in range(1, 9):
                    result_option = Image.open(problem.figures[str(i)].visualFilename)
                    diff_score = find_difference(final_transform, result_option)
                    diff_score_array.append(diff_score)
            # print diff_score_array
            if min(diff_score_array) < 1.5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

    except BaseException:
        pass

    return -1


def solve_by_decrease(problem, flag):
    try:
        if flag == 0:
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_b))
        else:
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_c))

        diff_a = ImageChops.invert(ImageChops.difference(image_a, image_diff))

        if flag == 0:
            diff = find_difference(diff_a, image_b)
        else:
            diff = find_difference(diff_a, image_c)

        if diff <= 1:
            diff_score_array = []

            if flag == 0:
                if find_difference(image_diff, image_c) < 1:
                    return -1
                final_transform = ImageChops.invert(ImageChops.difference(image_c, image_diff))
            else:
                if find_difference(image_diff, image_b) < 1:
                    return -1
                final_transform = ImageChops.invert(ImageChops.difference(image_b, image_diff))

            for i in range(1, 7):
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(final_transform, result_option)
                diff_score_array.append(diff_score)

            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1
        else:
            if flag == 1:
                return -1
            else:
                return solve_by_decrease(problem, 1)

    except BaseException:
        pass

    return -1


def solve_by_offset(problem, flag):
    try:
        dim_a = get_bounding_box(image_a)
        dim_c = get_bounding_box(image_c)

        left_image = ImageChops.offset(image_a, dim_c[0] - dim_a[0], dim_c[1] - dim_a[1])
        right_image = ImageChops.offset(image_a, dim_c[2] - dim_a[2], dim_c[3] - dim_a[3])
        if flag == 0:
            left_intersect_a = get_union(left_image, image_a)
            final_intersect = get_union(left_intersect_a, right_image)
        elif flag == 1:
            final_intersect = get_union(left_image, right_image)
        else:
            return -1

        diff = find_difference(final_intersect, image_c)

        if diff <= 3:
            left_image_g = ImageChops.offset(image_g, dim_c[0] - dim_a[0], dim_c[1] - dim_a[1])
            right_image_g = ImageChops.offset(image_g, dim_c[2] - dim_a[2], dim_c[3] - dim_a[3])
            if flag == 0:
                left_intersect_g = get_union(left_image_g, image_g)
                final_transform = get_union(left_intersect_g, right_image_g)
            elif flag == 1:
                final_transform = get_union(left_image_g, right_image_g)
            else:
                return -1

            diff_score_array = []
            for i in range(1, 9):
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(final_transform, result_option)
                diff_score_array.append(diff_score)
            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1
        else:
            if flag == 1:
                return -1
            else:
                return solve_by_offset(problem, 1)

    except BaseException:
        pass

    return -1


def solve_by_general_scaling(problem):
    try:
        dim_a = get_bounding_box(image_a)
        dim_b = get_bounding_box(image_b)
        dim_c = get_bounding_box(image_c)
        dim_d = get_bounding_box(image_d)
        dim_e = get_bounding_box(image_e)
        dim_f = get_bounding_box(image_f)
        dim_g = get_bounding_box(image_g)
        dim_h = get_bounding_box(image_h)
        dim_answer = get_bounding_box(image_4)

        # calculate lengths of a,b & c
        length_a = dim_a[2] - dim_a[0]
        # width_a = dim_a[3] - dim_a[1]
        length_b = dim_b[2] - dim_b[0]
        # width_b = dim_b[3] - dim_b[1]
        length_c = dim_c[2] - dim_c[0]
        # width_c = dim_c[3] - dim_c[1]
        # print length_b/float(length_a), length_c/float(length_b)

        # calculate lengths of d,e & f
        length_d = dim_d[2] - dim_d[0]
        # width_d = dim_d[3] - dim_d[1]
        length_e = dim_e[2] - dim_e[0]
        # width_e = dim_e[3] - dim_e[1]
        length_f = dim_f[2] - dim_f[0]
        # width_f = dim_f[3] - dim_f[1]
        # print length_e/float(length_d), length_f/float(length_e)

        # calculate lengths of g,h & i
        length_g = dim_g[2] - dim_g[0]
        # width_g = dim_g[3] - dim_g[1]
        length_h = dim_h[2] - dim_h[0]
        # width_h = dim_h[3] - dim_h[1]
        length_answer = dim_answer[2] - dim_answer[0]
        # width_answer = dim_answer[3] - dim_answer[1]
        # print length_h/float(length_g), length_answer/float(length_h)

        # find scale tuple
        scalex_ba = length_b / float(length_a)
        # scale_y_ba = width_b / float(width_a)

        scalex_cb = length_c / float(length_b)
        # scale_y_cb = width_c / float(width_c)
        scale_tuple = int(scalex_cb * scalex_ba * image_a.size[0]), int(
            scalex_cb * scalex_ba * image_a.size[1])

        # find intersection between a & c
        diff_ac = ImageChops.invert(ImageChops.difference(image_a, image_c))
        ac_intersect_a = get_intersection(diff_ac, image_a)

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

        a_intersect_c = get_intersection(image_a, image_c)
        cropped_a = resized_a.crop(crop_box)

        final_transform = get_union(a_intersect_c, cropped_a)

        diff = find_difference(final_transform, image_c)

        # now apply the transformation to solution set and check
        scale_factor = length_c / float(length_a)
        result_scale = int(scale_factor * image_a.size[0]), int(scale_factor * image_a.size[1])
        # 97 percent similarity
        if diff < 3:
            g_intersect_a = ImageChops.difference(image_g, image_a)
            g_intersect_a = ImageChops.invert(g_intersect_a)
            ga_intersect_g = get_intersection(g_intersect_a, image_g)
            ga_intersect_g_resize = ga_intersect_g.resize(result_scale)

            scaled_width = ga_intersect_g_resize.size[0]
            scaled_length = ga_intersect_g_resize.size[1]

            left_margin = (scaled_width - image_a.size[0]) / 2
            right_margin = scaled_width - left_margin
            upper_margin = (scaled_length - image_a.size[1]) / 2
            lower_margin = scaled_length - upper_margin
            crop_box = left_margin, upper_margin, right_margin, lower_margin

            cropped_g = ga_intersect_g_resize.crop(crop_box)
            result_final_transform = get_union(a_intersect_c, cropped_g)

            diff_score_array = []
            for i in range(1, 9):
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(result_final_transform, result_option)
                diff_score_array.append(diff_score)

            if min(diff_score_array) < 7:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

    except BaseException:
        pass

    return -1


def solve_by_special_scaling(problem):
    try:
        dim_a = get_bounding_box(image_a)
        dim_b = get_bounding_box(image_b)
        dim_c = get_bounding_box(image_c)
        dim_d = get_bounding_box(image_d)
        dim_e = get_bounding_box(image_e)
        dim_f = get_bounding_box(image_f)
        dim_g = get_bounding_box(image_g)
        dim_h = get_bounding_box(image_h)
        dim_answer = get_bounding_box(image_4)

        # calculate lengths of a,b & c
        length_a = dim_a[2] - dim_a[0]
        # width_a = dim_a[3] - dim_a[1]
        length_b = dim_b[2] - dim_b[0]
        # width_b = dim_b[3] - dim_b[1]
        length_c = dim_c[2] - dim_c[0]
        # width_c = dim_c[3] - dim_c[1]
        # print length_b/float(length_a), length_c/float(length_b)

        # find scale tuple
        scalex_ba = length_b / float(length_a)
        # scale_y_ba = width_b / float(width_a)

        scalex_cb = length_c / float(length_b)
        # scale_y_cb = width_c / float(width_c)
        scale_tuple = int(scalex_cb * scalex_ba * image_a.size[0]), int(
            scalex_cb * scalex_ba * image_a.size[1])

        # find intersection between a & c
        diff_ac = ImageChops.invert(ImageChops.difference(image_a, image_c))
        ac_intersect_a = get_intersection(diff_ac, image_a)

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

        a_intersect_c = get_intersection(image_a, image_c)
        cropped_a = resized_a.crop(crop_box)

        final_transform = get_union(a_intersect_c, cropped_a)

        diff = find_difference(final_transform, image_c)

        # now apply the transformation to solution set and check
        result_scale = int(1.45 * image_a.size[0]), int(1.45 * image_a.size[1])
        # 94 percent similarity
        if diff < 6:
            g_intersect_a = ImageChops.difference(image_g, image_a)
            g_intersect_a = ImageChops.invert(g_intersect_a)
            ga_intersect_g = get_intersection(g_intersect_a, image_g)
            ga_intersect_g_resize = ga_intersect_g.resize(result_scale)

            scaled_width = ga_intersect_g_resize.size[0]
            scaled_length = ga_intersect_g_resize.size[1]

            left_margin = (scaled_width - image_a.size[0]) / 2
            right_margin = scaled_width - left_margin
            upper_margin = (scaled_length - image_a.size[1]) / 2
            lower_margin = scaled_length - upper_margin
            crop_box = left_margin, upper_margin, right_margin, lower_margin

            cropped_g = ga_intersect_g_resize.crop(crop_box)
            result_final_transform = get_union(a_intersect_c, cropped_g)

            diff_score_array = []
            for i in range(1, 9):
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(result_final_transform, result_option)
                diff_score_array.append(diff_score)

            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

    except BaseException:
        pass

    return -1


def solve_by_rolling(problem):
    try:
        width, length = image_a.size[0], image_a.size[1]

        left_half = image_a.crop((0, 0, width / 2, length))
        right_half = image_a.crop((width / 2, 0, width, length))

        final_image = image_a.copy()
        final_image.paste(right_half, (5, 0, width / 2 + 5, length))
        final_image.paste(left_half, (width / 2 - 5, 0, width - 5, length))

        diff = find_difference(final_image, image_c)

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
                diff_score = find_difference(final_transform, result_option)
                diff_score_array.append(diff_score)

            if min(diff_score_array) < 5:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1

        return -1
    except BaseException:
        pass

    return -1


def solve_by_rolling_transform(problem):
    try:
        diff_list = []
        match_list = []
        diff_list.append(find_difference(image_a, image_g))
        diff_list.append(find_difference(image_b, image_g))
        diff_list.append(find_difference(image_c, image_g))

        for index in range(len(diff_list)):
            if diff_list[index] < 1:
                match_list.append(index)

        del diff_list[:]

        diff_list.append(find_difference(image_a, image_h))
        diff_list.append(find_difference(image_b, image_h))
        diff_list.append(find_difference(image_c, image_h))

        for index in range(len(diff_list)):
            if diff_list[index] < 1:
                match_list.append(index)

        if match_list[0] == 0 and match_list[1] == 1:
            sol_img = image_c
        elif match_list[0] == 0 and match_list[1] == 2:
            sol_img = image_b
        else:
            sol_img = image_a

        if diff_list[match_list[1]] < 1:
            diff_score_array = []
            for i in range(1, 9):
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_img, result_option)
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


def solve_by_special_rolltrans(problem):
    try:
        intersect = get_intersection(image_a, image_c)
        a_new = ImageChops.invert(ImageChops.difference(image_a, intersect))
        b_new = ImageChops.invert(ImageChops.difference(image_b, intersect))
        c_new = ImageChops.invert(ImageChops.difference(image_c, intersect))

        sol_intersect = get_intersection(image_g, image_h)
        g_new = ImageChops.invert(ImageChops.difference(image_g, sol_intersect))
        h_new = ImageChops.invert(ImageChops.difference(image_h, sol_intersect))

        diff_list = []
        match_list = []
        diff_list.append(find_difference(a_new, g_new))
        diff_list.append(find_difference(image_b, g_new))
        diff_list.append(find_difference(image_c, g_new))

        for index in range(len(diff_list)):
            if diff_list[index] < 3:
                match_list.append(index)

        del diff_list[:]

        diff_list.append(find_difference(a_new, h_new))
        diff_list.append(find_difference(b_new, h_new))
        diff_list.append(find_difference(c_new, h_new))

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
                diff_score = find_difference(sol_img, sol_new)
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


def solve_by_special_diff(problem):
    try:
        a_diff_c = ImageChops.invert(ImageChops.difference(image_a, image_c))
        diff_score_array = []
        for i in range(1, 9):
            result_option = Image.open(problem.figures[str(i)].visualFilename)
            g_diff_sol = ImageChops.invert(ImageChops.difference(image_g, result_option))
            diff_score = find_difference(a_diff_c, g_diff_sol)
            diff_score_array.append(diff_score)

        if min(diff_score_array) < 3.0:
            return diff_score_array.index(min(diff_score_array)) + 1
        else:
            return -1
    except BaseException:
        pass

    return -1


def solve_by_inner_extract(problem):
    try:
        a_union_b = get_union(image_a, image_b)
        row_a = get_union(a_union_b, image_c)

        d_union_e = get_union(image_d, image_e)
        row_b = get_union(d_union_e, image_f)

        diff = ImageChops.invert(ImageChops.difference(row_a, row_b))

        g_union_h = get_union(image_g, image_h)
        diff_score_array = []
        for i in range(1, 9):
            if i == 1:
                result_option = Image.open(problem.figures[str(i)].visualFilename)
                row_c = get_union(g_union_h, result_option)
                sol_diff = ImageChops.invert(ImageChops.difference(row_b, row_c))
                temp_img = get_union(diff, sol_diff)
                a_new = ImageChops.invert(ImageChops.difference(image_a, temp_img))
                b_new = ImageChops.invert(ImageChops.difference(image_b, temp_img))
                c_new = ImageChops.invert(ImageChops.difference(image_c, temp_img))

                diff_list = []
                match_list = []
                diff_list.append(find_difference(a_new, image_g))
                diff_list.append(find_difference(b_new, image_g))
                diff_list.append(find_difference(c_new, image_g))

                for index in range(len(diff_list)):
                    if diff_list[index] < 2.5:
                        match_list.append(index)

                del diff_list[:]

                diff_list.append(find_difference(a_new, image_h))
                diff_list.append(find_difference(b_new, image_h))
                diff_list.append(find_difference(c_new, image_h))

                for index in range(len(diff_list)):
                    if diff_list[index] < 2.5:
                        match_list.append(index)

                if match_list[0] == 0 and match_list[1] == 1:
                    sol_img = c_new
                elif match_list[0] == 0 and match_list[1] == 2:
                    sol_img = b_new
                else:
                    sol_img = a_new

                if diff_list[match_list[1]] < 2.5:
                    diff_score = find_difference(sol_img, result_option)
                    diff_score_array.append(diff_score)
                    return diff_score_array.index(min(diff_score_array)) + 1
                else:
                    return -1

        return -1
    except BaseException:
        pass

    return -1


def solve_by_misc(problem):
    try:
        c_pixel = get_pixel_count(image_c)
        f_pixel = get_pixel_count(image_f)
        g_pixel = get_pixel_count(image_g)
        h_pixel = get_pixel_count(image_h)

        if c_pixel == -1 or f_pixel == -1 or g_pixel == -1 or h_pixel == -1:
            return -1

        diff1 = c_pixel - f_pixel
        diff2 = g_pixel - h_pixel

        mean_diff = (diff1 + diff2) / 2
        mean_pixel = (f_pixel + h_pixel) / 2

        pixel_array = []

        for i in range(1, 9):
            option_image = Image.open(problem.figures[str(i)].visualFilename)
            pixel_count = get_pixel_count(option_image)
            pixel_array.append(abs(mean_pixel - pixel_count - mean_diff))

        if min(pixel_array) < 200:
            return pixel_array.index(min(pixel_array)) + 1
        else:
            return -1

    except BaseException:
        pass

    return -1


def solve_by_union(problem):
    try:
        a_count = get_pixel_count(image_a)
        b_count = get_pixel_count(image_b)
        c_count = get_pixel_count(image_c)
        count_mean = (a_count + b_count + c_count) / 3
        # print c_count
        # print count_mean
        a_union_b = get_union(image_a, image_b)
        # a_union_b.show()
        diff_1 = find_difference(a_union_b, image_c)

        d_union_e = get_union(image_d, image_e)
        diff_2 = find_difference(d_union_e, image_f)

        g_union_h = get_union(image_g, image_h)

        diff_score_array = []
        # print diff_1, diff_2
        if diff_1 < 5 and diff_2 < 7 and count_mean > 1000 and c_count > 1300:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(g_union_h, option_image)
                diff_score_array.append(diff_score)

            # print diff_score_array
            if min(diff_score_array) < 6:
                return diff_score_array.index(min(diff_score_array)) + 1
            else:
                return -1
        else:
            return -1
        return -1

    except BaseException:
        pass

    return -1


def solve_by_shift_diff(problem):
    try:
        dim_a = get_bounding_box(image_a)
        width_a = dim_a[2] - dim_a[0]
        offset_b = ImageChops.offset(image_b, -width_a/3, 0)
        image_diff_1 = ImageChops.invert(ImageChops.difference(image_a, offset_b))
        row_a_offset = ImageChops.offset(image_diff_1, int(-width_a/6), 0)
        diff = find_difference(row_a_offset, image_c)

        dim_g = get_bounding_box(image_g)
        width_g = dim_g[2] - dim_g[0]
        offset_h = ImageChops.offset(image_h, -width_g/3, 0)
        image_diff_2 = ImageChops.invert(ImageChops.difference(image_g, offset_h))
        row_c_offset = ImageChops.offset(image_diff_2, int(-width_g/6), 0)

        diff_score_array = []

        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(row_c_offset, option_image)
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


def solve_by_simple_diff(problem):
    # TODO: fix 7 and 8 for Set E
    try:
        image_diff_1 = ImageChops.invert(ImageChops.difference(image_a, image_b))
        diff = find_difference(image_diff_1, image_c)
        image_diff_2 = ImageChops.invert(ImageChops.difference(image_g, image_h))

        diff_score_array = []
        if diff < 2:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(image_diff_2, option_image)
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


def solve_by_intersection(problem):
    try:
        a_union_b = get_intersection(image_a, image_b)
        diff = find_difference(a_union_b, image_c)

        g_union_h = get_intersection(image_g, image_h)

        diff_score_array = []

        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(g_union_h, option_image)
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


def solve_by_reverse_diff(problem):
    # TODO: Generalize by adding center aligning code
    try:
        dim_a = get_bounding_box(image_a)
        width_a = dim_a[2] - dim_a[0]
        dim_b = get_bounding_box(image_b)
        width_b = dim_b[2] - dim_b[0]
        # print width_a, width_b
        transpose_b = image_b.transpose(Image.FLIP_TOP_BOTTOM)
        offset_b = ImageChops.offset(transpose_b, int(-width_a/3), 0)
        image_diff_1 = ImageChops.invert(ImageChops.difference(image_a, offset_b))
        c_new = ImageChops.offset(image_diff_1, int(-width_a/6), 0)
        diff_1 = find_difference(image_c, c_new)

        dim_d = get_bounding_box(image_d)
        width_d = dim_a[2] - dim_d[0]
        dim_e = get_bounding_box(image_e)
        width_e = dim_e[2] - dim_e[0]
        # print width_d, width_e
        transpose_e = image_e.transpose(Image.FLIP_TOP_BOTTOM)
        offset_e = ImageChops.offset(transpose_e, int(-width_d/6), 0)
        image_diff_2 = ImageChops.invert(ImageChops.difference(image_d, offset_e))
        f_new = ImageChops.offset(image_diff_2, int(-width_d/3), 0)
        diff_2 = find_difference(image_f, f_new)

        dim_g = get_bounding_box(image_g)
        width_g = dim_g[2] - dim_g[0]
        dim_h = get_bounding_box(image_h)
        width_h = dim_h[2] - dim_h[0]
        # print width_g, width_h
        transpose_h = image_h.transpose(Image.FLIP_TOP_BOTTOM)
        offset_h = ImageChops.offset(transpose_h, int(-width_h/2), 0)
        image_diff_3 = ImageChops.invert(ImageChops.difference(image_g, offset_h))
        sol_new = ImageChops.offset(image_diff_3, int(-width_h/2), 0)

        diff_score_array = []
        if diff_1 < 1 or diff_2 < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_new, option_image)
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


def solve_by_crop_union_a(problem):
    try:
        width_a = image_a.size[0]
        height_a = image_a.size[1]

        width_b = image_b.size[0]
        height_b = image_b.size[1]

        crop_box_a = 0, 0, width_a, height_a/2
        crop_box_b = 0, height_b/2, width_b, height_b

        cropped_a = image_a.crop(crop_box_a)
        cropped_b = image_b.crop(crop_box_b)

        c_new = image_a.copy()
        c_new.paste(cropped_a, (0, 0, width_a, height_a/2))
        c_new.paste(cropped_b, (0, height_b/2, width_b, height_b))

        diff = find_difference(image_c, c_new)

        width_g = image_g.size[0]
        height_g = image_g.size[1]

        width_h = image_h.size[0]
        height_h = image_h.size[1]

        crop_box_g = 0, 0, width_g, height_g/2
        crop_box_h = 0, height_h/2, width_h, height_h

        cropped_g = image_g.crop(crop_box_g)
        cropped_h = image_h.crop(crop_box_h)

        sol_new = image_g.copy()
        sol_new.paste(cropped_g, (0, 0, width_g, height_g/2))
        sol_new.paste(cropped_h, (0, height_h/2, width_h, height_h))

        diff_score_array = []
        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_new, option_image)
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


def solve_by_crop_union_b(problem):
    try:
        width_a = image_a.size[0]
        height_a = image_a.size[1]

        width_b = image_b.size[0]
        height_b = image_b.size[1]

        crop_box_a = 0, height_a/2, width_a, height_a
        crop_box_b = 0, 0, width_b, height_b/2

        cropped_a = image_a.crop(crop_box_a)
        cropped_b = image_b.crop(crop_box_b)

        c_new = image_a.copy()
        c_new.paste(cropped_a, (0, height_a/2, width_a, height_a))
        c_new.paste(cropped_b, (0, 0, width_b, height_b/2))

        diff = find_difference(image_c, c_new)

        width_g = image_g.size[0]
        height_g = image_g.size[1]

        width_h = image_h.size[0]
        height_h = image_h.size[1]

        crop_box_g = 0, height_g/2, width_g, height_g
        crop_box_h = 0, 0, width_h, height_h/2

        cropped_g = image_g.crop(crop_box_g)
        cropped_h = image_h.crop(crop_box_h)

        sol_new = image_g.copy()
        sol_new.paste(cropped_g, (0, height_g/2, width_g, height_g))
        sol_new.paste(cropped_h, (0, 0, width_h, height_h/2))

        diff_score_array = []
        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_new, option_image)
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


def solve_by_crop_union_c(problem):
    try:
        width_a = image_a.size[0]
        height_a = image_a.size[1]

        width_b = image_b.size[0]
        height_b = image_b.size[1]

        crop_box_a = 0, 0, width_a/2, height_a
        crop_box_b = width_b/2, 0, width_b, height_b

        cropped_a = image_a.crop(crop_box_a)
        cropped_b = image_b.crop(crop_box_b)

        c_new = image_a.copy()
        c_new.paste(cropped_a, (0, 0, width_a/2, height_a))
        c_new.paste(cropped_b, (width_b/2, 0, width_b, height_b))

        diff = find_difference(image_c, c_new)

        width_g = image_g.size[0]
        height_g = image_g.size[1]

        width_h = image_h.size[0]
        height_h = image_h.size[1]

        crop_box_g = 0, 0, width_g/2, height_g
        crop_box_h = width_h/2, 0, width_h, height_h

        cropped_g = image_g.crop(crop_box_g)
        cropped_h = image_h.crop(crop_box_h)

        sol_new = image_g.copy()
        sol_new.paste(cropped_g, (0, 0, width_g/2, height_g))
        sol_new.paste(cropped_h, (width_h/2, 0, width_h, height_h))

        diff_score_array = []
        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_new, option_image)
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


def solve_by_crop_union_d(problem):
    try:
        width_a = image_a.size[0]
        height_a = image_a.size[1]

        width_b = image_b.size[0]
        height_b = image_b.size[1]

        crop_box_a = width_a/2, 0, width_a, height_a
        crop_box_b = 0, 0, width_b/2, height_b

        cropped_a = image_a.crop(crop_box_a)
        cropped_b = image_b.crop(crop_box_b)

        c_new = image_a.copy()
        c_new.paste(cropped_a, (width_a/2, 0, width_a, height_a))
        c_new.paste(cropped_b, (0, 0, width_b/2, height_b))

        diff = find_difference(image_c, c_new)

        width_g = image_g.size[0]
        height_g = image_g.size[1]

        width_h = image_h.size[0]
        height_h = image_h.size[1]

        crop_box_g = width_g/2, 0, width_g, height_g
        crop_box_h = 0, 0, width_h/2, height_h

        cropped_g = image_g.crop(crop_box_g)
        cropped_h = image_h.crop(crop_box_h)

        sol_new = image_g.copy()
        sol_new.paste(cropped_g, (width_g/2, 0, width_g, height_g))
        sol_new.paste(cropped_h, (0, 0, width_h/2, height_h))

        diff_score_array = []
        if diff < 1:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_new, option_image)
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


def solve_by_extract_roll(problem):
    try:
        rotated_square = get_intersection(image_b, image_f)
        four_squares = get_image_difference(rotated_square, image_f)
        rotated_lines = get_image_difference(rotated_square, image_b)
        circle = get_intersection(image_c, image_d)
        square = get_image_difference(four_squares, image_a)
        straight_lines = get_image_difference(circle, image_c)

        shape_array = [square, rotated_square, circle, four_squares, rotated_lines, straight_lines]

        diff_array = []
        index_array = []

        for i in range(len(shape_array)):
            for j in range(i+1, len(shape_array), 1):
                temp_image = get_union(shape_array[i], shape_array[j])
                diff = find_difference(temp_image, image_g)
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
            for j in range(i+1, len(shape_array), 1):
                temp_image = get_union(shape_array[i], shape_array[j])
                diff = find_difference(temp_image, image_h)
                diff_array.append(diff)
                index_array.append((i, j))

        diff_2 = min(diff_array)
        index_c, index_d = index_array[diff_array.index(min(diff_array))]

        shape_c = shape_array[index_c]
        shape_d = shape_array[index_d]
        shape_array.remove(shape_c)
        shape_array.remove(shape_d)

        sol_new = get_union(shape_array[0], shape_array[1])

        diff_score_array = []

        if diff_1 < 6 and diff_2 < 6:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_new, option_image)
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


def solve_by_special_approach(problem):
    try:
        a_pixel = get_pixel_count(image_a)
        f_pixel = get_pixel_count(image_f)
        h_pixel = get_pixel_count(image_h)
        diff_1 = abs((f_pixel - a_pixel) - (h_pixel - f_pixel))

        e_pixel = get_pixel_count(image_e)
        g_pixel = get_pixel_count(image_g)
        c_pixel = get_pixel_count(image_c)
        diff_2 = abs((g_pixel - e_pixel) - (c_pixel - g_pixel))

        b_pixel = get_pixel_count(image_b)
        d_pixel = get_pixel_count(image_d)
        min_count = min(b_pixel, d_pixel)
        max_count = max(b_pixel, d_pixel)
        pixel_diff = d_pixel - b_pixel

        lower_count = min_count - pixel_diff
        upper_count = max_count + pixel_diff

        lower_array = []
        upper_array = []

        if diff_1 < 150 and diff_2 < 150:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                pixel_count = get_pixel_count(option_image)
                lower_array.append(abs(pixel_count - lower_count))
                upper_array.append(abs(pixel_count - upper_count))

            if min(lower_array) <= min(upper_array):
                if min(lower_array) < 100:
                    return lower_array.index(min(lower_array)) + 1
                else:
                    return -1
            else:
                return upper_array.index(min(upper_array)) + 1

        else:
            return -1

    except BaseException:
        pass

    return -1


def solve_by_diagonal_approach(problem):
    try:
        plus = get_intersection(image_f, image_h)
        circle = get_image_difference(plus, image_f)
        four_dots = get_image_difference(image_a, plus)
        square = get_image_difference(circle, image_b)
        bigger_square = get_image_difference(square, image_d)
        heart = get_image_difference(four_dots, image_e)

        diff_1 = find_difference(get_union(plus, four_dots), image_a)
        diff_2 = find_difference(get_union(heart, four_dots), image_e)
        sol_image = get_union(square, four_dots)

        diff_score_array = []
        if diff_1 < 2 and diff_2 < 2:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_image, option_image)
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


def solve_by_alternate_fill(problem):
    try:
        dim_c = get_bounding_box(image_c)
        width_c = dim_c[2] - dim_c[0]

        dim_g = get_bounding_box(image_g)
        width_g = dim_g[2] - dim_g[0]

        scale = width_c/float(width_g)

        scale_tuple = int(scale * image_b.size[0]), int(scale * image_b.size[1])
        resized_g = image_g.resize(scale_tuple)
        resized_b = image_b.resize(scale_tuple)
        scaled_width, scaled_height = resized_g.size

        # find the crop box tuple
        left_margin = (scaled_width - image_b.size[0]) / 2
        right_margin = scaled_width - left_margin
        upper_margin = (scaled_height - image_a.size[1]) / 2
        lower_margin = scaled_height - upper_margin
        crop_box = left_margin, upper_margin, right_margin, lower_margin

        cropped_g = resized_g.crop(crop_box)
        diff = find_difference(cropped_g, get_image_difference(image_c, image_e))

        cropped_b = resized_b.crop(crop_box)
        sol_image= get_image_difference(cropped_b, image_d)

        diff_score_array = []
        if diff < 4:
            for i in range(1, 9):
                option_image = Image.open(problem.figures[str(i)].visualFilename)
                diff_score = find_difference(sol_image, option_image)
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
# Utilities Methods


def get_bounding_box(image):
    # convert to grayscale and invert
    image_bw = image.convert(mode='L')
    image_inv = ImageChops.invert(image_bw)

    return image_inv.getbbox()


def get_pixel_count(image):
    try:
        # make the image black & white and then count the black pixels
        image_bw = image.convert(mode='L')
        image_loaded = image_bw.load()
        pixel_count = 0
        for i in range(0, image.size[0]):
            for j in range(0, image.size[1]):
                pixel_val = image_loaded[i, j]
                if pixel_val == 0:
                    pixel_count += 1

        return pixel_count
    except BaseException:
        return -1


def get_image_difference(first_image, second_image):
    return ImageChops.invert(ImageChops.difference(first_image, second_image))


def get_intersection(first_image, second_image):
    return ImageChops.lighter(first_image, second_image)


def get_union(first_image, second_image):
    return ImageChops.darker(first_image, second_image)


def get_xor(first_image, second_image):
    first_expression = get_intersection(first_image, ImageChops.invert(second_image))
    second_expression = get_intersection(ImageChops.invert(first_image), image_b)
    return get_union(first_expression, second_expression)


def find_difference(first_image, second_image):
    # Reference: http://rosettacode.org/wiki/Percentage_difference_between_images#Python

    pairs = izip(first_image.getdata(), second_image.getdata())
    if len(first_image.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    n_components = first_image.size[0] * first_image.size[1] * 3

    return (dif / 255.0 * 100) / n_components


# Code for Solving only 2x2 problems using verbal approach


class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an integer representing its
    # answer to the question: "1", "2", "3", "4", "5", or "6". These integers
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName() (as Strings).
    #
    # In addition to returning your answer at the end of the method, your Agent
    # may also call problem.checkAnswer(int givenAnswer). The parameter
    # passed to checkAnswer should be your Agent's current guess for the
    # problem; checkAnswer will return the correct answer to the problem. This
    # allows your Agent to check its answer. Note, however, that after your
    # agent has called checkAnswer, it will *not* be able to change its answer.
    # checkAnswer is used to allow your Agent to learn from its incorrect
    # answers; however, your Agent cannot change the answer to a question it
    # has already answered.
    #
    # If your Agent calls checkAnswer during execution of Solve, the answer it
    # returns will be ignored; otherwise, the answer returned at the end of
    # Solve will be taken as your Agent's answer to this problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self, problem):
        init_objects()
        print problem.name
        print "Attempting to solve " + problem.name + " using visual approach"
        if problem.problemType == '2x2':
            prob = problem.figures
            for key, value in sorted(prob.iteritems()):
                figure = prob[key]
                object_list = figure.objects
                parse_problem(key, object_list)
                file_name = figure.visualFilename
                load_image(key, file_name)
            i = solve_by_horizontal_reflection(problem, 0)
            if i != -1:
                return i
            i = solve_by_vertical_reflection(problem, 0)
            if i != -1:
                return i
            i = solve_by_horizontal_rotation(problem)
            if i != -1:
                return i
            i = solve_by_vertical_rotation(problem)
            if i != -1:
                return i
            # i = solve_by_pixel_diff(problem)
            # if i != -1:
            #     print 'Problem Solved' + "\n"
            #     return i
            i = solve_by_decrease(problem, 0)
            if i != -1:
                return i
            i = solve_by_and(problem)
            if i != -1:
                return i
            else:
                return i
        elif problem.problemType == '3x3':
            # TODO:write code for vertical symmetry
            prob = problem.figures
            for key, value in sorted(prob.iteritems()):
                figure = prob[key]
                file_name = figure.visualFilename
                load_image(key, file_name)
            if 'C-' in problem.name:
                i = solve_by_reflection(problem)
                if i != -1:
                    return i
                i = solve_by_pixel_diff(problem)
                if i != -1:
                    return i
                i = solve_by_offset(problem, 0)
                if i != -1:
                    return i
                i = solve_by_general_scaling(problem)
                if i != -1:
                    return i
                i = solve_by_special_scaling(problem)
                if i != -1:
                    return i
                i = solve_by_rolling(problem)
                if i != -1:
                    return i
                i = solve_by_misc(problem)
                if i != -1:
                    return i
                else:
                    return i

            elif 'D-' in problem.name:
                i = solve_by_reflection(problem)
                if i != -1:
                    return i
                i = solve_by_offset(problem, 0)
                if i != -1:
                    return i
                i = solve_by_general_scaling(problem)
                if i != -1:
                    return i
                i = solve_by_rolling(problem)
                if i != -1:
                    return i
                i = solve_by_rolling_transform(problem)
                if i != -1:
                    return i
                i = solve_by_inner_extract(problem)
                if i != -1:
                    return i
                i = solve_by_special_rolltrans(problem)
                if i != -1:
                    return i
                i = solve_by_special_diff(problem)
                if i != -1:
                    return i
                i = solve_by_extract_roll(problem)
                if i != -1:
                    return i
                i = solve_by_special_approach(problem)
                if i != -1:
                    return i
                i = solve_by_diagonal_approach(problem)
                if i != -1:
                    return i
                # i = solve_by_alternate_fill(problem)
                # if i != -1:
                #     return i
                # i = solve_by_misc(problem)
                # if i != -1:
                #     return i
                else:
                    print "Hmmm, this looks tricky. I would skip this problem." + "\n"
                    return i
            else:
                i = solve_by_reflection(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                # i = solve_by_pixel_diff(problem)
                # if i != -1:
                #     print 'here'
                #     print 'Problem Solved' + "\n"
                #     return i
                i = solve_by_offset(problem, 0)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_rolling(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_union(problem)
                if i != -1:
                    # print 'here'
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_shift_diff(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_simple_diff(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_intersection(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_reverse_diff(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_crop_union_a(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_crop_union_b(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_crop_union_c(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                i = solve_by_crop_union_d(problem)
                if i != -1:
                    print 'Problem Solved' + "\n"
                    return i
                else:
                    print "Hmmm, this looks tricky. I would skip this problem." + "\n"
                    return i
        else:
            print "My creator has not equipped me to handle such problems yet. I would skip this problem." + "\n"
            return -1