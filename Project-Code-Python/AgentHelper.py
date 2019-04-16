# implemented for project2
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image
import numpy as np
import random as rand

PIXEL_THRESHOLD = 10


class AgentHelper:

    def __init__(self, problem):
        self.figures = problem.figures



    def calculate_percent_difference(self, image1, image2):

        num_pixels_img1 = self.get_number_pixels(image1) * 1.0
        num_pixels_img2 = self.get_number_pixels(image2) * 1.0

        dark_pixel_pct_img1 = float(self.number_dark_pixels(image1)/num_pixels_img1)
        dark_pixel_pct_img2 = float(self.number_dark_pixels(image2)/num_pixels_img2)
        return float(dark_pixel_pct_img2 - dark_pixel_pct_img1)



    def figureDeletionDifference(self, image1, image2):
        return self.number_dark_pixels(image1) - self.number_dark_pixels(image2)


    def number_dark_pixels(self, image):
        return sum(image.histogram()[:-1])


    def rowOrColumnAddition(self, images):
        total = 0
        for image in images:
            total = self.number_dark_pixels(image)

        return total


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


    def choose_answer(self, rms_vals, answers):

        similarity = float("inf")
        most_similar = []
        for option in answers:
            diff = abs(self.encode(option) - rms_vals)
            if diff < similarity:
                similarity = diff
                most_similar = [option]
            elif diff == similarity:
                most_similar.append(option)
        most_similar = rand.choice(most_similar) if len(most_similar) > 0 else -1

        return int(most_similar)


    def check_percentage_change(self, percent1, percent2):
        if percent1 == 0:
            return 1
        else:
            return float(percent2/percent1) * 100


    def get_figures(self):
        return {k: v for k, v in self.figures.items() if k.isalpha() == True}

    def get_options(self):
        return {k: v for k, v in self.figures.items() if k.isalpha() == False}

    def encode(self, option):
        val = self.convert_images()
        val.append(self.get_historgram(option))
        return self.get_rms(val)


    def get_historgram(self, a):
        hist = Image.open(self.figures[str(a)].visualFilename).convert('L').resize([184,184]).histogram()
        return ImageStat.Stat(hist).rms


    def convert_images(self):
        array = []
        for figure in self.get_figures():
            array.append(self.get_historgram(figure))
        return array


    def get_rms(self, array):
        return np.sqrt(np.mean(np.square(array)))


    def get_number_pixels(self, img):
        width, height = img.size
        return width * height


    def checkIfDarkPixelsEqual(self, img1, img2, img3, img4):
        tmp = abs(abs(self.number_dark_pixels(img2) - self.number_dark_pixels(img1)) - abs(self.number_dark_pixels(img4) - self.number_dark_pixels(img3)))
        if tmp < PIXEL_THRESHOLD:
            return True
        else:
            return False

    def checkIfDarkPixelsEqual_for2(self, img1, img2):
        tmp = abs(self.number_dark_pixels(img2) - self.number_dark_pixels(img1))
        if tmp < PIXEL_THRESHOLD:
            return True
        else:
            return False


    def calculateIfPixelPercentageEqual(self, img1, img2, img3):
        percent_1_2 = self.calculate_percent_difference(img1, img2)
        percent_2_3 = self.calculate_percent_difference(img2, img3)
        percent_1_3 = self.calculate_percent_difference(img1, img3)
        return percent_1_2, percent_2_3, percent_1_3
