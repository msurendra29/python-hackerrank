N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
pattern = [('.|.'*(2*i + 1)).center(M,'-') for i in range(N//2)]
print('\n'.join(pattern + ['WELCOME'.center(M,'-')] + pattern[::-1]))
