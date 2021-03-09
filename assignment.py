import time
import random


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


def binaryIncludingSorting():
	listLengths = range(1_000, 100_000, 1_000)
	repeats = 10
	maxListValue = 1_000_000

	random.seed(54325)

	text = "n\tBinary search (including sort)\tBinary search (excluding sort)\tLinear search\n"

	for i, listLength in enumerate(listLengths):
		print(f"{i}/{len(listLengths)}")

		sumLinear = 0
		sumBinary = 0
		sumBinaryWithSort = 0

		for i in range(repeats):
			testList = random.choices(population=range(maxListValue), k=listLength)

			startTime = time.time()
			linearSearch(-1, testList)
			timeLinear = time.time() - startTime

			startTime = time.time()
			testList.sort()
			binarySearch(-1, testList, 0, len(testList))
			timeBinaryWithSort = time.time() - startTime

			startTime = time.time()
			binarySearch(-1, testList, 0, len(testList))
			timeBinary = time.time() - startTime

			sumLinear += timeLinear
			sumBinary += timeBinary
			sumBinaryWithSort += timeBinaryWithSort

		text += f"{listLength}\t{sumBinaryWithSort/repeats}\t{sumBinary/repeats}\t{sumLinear/repeats}\n"

	with open("output.txt", "w") as file:
		file.write(text)


def justBinary():
	listLengths = range(100_000, 10_000_000, 100_000)
	repeats = 100

	random.seed(54325)

	text = "n\tBinary search (excluding sort)\n"

	for i, listLength in enumerate(listLengths):
		print(f"{i}/{len(listLengths)}")

		sumBinary = 0

		for i in range(repeats):
			testList = list(range(listLength))

			startTime = time.time()
			binarySearch(-1, testList, 0, len(testList))
			sumBinary += time.time() - startTime

		text += f"{listLength}\t{sumBinary/repeats}\n"

	with open("output.txt", "w") as file:
		file.write(text)


justBinary()
