from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    test_instance = Ingredient("chocolate")

    assert repr(test_instance) == "Ingredient('chocolate')"
    assert hash(test_instance) == hash("chocolate")
    assert test_instance.name == "chocolate"
    assert test_instance == Ingredient("chocolate")
    assert not test_instance.restrictions
