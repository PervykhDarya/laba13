def print_scores(student, *scores):
    print(f"Student Name: {student}")
    for score in scores:
        print(score)


print_scores("Jonathan", 100, 95, 88, 92, 99)
