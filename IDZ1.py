
# Создаем список учеников и их рост в дюймах
students = [
    {"name": "John", "gender": "male", "height": 65},
    {"name": "Anna", "gender": "female", "height": 62},
    {"name": "Mike", "gender": "male", "height": 68},
    {"name": "Sarah", "gender": "female", "height": 59},
    {"name": "Kate", "gender": "female", "height": 63},
    {"name": "Tom", "gender": "male", "height": 70},
    {"name": "Linda", "gender": "female", "height": 61},
    {"name": "Alex", "gender": "male", "height": 67},
    {"name": "Emily", "gender": "female", "height": 60},
    {"name": "Jake", "gender": "male", "height": 71},
    {"name": "Olivia", "gender": "female", "height": 64},
    {"name": "David", "gender": "male", "height": 66},
    {"name": "Sophie", "gender": "female", "height": 58},
    {"name": "Daniel", "gender": "male", "height": 69},
    {"name": "Emma", "gender": "female", "height": 61},
    {"name": "Jason", "gender": "male", "height": 72},
    {"name": "Mia", "gender": "female", "height": 63}
]

# Вычисляем средний рост у мальчиков
male_heights = [s["height"] for s in students if s["gender"] == "male"]
male_avg_height = sum(male_heights) / len(male_heights)
print("Средний рост у мальчиков: {:.2f} дюймов".format(male_avg_height))

# Вычисляем средний рост у девочек
female_heights = [s["height"] for s in students if s["gender"] == "female"]
female_avg_height = sum(female_heights) / len(female_heights)
print("Средний рост у девочек: {:.2f} дюймов".format(female_avg_height))