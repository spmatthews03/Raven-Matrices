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

from PIL import Image, ImageChops
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
    shape_length = side_length/2
    area = (shape_length**2) * 1.5 * math.sqrt(3)
    pixel_a = get_pixel_count(image_b)
    diff = abs(pixel_a - area)

    value_array = []
    for i in range(1, 7):
        option_image = Image.open(problem.figures[str(i)].visualFilename)
        dim = get_bounding_box(option_image)
        side_length = dim[2] - dim[0]
        option_area = side_length**2
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

                return value_array.index(min(value_array)) + 1
            else:
                transpose_g = image_g.transpose(Image.FLIP_LEFT_RIGHT)
                for i in range(1, 9):
                    option_image = Image.open(problem.figures[str(i)].visualFilename)
                    option_diff = math.fabs(find_difference(transpose_g, option_image) - diff)
                    value_array.append(option_diff)

                return value_array.index(min(value_array)) + 1
        else:
            return -1

    except BaseException:
        pass

    return -1

    # TODO: normal scaling


def solve_by_pixel_diff(problem):
    try:
        if problem.problemType == '2x2':
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_b))
            union = get_union(image_diff, image_a)
            diff = find_difference(union, image_b)
        else:
            image_diff = ImageChops.invert(ImageChops.difference(image_a, image_c))
            union = get_union(image_diff, image_a)
            diff = find_difference(union, image_c)

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
            return diff_score_array.index(min(diff_score_array)) + 1
        else:
            if flag == 1:
                return -1
            else:
                return solve_by_offset(problem, 1)

    except BaseException:
        pass

    return -1


def solve_by_special_scaling(problem):
    try:
        dim_a = get_bounding_box(image_a)
        dim_b = get_bounding_box(image_b)
        dim_c = get_bounding_box(image_c)

        # calculate lengths of a,b & c
        length_a = dim_a[2] - dim_a[0]
        # width_a = dim_a[3] - dim_a[1]
        length_b = dim_b[2] - dim_b[0]
        # width_b = dim_b[3] - dim_b[1]
        length_c = dim_c[2] - dim_c[0]
        # width_c = dim_c[3] - dim_c[1]

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

            return diff_score_array.index(min(diff_score_array)) + 1

    except BaseException:
        pass

    return -1

    # TODO: normal scaling


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

            return diff_score_array.index(min(diff_score_array)) + 1

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


def get_intersection(first_image, second_image):
    return ImageChops.lighter(first_image, second_image)


def get_union(first_image, second_image):
    return ImageChops.darker(first_image, second_image)


def find_difference(first_image, second_image):
    # Reference: http://rosettacode.org/wiki/Percentage_difference_between_images#Python

    pairs = zip(first_image.getdata(), second_image.getdata())
    if len(first_image.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    n_components = first_image.size[0] * first_image.size[1] * 3

    return (dif / 255.0 * 100) / n_components

# Code for Solving only 2x2 problems using verbal approach


def map_vertically_basic():
    rule_diff = []
    temprule_diff = []
    ref_rules = {'shape': [],  #
                 'size': ['very small', 'small', 'medium', 'large', 'very large', 'huge'],  # order matters
                 'fill': ['no', 'yes'],
                 'angle': [0, 45, 90, 135, 180, 225, 270, 315],  # order matters
                 'inside': [],
                 'above': [],
                 'alignment': ['bottom-left', 'bottom-right', 'top-left', 'top-right'],
                 'overlaps': [],
                 'transform': ['add', 'remove']
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6]

    rule_length = max(len(objectlist_A), len(objectlist_C))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': ''})

    objectlist_A.sort(lambda x, y: cmp(len(x), len(y)))
    objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_C in objectlist_C:
                    for keyC, valueC in iter(sorted(dict_C.items())):
                        if keyC != 'name':
                            if valueA not in ref_rules[keyA]:
                                if keyA != 'inside' and keyA != 'above':
                                    ref_rules[keyA].append(valueA)
                            if valueC not in ref_rules[keyC]:
                                if keyC != 'inside' and keyC != 'above':
                                    ref_rules[keyC].append(valueC)
                            if keyA == keyC and i == j:
                                if keyA == 'inside' or keyA == 'above':
                                    rule_diff[j][keyA] = len(valueA) - len(valueC)
                                else:
                                    rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[keyC].index(valueC)
                    j += 1
        i += 1

    rule_add_count = -1
    rule_remove_count = -1
    if i > j:
        rule_remove_count = i - j
        for itr in range(j, i):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'remove'

    if i < j:
        rule_add_count = j - i
        for itr in range(i, j):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'add'

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        del temprule_diff[:]
        temprule_length = max(len(objectlist_B), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': ''})

        # number_list.sort(lambda x, y: cmp(len(x), len(y)))
        # objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

        i = 0
        for dict_B in objectlist_B:
            for keyB, valueB in iter(sorted(dict_B.items())):
                if keyB != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueB not in ref_rules[keyB]:
                                    if keyB != 'inside' and keyB != 'above':
                                        ref_rules[keyB].append(valueB)
                                if valueN not in ref_rules[keyN]:
                                    if keyN != 'inside' and keyN != 'above':
                                        ref_rules[keyN].append(valueN)
                                if keyB == keyN and i == j:
                                    if keyB == 'inside' or keyB == 'above':
                                        temprule_diff[j][keyB] = len(valueB) - len(valueN)
                                    else:
                                        temprule_diff[j][keyB] = ref_rules[keyB].index(valueB) - ref_rules[keyN].index(
                                            valueN)
                        j += 1
            i += 1

        temprule_add_count = -1
        temprule_remove_count = -1
        if i > j:
            temprule_remove_count = i - j
            for itr in range(j, i):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'remove'

        if i < j:
            temprule_add_count = j - i
            for itr in range(i, j):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'add'

        match = True
        for index in range(min(len(rule_diff), len(temprule_diff))):
            if rule_diff[index]['transform'] == 'add' or rule_diff[index]['transform'] == 'remove' \
                    or temprule_diff[index]['transform'] == 'add' or temprule_diff[index]['transform'] == 'remove':
                break
            if cmp(rule_diff[index], temprule_diff[index]) != 0:
                match = False
                break
        if match and rule_add_count == temprule_add_count and rule_remove_count == temprule_remove_count:
            return solution_index

    return -1


def find_solution_basic():
    rule_diff = []
    temprule_diff = []
    ref_rules = {'shape': [],  #
                 'size': ['very small', 'small', 'medium', 'large', 'very large', 'huge'],  # order matters
                 'fill': ['no', 'yes'],
                 'angle': [0, 45, 90, 135, 180, 225, 270, 315],  # order matters
                 'inside': [],
                 'above': [],
                 'alignment': ['bottom-left', 'bottom-right', 'top-left', 'top-right'],
                 'overlaps': [],
                 'transform': ['add', 'remove']
                 }

    solution_list = [objectlist_1, objectlist_2, objectlist_3, objectlist_4, objectlist_5, objectlist_6]

    rule_length = max(len(objectlist_A), len(objectlist_B))

    for i in range(rule_length):
        rule_diff.append({'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                          'overlaps': '', 'transform': ''})

    objectlist_A.sort(lambda x, y: cmp(len(x), len(y)))
    objectlist_B.sort(lambda x, y: cmp(len(x), len(y)))

    i = 0
    for dict_A in objectlist_A:
        for keyA, valueA in iter(sorted(dict_A.items())):
            if keyA != 'name':
                j = 0
                for dict_B in objectlist_B:
                    for keyB, valueB in iter(sorted(dict_B.items())):
                        if keyB != 'name':
                            if valueA not in ref_rules[keyA]:
                                if keyA != 'inside' and keyA != 'above':
                                    ref_rules[keyA].append(valueA)
                            if valueB not in ref_rules[keyB]:
                                if keyB != 'inside' and keyB != 'above':
                                    ref_rules[keyB].append(valueB)
                            if keyA == keyB and i == j:
                                if keyA == 'inside' or keyA == 'above':
                                    rule_diff[j][keyA] = len(valueA) - len(valueB)
                                else:
                                    rule_diff[j][keyA] = ref_rules[keyA].index(valueA) - ref_rules[
                                        keyB].index(valueB)
                    j += 1
        i += 1

    rule_add_count = -1
    rule_remove_count = -1
    if i > j:
        rule_remove_count = i - j
        for itr in range(j, i):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'remove'

    if i < j:
        rule_add_count = j - i
        for itr in range(i, j):
            for keyR, valueR in iter(sorted(rule_diff[itr].items())):
                if keyR == 'transform':
                    rule_diff[itr][keyR] = 'add'

    solution_index = 0

    for number_list in solution_list:
        solution_index += 1
        del temprule_diff[:]
        temprule_length = max(len(objectlist_C), len(number_list))
        for i in range(temprule_length):
            temprule_diff.append(
                {'shape': 0, 'size': 0, 'fill': 0, 'angle': 0, 'inside': '', 'above': '', 'alignment': 0,
                 'overlaps': '', 'transform': ''})

        number_list.sort(lambda x, y: cmp(len(x), len(y)))
        objectlist_C.sort(lambda x, y: cmp(len(x), len(y)))

        i = 0
        for dict_C in objectlist_C:
            for keyC, valueC in iter(sorted(dict_C.items())):
                if keyC != 'name':
                    j = 0
                    for dict_N in number_list:
                        for keyN, valueN in iter(sorted(dict_N.items())):
                            if keyN != 'name':
                                if valueC not in ref_rules[keyC]:
                                    if keyC != 'inside' and keyC != 'above':
                                        ref_rules[keyC].append(valueC)
                                if valueN not in ref_rules[keyN]:
                                    if keyN != 'inside' and keyN != 'above':
                                        ref_rules[keyN].append(valueN)
                                if keyC == keyN and i == j:
                                    if keyC == 'inside' or keyC == 'above':
                                        temprule_diff[j][keyC] = len(valueC) - len(valueN)
                                    else:
                                        temprule_diff[j][keyC] = ref_rules[keyC].index(valueC) - ref_rules[keyN].index(
                                            valueN)
                        j += 1
            i += 1

        temprule_add_count = -1
        temprule_remove_count = -1
        if i > j:
            temprule_remove_count = i - j
            for itr in range(j, i):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'remove'

        if i < j:
            temprule_add_count = j - i
            for itr in range(i, j):
                for keyR, valueR in iter(sorted(temprule_diff[itr].items())):
                    if keyR == 'transform':
                        temprule_diff[itr][keyR] = 'add'

        match = True
        for index in range(min(len(rule_diff), len(temprule_diff))):
            if rule_diff[index]['transform'] == 'add' or rule_diff[index]['transform'] == 'remove' \
                    or temprule_diff[index]['transform'] == 'add' or temprule_diff[index]['transform'] == 'remove':
                break
            if cmp(rule_diff[index], temprule_diff[index]) != 0:
                match = False
                break

        if match and rule_add_count == temprule_add_count and rule_remove_count == temprule_remove_count:
            temp_index = map_vertically_basic()
            if temp_index == solution_index and solution_index != -1:
                return solution_index
            else:
                if solution_index != -1:
                    return solution_index
                elif temp_index != -1:
                    return temp_index

    return -1


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
        if problem.problemType == '2x2':
            prob = problem.figures
            for key, value in sorted(prob.iteritems()):
                figure = prob[key]
                object_list = figure.objects
                parse_problem(key, object_list)
                file_name = figure.visualFilename
                load_image(key, file_name)
            i = solve_by_horizontal_reflection(problem, 0)
            if i == -1:
                i = solve_by_vertical_reflection(problem, 0)
                if i == -1:
                    i = solve_by_horizontal_rotation(problem)
                    if i == -1:
                        i = solve_by_vertical_rotation(problem)
                        if i == -1:
                            i = solve_by_pixel_diff(problem)
                            if i == -1:
                                i = solve_by_decrease(problem, 0)
                                if i == -1:
                                    i = solve_by_and(problem)
                                    if i == -1:
                                        return i
            return i
            # i = find_solution_basic()
            # if i == -1:
            #     print "Hmmm, this looks tricky. I would skip this problem." + "\n"
            # return i
        elif problem.problemType == '3x3':
            # TODO:write code for vertical symmetry
            prob = problem.figures
            for key, value in sorted(prob.items()):
                figure = prob[key]
                file_name = figure.visualFilename
                load_image(key, file_name)
            i = solve_by_reflection(problem)
            if i == -1:
                i = solve_by_pixel_diff(problem)
            #     if i == -1:
            #         i = solve_by_offset(problem, 0)
            #         if i == -1:
            #             i = solve_by_special_scaling(problem)
            #             if i == -1:
            #                 i = solve_by_rolling(problem)
            #                 if i == -1:
            #                     i = solve_by_misc(problem)
            #                     if i == -1:
            #                         return i
            return i
        else:
            return -1