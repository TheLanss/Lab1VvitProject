groupmates = [
    {
        "name": "Ярослав",
        "surname": "Семёнов",
        "exams": ["Информатика", "Вышмат", "ОБЖ"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Диана",
        "surname": "Крюкова",
        "exams": ["Обществознание", "АиГ", "Физика"],
        "marks": [5, 5, 3]
    },
    {
        "name": "Павел",
        "surname": "Охримчук",
        "exams": ["Философия", "История", "Физическая культура"],
        "marks": [5, 4, 4]
    },
    {
        "name": "Михаил",
        "surname": "Романчук",
        "exams": ["Английский язык", "Русский язык", "Физическая культура"],
        "marks": [4, 5, 4]
    },
    {
        "name": "Анастасия",
        "surname": "Сахарова",
        "exams": ["Алгоритмы", "Компьютерная графика", "Вычислительная техника"],
        "marks": [3, 3, 4]
    }
    
]

sort_stud = float(input())
groupmates = filter(lambda x: sum(x["marks"]) / len(x["marks"]) > sort_stud, groupmates)

def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(70), u"Оценки".ljust(30))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(70), str(student["marks"]).ljust(30))
print_students(groupmates)



























