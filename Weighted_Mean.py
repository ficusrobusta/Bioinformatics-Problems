# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
Z = 0

for i in range(N):
    Z = Z + (X[i]*W[i])
W_sum = sum(W)
Weight_mean = round((Z / W_sum),1)

print(Weight_mean)

