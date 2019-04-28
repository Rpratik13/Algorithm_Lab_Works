import random
import time
import matplotlib.pyplot as plt

def insertionSort(array: list) -> list:
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


def merge(left: list, right: list) -> list:
    leftIndex = rightIndex = 0
    merged = list()
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            merged.append(left[leftIndex])
            leftIndex += 1
        else:
            merged.append(right[rightIndex])
            rightIndex += 1

    for i in range(leftIndex, len(left)):
        merged.append(left[i])

    for i in range(rightIndex, len(right)):
        merged.append(right[i])

    return merged


def mergeSort(array: list) -> list:
    if len(array) > 1:
        left = mergeSort(array[:len(array) // 2])
        right = mergeSort(array[len(array) // 2:])
        array = merge(left, right)
    return array


def testInsertionSort() -> None:
    for i in range(1, 6):
        array = [random.randint(0, 1000) for r in range(10)]
        print("Test Case: {}".format(i))
        print("Given Array: {}".format(array))
        print("Sorted Array: {}\n".format(insertionSort(array)))


def testMergeSort() -> None:
    for i in range(1, 6):
        array = [random.randint(0, 1000) for r in range(10)]
        print("Test Case: {}".format(i))
        print("Given Array: {}".format(array))
        print("Sorted Array: {}\n".format(mergeSort(array)))


def plotInsertionSort() -> None:
    times = list()
    for i in range(1000, 10001, 1000):
        array = list(range(1, i + 1))
        array = array[::-1]
        startTime = time.time()
        array = insertionSort(array)
        endTime = time.time()
        times.append(endTime - startTime)
        print("{} {}".format(i, endTime - startTime))
    plt.plot(times, color='red', lw=5)
    plt.xlabel('n (x1000)')
    plt.ylabel('t (s) ')
    plt.show()


def plotMergeSort() -> None:
    times = list()
    for i in range(100000, 1000001, 100000):
        array = list(range(1, i + 1))
        array = array[::-1]
        startTime = time.time()
        array = mergeSort(array)
        endTime = time.time()
        times.append(endTime - startTime)
        print("{} {}".format(i, endTime - startTime))
    plt.plot(times, color='red', lw=5)
    plt.xlabel('n (x100000)')
    plt.ylabel('t (s) ')
    plt.show()

if __name__ == '__main__':
    plotMergeSort()