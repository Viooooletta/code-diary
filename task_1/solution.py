from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int (input())
    people = defaultdict(int)
    for _ in range(n):
        statement = input().strip()

        # делаем парсер строки
        max_score = max(score.values())
        suspects = [name for name, score in score.items() if score == max_score]