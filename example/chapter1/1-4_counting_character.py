# 1-4_counting_character.py
def solution(input_str):
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
	# Write your code here.
	answer = ""
	input_dic = {}
	for i in input_str:
		if i in input_dic.keys():
			input_dic[i] += 1
		else:
			input_dic[i] = 1
	input_list = list(input_dic.keys())
	input_list.sort()

	for i in input_list:
		answer += i
		answer += str(input_dic[i])

	return answer
	# - # - # - # - # - # - # - # - # - # - # - # - # - # - # 
input_str1 = "aaabbccd"
input_str2 = "ffaafddde"
input_str3 = "aabcdadbbfweeaddfadf"
print(solution(input_str1), solution(input_str2), solution(input_str3))