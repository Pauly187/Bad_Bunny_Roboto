


def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st = 0;
    end = 0;
    poi = 0
    for i in range(0, size):
        curr_sum = curr_sum + arr[i]

        if (max_so_far < curr_sum):
            max_so_far = curr_sum
            st = poi
            en = i
        if (curr_sum < 0):
            curr_sum = 0
            poi = i + 1

    print("Maximum sum Subarray is", max_so_far)


arr = [2, 3, 2, -1, 3, 4, 0, -2, 0, 3, 1, -3, 0, -1, 1, 0, 4, -2, -2, 0, 3, -1, -3, 5, 0, 5, -2, 2, 0, 1, 2, -2, 1, 0,
       4, 1, -2, 4, 1, 2, 0, 1, 3, 1, -3, -3, -1, 0, 0, 2, 4, 3, 3, 2, -2, 0, -1, 1, 1, 3, 3, 1, 2, -2, -3, -3, 4, 4, 1,
       -3, -3, 1, 4, 5, 1, 2, 4, 5, 5, -2, -1, 0, -2, 3, 4, 5, 0, -1, -3, 2, 0, 0, -3, 3, -3, 1, -1, -3, 3, 1]
max_sum_subarray(arr)