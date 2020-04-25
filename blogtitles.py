import re
user_writing = []
while True:
	line = input()
	if not line: 
		break
	else:
		user_writing.append(line)
user_writing = '\n'.join(user_writing)
print(re.sub('([A-Z])', r' \1', user_writing))