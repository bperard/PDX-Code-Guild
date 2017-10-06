import random
eyes = ['8', 'X', ':', ';', '>:']
noses = ['o', '0', '3']
mouths = ['P', 'D', ')', '(', '|']
faces = int(input('How many silly faces would you like me to make for you?'))
i = 0
sentence = ''
while i < faces:
    sentence += random.choice(eyes)
    sentence += random.choice(noses)
    sentence += random.choice(mouths) + '\n'
    i += 1

print(sentence)
