# implemented for project2

from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image


PIXEL_THRESHOLD = 10

def calculatePercentDifference(image1, image2):

    if type(image1) is int or type(image2) is int or type(image1) is float or type(image2) is float:
        if abs(image2 + image1) < THRESHOLD:
            print("No Difference")
            return 0
        else:
            return float((image2 - image1) / ((image2 + image1)*.05))
    else:
        return float((numberDarkPixels(image2) - numberDarkPixels(image1)) / ((numberDarkPixels(image2) + numberDarkPixels(image1))*.5))


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



def checkIfDarkPixelsEqual(img1, img2, img3, img4):
    tmp = abs(abs(numberDarkPixels(img2) - numberDarkPixels(img1)) - abs(numberDarkPixels(img4) - numberDarkPixels(img3)))
    if tmp < PIXEL_THRESHOLD:
        return True
    else:
        return False


def calculateIfPixelPercentageEqual(img1, img2, img3):
    percent_1_2 = calculatePercentDifference(img1, img2)
    percent_2_3 = calculatePercentDifference(img2, img3)
    return percent_2_3 - percent_1_2
