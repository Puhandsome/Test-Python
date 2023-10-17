'''docstring'''
from math import gcd

def main():
    '''docstring'''
    size = [int(x) for  x in input().split()]
    matrix = []

    for i in range(size[0]):
        nums = [int(x) for x in input().split()]

        common = nums[0]
        for j in range(1,size[1]):
            common = gcd(common,nums[j])

        if common == 0:
            matrix.append([0]*size[1])
        else:
            matrix.append([x//common for x in nums])

    for i in range(size[0]-1):
        for j in range(i+1,size[0]):
            if matrix[i] == matrix[j]:
                print(i+1,j+1)

main()