def findJudge(N, trust):
    # Initialize counts for trusts and trusted_by
    trusts = [0] * (N + 1)
    trusted_by = [0] * (N + 1)
    
    # Update trust relationships
    for a, b in trust:
        trusts[a] += 1
        trusted_by[b] += 1
    
    # Find the judge
    for i in range(1, N + 1):
        if trusts[i] == 0 and trusted_by[i] == N - 1:
            return i
    
    return -1
