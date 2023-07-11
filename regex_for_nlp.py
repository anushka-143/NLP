import re

chat1 = 'Anushka: you ask a lot of questions 1234567890,abc@xyz.com'
chat2 = 'Anushka: yes phone: (123)-456-7890 , email: abc@xyz.com'

pattern = '\d{10}'
matches = re.findall(pattern, chat1)
print(matches)