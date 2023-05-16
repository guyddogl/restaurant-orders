import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient


# Req 2
def test_dish():
    test_instance = Dish("Churrasco", 28.9)

    assert test_instance == Dish("Churrasco", 28.9)
    assert test_instance.name == "Churrasco"
    assert hash(test_instance) == hash("Dish('Churrasco', R$28.90)")
    assert not test_instance.get_restrictions()

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Pizza", 0)

    test_instance.add_ingredient_dependency(Ingredient("Queijo"), 1)

    assert test_instance.recipe == {Ingredient("Queijo"): 1}
    assert {
        ingredient.name for ingredient in test_instance.get_ingredients()
    } == {"Queijo"}
