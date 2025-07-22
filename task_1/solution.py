from collections import defaultdict # {'score': 0}

t = int(input())

for _ in range(t):
    n = int (input())
    people = defaultdict(int)
    action = {}

    for _ in range(n):
        line = input().strip() # .strip Убираем пробелы в начале и в конце строки
        speaker, sentence = line.split(': ')
        words = sentence.split()
        verb = words[-1].rstrip('!')

        if words[0] == 'I':
            if words[1] == 'am':
                if words[2] == 'not':
                    people[speaker] -= 1
                else:
                    people[speaker] += 2
            else:
                target = words[0]
                if words[1] == 'is':
                    if words[2] == 'not':
                        people[target] -= 1
                    else:
                        people[target] += 1
                        action[target] = verb
if people:
    max_score = max(people.values())
    suspects = [name for name, score in people.items() if score == max_score]
    suspects.sort()

    for name in suspects:
        print(f'{name} is {action[name]}.')


