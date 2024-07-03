in_stock = {"coffee": 1, "milk": 2, "cream": 3}


def order(*preferences):
    recipes = {
        "Эспрессо": {"coffee": 1, "cream": 0, "milk": 0},
        "Капучино": {"coffee": 1, "cream": 0, "milk": 3},
        "Макиато": {"coffee": 2, "cream": 0, "milk": 1},
        "Кофе по-венски": {"coffee": 1, "cream": 2, "milk": 0},
        "Латте Макиато": {"coffee": 1, "cream": 1, "milk": 2},
        "Кон Панна": {"coffee": 1, "cream": 1, "milk": 0}
    }

    for drink in preferences:
        recipe = recipes.get(drink)
        if recipe:
            enough = True
            for ingredient, amount in recipe.items():
                if in_stock.get(ingredient, 0) < amount:
                    enough = False
                    break
            if enough:
                for ingredient, amount in recipe.items():
                    in_stock[ingredient] -= amount
                return drink

    return "К сожалению, не можем предложить Вам напиток"