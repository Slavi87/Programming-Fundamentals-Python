import re

text = 'fslkvnorenglkdf545023xcv;x;lfdbm4-5249020dvcd'

result = re.findall('(\d+)([a-z]+)', text)
if result:
    print(result)
    print(result[0][0])
    print(result[0][1])
