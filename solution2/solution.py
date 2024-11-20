import wikipediaapi
import csv


def first_letters(categorymembers, level=0, max_level=1):
    output = []
    for c in categorymembers.values():
        output.append(c.title[0])
    return output

def get_answer():
    wiki = wikipediaapi.Wikipedia("solution", "ru")
    page = wiki.page("Категория:Животные по алфавиту")
    letters = first_letters(page.categorymembers)
    letters.pop(-1)
    letters.pop(-1)
    consts = sorted(set(letters), key=lambda x: x)
    with open("beasts.csv", mode="w", encoding='utf-8') as f:
        file = csv.writer(f, delimiter=",", lineterminator="\r")
        for item in consts:
            count = letters.count(item)
            file.writerow([item, count])