spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    get_names= [spicy_foods["name"] for spicy_foods in spicy_foods]
    return get_names

def get_spiciest_foods(spicy_foods):
    spiciest_food= [spicy_foods for spicy_foods in spicy_foods if spicy_foods["heat_level"] > 5]
    return spiciest_food

def print_spicy_foods(spicy_foods):
    for spicy_food in spicy_foods:
        print(f"{spicy_food['name']} ({spicy_food['cuisine']}) | Heat Level: {'🌶' * spicy_food['heat_level']}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for spiciest_food in spicy_foods:
        if spiciest_food["cuisine"] == cuisine:
          return spiciest_food

def print_spiciest_foods(spicy_foods):
    for spiciest_food in spicy_foods:
        if spiciest_food["heat_level"] > 5:
            print(f"{spiciest_food['name']} ({spiciest_food['cuisine']}) | Heat Level: {'🌶' * spiciest_food['heat_level']}")


def get_average_heat_level(spicy_foods):
    average_heat = sum(spicy_food["heat_level"] for spicy_food in spicy_foods)
    average_heat_level = average_heat / len(spicy_foods)
    return average_heat_level

def create_spicy_food(spicy_foods, spicy_food):
        spicy_foods.append(spicy_food)
        return spicy_foods
