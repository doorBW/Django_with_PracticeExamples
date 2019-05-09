# 1-3_remove_num.py
def solution(input_str):
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
	# Write your code here.
	answer = ""
	number_list = ['0','1','2','3','4','5','6','7','8','9']
	# 또는 아래와 같이 map함수를 이용하여 number_list를 만들 수 있습니다.
	# number_list = list(map(str,range(10)))
	
	for i in input_str:
		if i in number_list:
			pass
		else:
			answer += i

	return answer
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 

input_str1 = "H123e4l5l6o7, P8y9t1h2o3n.4"
input_str2 = "6L11if3e 4is 5to1o0 sh00or3t."
input_str3 = "7Y3o7u n456ee2d5 6pyt9h5on2."
print(solution(input_str1)+", "+solution(input_str2)+", "+solution(input_str3))