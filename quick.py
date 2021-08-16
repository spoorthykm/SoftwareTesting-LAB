def quick(a,low,high):
	if(low<high):
		i=low
		j=high
		piv=low
		while(i<j):
			while(a[i]<=a[piv] and i<high):
				i+=1
			while(a[j]>a[piv]):
				j-=1
			if(i<j):
				a[i],a[j]=a[j],a[i]
		a[piv],a[j]=a[j],a[piv]
		quick(a,low,j-1)
		quick(a,j+1,high)
a=[]
n=int(input())
print("enter arr ele")
for i in range(n):
	ele=int(input())
	a.append(ele)
quick(a,0,n-1)
print(a)