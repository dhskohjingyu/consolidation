def linear_search(a, t):
    for i in range(len(a)):
        if a[i] == t:
            return i
    return -1

def binary_search(a, t):
    low = 0
    high = len(a)

    while low <= high:
        mid = (low + high)//2

        if a[mid] == t:
            return mid
        elif a[mid] < t:
            low = mid + 1
        elif a[mid] > t:
            high = mid - 1

    return -1

def bubble_sort(a):
    swapped = True

    while swapped:
        swapped = False
        for i in range(0, len(a)):
            for j in range(i):
                if a[i] < a[j]:
                    swapped = True
                    a[i], a[j] = a[j], a[i]

    return a

def insertion_sort(a):
    for i in range(0, len(a)):
        pivot = a[i]
        j = i

        while j > 0 and a[j - 1] > p:
            a[j] = a[j - 1]
            j -= 1

        a[j] = p

    return a

def quick_sort(a):
    if a == []:
        return []
    else:
        pivot = a[0]
        less, great = [], []

        for i in range(1, len(a)):
            if a[i] < pivot:
                less.append(a[i])
            else:
                great.append(a[i])

        return quick_sort(less) + [pivot] + quick_sort(great)
