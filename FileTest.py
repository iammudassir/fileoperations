
import json

f = open('<file path>')

data = json.load(f)
arr=[]

for i in data['data']:
	print(i['test'])
	arr.append(i['test']) #replace this with the string to search
f.close()
print ("Total:"+str(len(arr)))
print("Duplicate elements in given array: ");

for i in range(0, len(arr)):
	for j in range(i+1, len(arr)):
		if(arr[i] == arr[j]):
			print(arr[j]);

