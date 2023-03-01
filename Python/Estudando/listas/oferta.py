T = int(input())

for i in range(T):
    A = input()
    N,K=map(int,A.split())

    x=int((N % K) + (N / K))
    print(x)