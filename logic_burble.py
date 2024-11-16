def orden_burble(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]

lista = [103,23,543,65,5,867,230]

