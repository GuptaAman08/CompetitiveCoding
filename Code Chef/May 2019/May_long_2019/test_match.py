t=int(input())
for _ in range(t):
	n,m=map(int,input().split())

	winner='Ari'

	while n>0 and m>0:
		if n==m:
			break
		if n>=2*m or m>=2*n:
			break
		else:
			if m>n:
				m=m-n
			else:
				n=n-m

			if winner=='Ari':
				winner='Rich'
			else:
				winner='Ari'

	print(winner)