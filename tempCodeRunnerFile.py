# arr = [1,2,3,7,5]
# s = 12
# start = 0
# sum = 0
# for i in range(0,len(arr)):
#     sum += arr[i]
#     while sum > s:
#         sum -= arr[start]
#         start += 1
#     if(sum == s):
#         print(start,i)
#         break


# arr = [1,3,5,8,9,2,6,7,6,8,9]
# jump = 0
# i = 0
# while i<len(arr):
#     i += arr[i]
#     jump += 1
# print(jump)


# arr = [1,2,3,2,4,5,5]
# ans = set()
# for i in arr:
#     if(arr.count(i) > 1):
#         ans.add(i)
# print(ans)

A = [3,1,2,3,3]
N = 5
for i in range(0,N):
    if(A.count(i) >= N//2):
        print(i)
