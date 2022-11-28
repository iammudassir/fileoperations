
import json

f = open('<file path>')

data = json.load(f)
arr=[]

for i in data['data']:
	print(i['sha'])
	arr.append(i['sha'])
f.close()
print ("Total Container SHA Count:"+str(len(arr)))
print("Duplicate elements in given array: ");

for i in range(0, len(arr)):
	for j in range(i+1, len(arr)):
		if(arr[i] == arr[j]):
			print(arr[j]);

