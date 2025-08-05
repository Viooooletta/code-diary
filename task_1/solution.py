from collections import defaultdict
import string


def process_block(lines):
    scores = defaultdict(int)
    action = {}

    for line in lines:
        if ':' in line:
            speaker, sentence = line.split(': ', 1)
        else:
            parts = line.split()
            if not parts:
                continue
            speaker = parts[0]
            sentence = ' '.join(parts[1:])
        words = sentence.rstrip(string.punctuation).split()
        if not words:
            continue

        if words[0] == 'I':
            if len(words) >= 3 and words[1] == 'am':
                if words[2] == 'not':
                    scores[speaker] -= 1
                else:
                    scores[speaker] += 2
                    action[speaker] = words[-1]
        else:
            target = words[0]
            if len(words) >= 3 and words[1] == 'is':
                if words[2] == 'not':
                    scores[target] -= 1
                else:
                    scores[target] += 1
                    action[target] = words[-1]

    if scores:
        max_score = max(scores.values())
        winners = sorted(name for name, score in scores.items() if score == max_score)
        for name in winners:
            print(f"{name} is {action[name]}.")
lines = [line.strip() for line in sys.stdin if line.strip()]

if lines and lines[0].isdigit():
    t = int(lines[0])
    idx = 1
    for _ in range(t):
        n = int(lines[idx])
        idx += 1
        block = lines[idx:idx+n]
        idx += n
        process_block(block)
else:
    process_block(lines)