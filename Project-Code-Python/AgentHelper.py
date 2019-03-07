# implemented for project2

from PIL import ImageFilter, ImageStat, ImageOps, ImageChops, Image


THRESHOLD = 0.001

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


