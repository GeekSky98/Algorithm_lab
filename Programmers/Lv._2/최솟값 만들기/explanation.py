def solution(A,B):
    A, B = sorted(A, reverse=True), sorted(B)
    return sum([A[i]*B[i] for i in range(len(A))])