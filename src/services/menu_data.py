# Req 3
from src.models.dish import Dish
from src.models.ingredient import Ingredient
import csv


class MenuData:
    def __init__(self, source_path) -> None:
        self.path = source_path
        self.dishes = set()
        self.increase_menu()

    def read_file(self, path):
        with open(path) as file:
            file = csv.reader(file)
            return list(file)

    def increase_menu(self):
        lines = self.read_file(self.path)

        for line in lines[1:]:
            dish_name = line[0]
            price = float(line[1])
            ingredient_name = line[2]
            amount = int(line[3])

            existing_dish = next(
                (
                    item
                    for item in self.dishes
                    if item == Dish(dish_name, price)
                ),
                object,
            )

            dish = Dish(dish_name, price)

            if existing_dish is not object:
                existing_dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), amount
                )
            else:
                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), amount
                )
                self.dishes.add(dish)
