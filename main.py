import time


def linearSearch(target, myList):
    printDebug(f"linearSearch(target={target}, myList={myList}")

    for i, item in enumerate(myList):
        if item == target:
            return i

    return None


def binarySearch(target, myList):
    printDebug(f"binarySearch(target={target}, myList={myList}")

    if len(myList) == 0:
        return None

    midIndex = len(myList) // 2
    midValue = myList[midIndex]

    printDebug(f"midIndex={midIndex}")
    printDebug(f"midValue={midValue}")

    if target == midValue:
        return midIndex
    elif target < midValue:
        return binarySearch(target, myList[:midIndex])
    else:
        return binarySearch(target, myList[midIndex + 1:])


def printDebug(msg):
    # print(msg)
    pass


def testSearches():
    listLengths = range(0, 1000000, 50000)

    print("n\tlinear\tbinary")

    for listLength in listLengths:
        testList = list(range(listLength))

        startTime = time.time()
        linearSearch(-1, testList)
        timeLinear = time.time() - startTime

        startTime = time.time()
        binarySearch(-1, testList)
        timeBinary = time.time() - startTime

        print(f"{listLength}\t{timeLinear}\t{timeBinary}")


testSearches()
