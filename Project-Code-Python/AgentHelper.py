# implemented for project2
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image
import numpy as np
import random as rand

PIXEL_THRESHOLD = 10


class AgentHelper:

    def __init__(self, problem):
        self.figures = problem.figures

    def get_intersection(self, image_1, image_2):
        return ImageChops.lighter(image_1, image_2)

    def get_num_pixels(self, img):
        black_and_white = img.convert("L")
        load = black_and_white.load()
        pixels = 0

        for i in range(0, img.size[0]):
            for j in range(0, img.size[1]):
                val = load[i, j]
                if val == 0:
                    pixels += 1
        return pixels

    def calculate_percent_difference(self, image1, image2):

        num_pixels_img1 = self.get_number_pixels(image1) * 1.0
        num_pixels_img2 = self.get_number_pixels(image2) * 1.0

        dark_pixel_pct_img1 = float(self.number_dark_pixels(image1)/num_pixels_img1)
        dark_pixel_pct_img2 = float(self.number_dark_pixels(image2)/num_pixels_img2)
        return float(dark_pixel_pct_img2 - dark_pixel_pct_img1)

    def percent_difference(self, image1, image2):
        return float(self.number_dark_pixels(image2) - self.number_dark_pixels(image1)) / ((self.number_dark_pixels(image2) + self.number_dark_pixels(image1)))

    def union(self, image_1, image_2):
        return ImageChops.darker(image_1, image_2)

    def difference(self, image_1, image_2):
        pairs = zip(image_1.getdata(), image_2.getdata())
        if len(image_1.getbands()) == 1:
            dif = sum(abs(p1 - p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1,c2 in zip(p1,p2))

        num_components = image_1.size[0] * image_1.size[1] * 3
        return (dif / 255.0 * 100 ) / num_components

    def get_bounding_box(self, image):
        org_image = image.convert(mode='L')
        inv_image = ImageChops.invert(org_image)
        return inv_image.getbbox()

    def figure_deletion_difference(self, image1, image2):
        return self.number_dark_pixels(image2) - self.number_dark_pixels(image1)

    def number_dark_pixels(self, image):
        return sum(image.histogram()[:-1])

    def populate_dictionaries(self, figureImages, answerImages):
        figures_list = {}
        answers_list = {}

        figures_list_stats = {}
        answers_list_stats = {}

        figures_list_logic = {}
        answers_list_logic = {}

        for image in figureImages:
            figures_list[image] = Image.open(self.figures[image].visualFilename)
        for image in answerImages:
            answers_list[image] = Image.open(self.figures[image].visualFilename)

        for image in figureImages:
            figures_list_stats[image] = Image.open(self.figures[image].visualFilename).convert("1")
        for image in answerImages:
            answers_list_stats[image] = Image.open(self.figures[image].visualFilename).convert("1")

        for image in figureImages:
            figures_list_logic[image] = Image.open(self.figures[image].visualFilename).convert("1")
        for image in answerImages:
            answers_list_logic[image] = Image.open(self.figures[image].visualFilename).convert("1")

        return figures_list, answers_list, figures_list_stats, answers_list_stats, figures_list_stats, answers_list_stats

    def check_percentage_change(self, percent1, percent2):
        if percent1 == 0:
            return 1
        else:
            return float(percent2/percent1) * 100

    def get_difference(self, image1, image2):
        return ImageChops.invert(ImageChops.difference(image1, image2))

    def get_options(self):
        return {k: v for k, v in self.figures.items() if k.isalpha() == False}

    def get_number_pixels(self, img):
        width, height = img.size
        return width * height

    def checkIfDarkPixelsEqual(self, img1, img2, img3, img4):
        tmp = abs(abs(self.number_dark_pixels(img2) - self.number_dark_pixels(img1)) - abs(self.number_dark_pixels(img4) - self.number_dark_pixels(img3)))
        if tmp < PIXEL_THRESHOLD:
            return True
        else:
            return False

    def calculateIfPixelPercentageEqual(self, img1, img2, img3):
        percent_1_2 = self.calculate_percent_difference(img1, img2)
        percent_2_3 = self.calculate_percent_difference(img2, img3)
        percent_1_3 = self.calculate_percent_difference(img1, img3)
        return percent_1_2, percent_2_3, percent_1_3
