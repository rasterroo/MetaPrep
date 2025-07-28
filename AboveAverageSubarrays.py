'''
Above-Average Subarrays
You are given an array A containing N integers. Your task is to find all subarrays whose average sum is greater than the average sum of the remaining array elements. You must return the start and end index of each subarray in sorted order.
A subarray that starts at position L1 and ends at position R1 comes before a subarray that starts at L2 and ends at R2 if L1 < L2, or if L1 = L2 and R1 ≤ R2.
Note that we'll define the average sum of an empty array to be 0, and we'll define the indicies of the array (for the purpose of output) to be 1 through N. A subarray that contains a single element will have L1 = R1.
Signature
Subarray[] aboveAverageSubarrays(int[] A)
Input
1 ≤ N ≤ 2,000
1 ≤ A[i] ≤ 1,000,000
Output
A Subarray is an object with two integer fields, left and right, defining the range that a given subarray covers. Return a list of all above-average subarrays sorted as explained above.
Example 1
A = [3, 4, 2]
output = [[1, 2], [1, 3], [2, 2]]
The above-average subarrays are [3, 4], [3, 4, 2], and [4].


Welcome to Meta!

This is just a simple shared plaintext pad, with no execution capabilities.

When you know what language you would like to use during your interview,
simply choose it from the dropdown in the left bar.

Enjoy your interview!
'''

def aboveAverageSubarrays(A):
    N = len(A)
    prefix = [0] * (N + 1)
    total_sum = 0

    for i in range(N):
        total_sum += A[i]
        prefix[i + 1] = prefix[i] + A[i]

    result = []

    for i in range(N):
        for j in range(i, N):
            sub_sum = prefix[j + 1] - prefix[i]
            sub_len = j - i + 1
            sub_avg = sub_sum / sub_len

            rest_len = N - sub_len
            if rest_len > 0:
                rest_sum = total_sum - sub_sum
                rest_avg = rest_sum / rest_len
            else:
                rest_avg = 0

            if sub_avg > rest_avg:
                # Use 1-based indexing
                result.append([i + 1, j + 1])

    return result
