
def m_variance(A):
    N=len(A)
    sum = 0
    for i in range(0,N):
        sum = sum + A[i]
    M = sum/N
    mean_dist = []
    for i in range(0,N):
        mean_dist.append((A[i]-M)**2)
    sum=0
    for i in range(0,len(mean_dist)):
        sum=sum+mean_dist[i]
    return sum/N
    