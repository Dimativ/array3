def multipication_on_avg(arr):
    avg = 0
    for i in range(len(arr)):
        avg += arr[i]
    avg /= len(arr)
    for i in range(len(arr)):
        arr[i] *= avg
    return arr