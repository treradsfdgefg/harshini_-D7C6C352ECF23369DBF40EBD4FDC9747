def linear_search_product(list, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (list[i] == x):
            return i
    return -1


list = ['chocolate','vim bar','clinic plus','maggi']
x = 1
n = len(list)
result = linear_search_product(list, n, x)
if(result ==-1):
    print("Element not found")
else:
    print("Element found at index: ", result)