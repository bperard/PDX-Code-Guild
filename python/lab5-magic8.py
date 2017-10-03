import random
outcomes = ['Leave me alone.', 'Doubt it.', 'Beat it kid.', 'Sure, why not?', 'I mean, anything is possible.', 'Undoubtedly.', 'I\'m not going to justify that with an answer.']
answer = ''
print('Hello, I am a "Magic" Eight Ball, and since you\'ve found me, I might as well answer a question or two.\n')
print('When you are finished bothering me, type "done".\n')
print('Let\'s begin.\n')
while answer != 'done':
    answer = input('What would you like me to tell you?')
    if answer == 'done':
        print('Throw me in the bushes and leave.')
    else:
        predict = random.choice(outcomes)
        print(predict)


