from devopslib.randomfruit import pick_fruit, meal


def test_pick_fruit():
    fruit_choice = pick_fruit()
    assert fruit_choice in ["apple", "cherry", "strawberry"]


def test_meal():
    meal_choice = meal("muffins")
    if meal_choice == "muffins":
        assert "muffins" in meal_choice
