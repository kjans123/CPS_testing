class MaxDifference:

    """"Returns the max difference from a list of numbers

    :param inputList: List of input numbers. May be float or int

    :returns: max difference between any two adjacent numbers from list \
    (list[i]-list[i+1])
    :raises ImportError: raises error if math function is not found
    :raises TypeError: raises error if any list element is a string
    :raises ValueError: raises error if input is numerical, but of wrong type
    """

    def __init__(self, inputList = list):
        self.inputList = inputList
        self.maxVal = None
        self.findMax()


    def findMax(self):
        try:
            import math as mt
            import logging
            str1 = logging.DEBUG
            logging.basicConfig(filename="maxDiffLogs06.txt", \
            format='%(levelname)s %(asctime)s %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p', level=str1)
            logging.info('Succesfully imported modules')
        except ImportError:
            logging.warning('Unable to find packages')
            print("cant find package (most likely you have not \
            activated your virtual env)")
        diffList = []
        oneDiff = 0
        for i in range(len(self.inputList)):
            if i != (len(self.inputList)-1):
                try:
                    firstVal = float(self.inputList[i])
                    secondVal = float(self.inputList[i+1])
                    oneDiff = float(mt.copysign((firstVal - secondVal),1))
                    logging.info('Found difference')
                    logging.debug('Difference =' + str(oneDiff))
                except TypeError:
                    logging.warning('Invalid input: data in list \
                    is not all numerical')
                    print("attemping math operation on non-numerical input")
                except ValueError:
                    logging.warning('Invalid input: data in list is of \
                    wrong numerical type')
                    print("attempting to use an invalid numerical input (e.g., \
                    trying to find the square root of a negative number)")
                diffList.append(oneDiff)
        self.maxVal = round(max(diffList), 5)
        logging.info('Finished')
        logging.debug('Max Difference= ' + str(self.maxVal))
