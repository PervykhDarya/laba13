# !/usr/bin/env python3
# -*- cosing: utf-8 -*-

def knigi(author, **books):
    print(f"Автор: {author}")
    for books, name in books.items():
        print(f"{books}: {name}")


if __name__ == "__main__":
    knigi(
        "Джо Диспенза",
        книга="Сила подсознания",
        книга_1="Сам себе плацебо",
        книга_2="Сверхестественный разум",
        книга_3="Развивай свой мозг"
    )