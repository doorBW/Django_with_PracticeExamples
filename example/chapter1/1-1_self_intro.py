# 1-1_self_intro.py
name = "문범우"
age = 26
school = "서울 소재의 대학교"
job = "개발자"
dream = "많은 사람들이 코딩을 즐길 수 있도록 기여하는 것"
say_hello = "안녕하세요!"
say_goodbye = "잘 부탁드립니다 :)"

print(say_hello,name+"입니다.")
print("저는",school+"를 졸업하고 현재는 "+job,end='')
# end를 활용하여 print문 이후 자동 줄바꿈을 컨트롤 할 수 있다.
print("로 일하고 있습니다.\n다양한 꿈이 있지만 그 중 하나는\n'"+dream+"' 입니다.")
print('그럼',say_goodbye)