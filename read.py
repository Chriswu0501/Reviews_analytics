data = []
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		sum_len += len(line)
		data.append(line)
print("總共有", len(data), "筆資料")
print("資料中留言的平均長度為", sum_len/len(data), "個字")
