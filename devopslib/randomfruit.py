from random import choices


def pick_fruit():
    fruits = ["apple", "cherry", "strawberry"]
    return choices(fruits)[0]


def meal(beverage):
    my_fruit = pick_fruit()
    if my_fruit == "cherry":
        return f"I love {my_fruit}" + "pie"
    elif my_fruit == "apple" and beverage == "muffins":
        return f"I totally love {my_fruit}" + " " + beverage
    return f"I don't like {my_fruit}"
