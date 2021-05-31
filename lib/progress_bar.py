def createBar(iterable, decimals = 1, length = 50, printEnd = "\r"):
    total = len(iterable)
    # Progress Bar Printing Function
    def printProgressBar (iteration):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = "█" * filledLength + "-" * (length - filledLength)
        print(f'\rSearching |{bar}| {percent}% Complete', end = printEnd)
    # Initial Call
    printProgressBar(0)
    # Update Progress Bar
    for i, item in enumerate(iterable):
        yield item
        printProgressBar(i + 1)
    print()