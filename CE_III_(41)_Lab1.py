import matplotlib.pyplot as plt
import time

def linearSearch(array: list, target: int) -> int:
	for index in range(len(array)):
		if (array[index] == target):
			return index
	return -1


def binarySearch(array: list, target: int) -> int:
	left = 0
	right = len(array)

	while (left <= right):
		mid = (left + right) // 2

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			right = mid - 1
		else:
			left = mid + 1
	return -1


def recursiveBinarySearch(array: list, target: int, left: int, right: int) -> int:
	if (left <= right):
		mid = (left + right) // 2

		if array[mid] == target:
			return mid
		elif array[mid] > target:
			return recursiveBinarySearch(array, target, left, mid - 1)
		else:
			return recursiveBinarySearch(array, target, mid + 1, right)
	return -1


def testLinearSearch() -> None:
	array = [5, 7, 8, 4, 3, 19, 34]
	print("\nGiven array: {} \n".format(array))
	print("Test Case 1")
	target = 8
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))
		
	print("Test Case 2")
	target = 3
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))

	print("Test Case 3")
	target = 5
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))

	print("Test Case 4")
	target = 34
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))


def testBinarySearch() -> None:
	array = [1, 3, 4, 7, 8, 9, 11, 13, 15, 17]
	print("\nGiven array: {} \n".format(array))
	print("Test Case 1")
	target = 11
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))
		
	print("Test Case 2")
	target = 3
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))

	print("Test Case 3")
	target = 8
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))

	print("Test Case 4")
	target = 34
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))


def testRecursiveBinarySearch() -> None:
	array = [1, 3, 4, 7, 8, 9, 11, 13, 15, 17]
	print("\nGiven array: {} \n".format(array))
	print("Test Case 1")
	target = 11
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))
		
	print("Test Case 2")
	target = 3
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))

	print("Test Case 3")
	target = 8
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))

	print("Test Case 4")
	target = 34
	print("Target = {}".format(target))
	print("Target Index = {} \n".format(linearSearch(array, target)))


def plotLinearSearch() -> None:
	times = list()
	for i in range(10000, 100001, 10000):
		array = list(range(1, i + 1))
		target = array[-1]
		startTime = time.time()
		print(startTime, end=" ")
		index = linearSearch(array, target)
		endTime = time.time()
		print(endTime, end=" ")
		print(target)
		times.append(endTime - startTime)
	print(times)
	plt.plot(times, color='red', lw=10)
	plt.xlabel('n (x10000)')
	plt.ylabel('t (s) ')
	plt.show()


def plotBinarySearch() -> None:
	times = list()
	for i in range(10000, 100001, 10000):
		array = list(range(1, i + 1))
		target = array[len(array) // 2]
		startTime = time.time()
		print(startTime, end=" ")
		index = binarySearch(array, target)
		endTime = time.time()
		print(endTime, end=" ")
		print(target)
		times.append(endTime - startTime)
	print(times)
	plt.plot(times, color='red', lw=10)
	plt.xlabel('n (x10000)')
	plt.ylabel('t (s) ')
	plt.show()


def plotRecursiveBinarySearch() -> None:
	times = list()
	for i in range(10000, 100001, 10000):
		array = list(range(1, i + 1))
		target = array[len(array) // 2]
		startTime = time.time()
		print(startTime, end=" ")
		index = recursiveBinarySearch(array, target, 0, len(array))
		endTime = time.time()
		print(endTime, end=" ")
		print(target)
		times.append(endTime - startTime)
	print(times)
	plt.plot(times, color='red', lw=10)
	plt.xlabel('n (x10000)')
	plt.ylabel('t (s) ')
	plt.show()


if __name__ == '__main__':
	testRecursiveBinarySearch()

