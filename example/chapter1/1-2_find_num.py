# 1-2_find_num.py
def solution(input_str):
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
	# Write your code here.
	answer = ""
	for i in range(10):
		if str(i) in input_str:
			pass
		else:
			answer = str(i)
			break

	return answer
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 

input_str1 = "012345678"
input_str2 = "483750219"
input_str3 = "242810485760109726496"
print(solution(input_str1)+", "+solution(input_str2)+", "+solution(input_str3))