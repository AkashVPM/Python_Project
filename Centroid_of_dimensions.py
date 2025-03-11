# # Find centroid of any dimensional value by Akash S

# point = []
# center = []
# def centroid (a):
#       print(len(a))
#       b = max(a, key=len)
#       # print(b)
#       for m in range(len(a)):
#             if len(a[m]) <= len(b):
#                   for x in range (len(a[m]),len(b)):
#                         a[m].append(0)
#                   point.append(a[m])
#       print(point)
#       for m in range (len(point[0])):
#             value = 0
#             for n in range(len(point)):
#                   value += point[n][m]
#             average = value / len(a)
#             print(average)
#             center.append(average)
#       print(center)

# a = [[1,2,3,4,5,6],[1,2],[1,2,3,4],[5,6],[7],[8,9,10]]
# #[3.8333333333333335, 3.5, 2.6666666666666665, 1.3333333333333333, 0.8333333333333334, 1.0]
# centroid (a)      

# Another way:
import itertools
def centroid(*args):
    return [sum(i) / len(i) for i in itertools.zip_longest(*args, fillvalue=0)]

a = [[1,2,3,4,5,6],[1,2],[1,2,3,4],[5,6],[7],[8,9,10]]  # All lists must be of equal length
print(centroid(*a))




