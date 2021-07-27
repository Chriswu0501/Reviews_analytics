data = []
sum_len = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		sum_len += len(line)
		data.append(line)
print("總共有", len(data), "筆留言")
print("留言的平均長度為", sum_len/len(data), "個字")
new = [n for n in data if len(n) < 100]
print("總共有", len(new), "筆留言少於100個字")
good = [g for g in data if 'good' in g]
print("總共有", len(good), "筆留言提到good")