N = int(input())
A = list(map(int, input().split()))

# スコアが大きい方から2番目を求めるのが面倒なので最大を一旦消そうとしたが
# removeで消すとindexがずれるので値を0にすることで対処
A[A.index(max(A))] = 0
print(A.index(max(A))+1)
