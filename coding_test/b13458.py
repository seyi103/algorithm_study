def solve(N, A, B, C):
    result = N
    for a in A:
        if(int(a) - B > 0):
            result += ((int(a) - B - 1)//C) +1
    return result

if __name__ == '__main__':
    N = int(input())
    A = input().split()
    temp = input().split()
    B, C= int(temp[0]), int(temp[1])

    print(solve(N, A, B, C))