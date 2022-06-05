class Dessert:
    def __init__(self, name: str = "", calories: int = 0):
        self._name = name.lower()
        self._calories = calories

    def name(self):
        return self._name

    def calories(self):
        return self._calories

    def set_name(self, name: str):
        self._name = name.lower()

    def set_calories(self, calories: int):
        self._calories = calories

    def is_healthy(self):
        return self._calories < 200

    def is_delicious(self):
        return True
