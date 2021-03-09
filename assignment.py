import time


def linearSearch(target, myList):
	printDebug(f"linearSearch(target={target}, myList={myList}")

	for item in myList:
		if item == target:
			return True

	return False


def binarySearch(element, array, start, end):
	if start > end:
		return -1

	mid = (start + end) // 2
	if element == array[mid]:
		return mid

	if element < array[mid]:
		return binarySearch(element, array, start, mid - 1)
	else:
		return binarySearch(element, array, mid + 1, end)


def printDebug(msg):
	# print(msg)
	pass


def testSearches():
	listLengths = range(1_000, 100_000, 1_000)
	repeats = 10

	text = "n\tlinear\tbinary\n"

	for listLength in listLengths:
		sumLinear = 0
		sumBinary = 0

		for i in range(repeats):
			testList = list(range(listLength))

			startTime = time.time()
			linearSearch(-1, testList)
			timeLinear = time.time() - startTime

			startTime = time.time()
			binarySearch(-1, testList, 0, len(testList))
			timeBinary = time.time() - startTime

			sumLinear += timeLinear
			sumBinary += timeBinary

		text += f"{listLength}\t{sumLinear/repeats}\t{sumBinary/repeats}\n"

	with open("output.txt", "w") as file:
		file.write(text)


testSearches()
