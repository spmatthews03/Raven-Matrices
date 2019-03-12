# implemented for project2
from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image

PIXEL_THRESHOLD = 10

def calculatePercentDifference(image1, image2):

    num_pixels_img1 = get_number_pixels(image1) * 1.0
    num_pixels_img2 = get_number_pixels(image2) * 1.0

    dark_pixel_pct_img1 = float(numberDarkPixels(image1)/num_pixels_img1)
    dark_pixel_pct_img2 = float(numberDarkPixels(image2)/num_pixels_img2)
    return float(dark_pixel_pct_img2 - dark_pixel_pct_img1)


def figureDeletionDifference(image1, image2):
    return numberDarkPixels(image1) - numberDarkPixels(image2)


def numberDarkPixels(image):
    return sum(image.histogram()[:-1])


def numberLightPixels(image):
    return True


def rowOrColumnAddition(images):
    total = 0
    for image in images:
        total = numberDarkPixels(image)

    return total


def populateDictionaries(figureImages, answerImages, problem):
    figuresList = {}
    answersList = {}

    figuresListStats = {}
    answersListStats = {}

    figuresListLogic = {}
    answersListLogic = {}

    for image in figureImages:
        figuresList[image] = Image.open(problem.figures[image].visualFilename)
    for image in answerImages:
        answersList[image] = Image.open(problem.figures[image].visualFilename)


    for image in figureImages:
        figuresListStats[image] = Image.open(problem.figures[image].visualFilename).convert("1")
    for image in answerImages:
        answersListStats[image] = Image.open(problem.figures[image].visualFilename).convert("1")

    for image in figureImages:
        figuresListLogic[image] = Image.open(problem.figures[image].visualFilename).convert("1")
    for image in answerImages:
        answersListLogic[image] = Image.open(problem.figures[image].visualFilename).convert("1")


    return figuresList, answersList, figuresListStats, answersListStats, figuresListStats, answersListStats


def check_percentage_change(percent1, percent2):
    if percent1 == 0:
        return 1
    else:
        return float(percent2/percent1) * 100


# def check_images_same(img1, img2):
#     if list(img1.getdata()) == list(img2.getdata()):
#         return True
#     else:
#         return False


def get_number_pixels(img):
    width, height = img.size
    return width * height


def checkIfDarkPixelsEqual(img1, img2, img3, img4):
    tmp = abs(abs(numberDarkPixels(img2) - numberDarkPixels(img1)) - abs(numberDarkPixels(img4) - numberDarkPixels(img3)))
    if tmp < PIXEL_THRESHOLD:
        return True
    else:
        return False

def checkIfDarkPixelsEqual_for2(img1, img2):
    tmp = abs(numberDarkPixels(img2) - numberDarkPixels(img1))
    if tmp < PIXEL_THRESHOLD:
        return True
    else:
        return False


def calculateIfPixelPercentageEqual(img1, img2, img3):
    percent_1_2 = calculatePercentDifference(img1, img2)
    percent_2_3 = calculatePercentDifference(img2, img3)
    percent_1_3 = calculatePercentDifference(img1, img3)
    return percent_1_2, percent_2_3, percent_1_3
