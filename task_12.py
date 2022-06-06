from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name: str = "JellyBean", flavor: str = "", calories: int = 0):
        super(JellyBean, self).__init__(name, calories)
        self._flavor = flavor.lower()

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor: str):
        self._flavor = flavor.lower()

    def is_delicious(self):
        return self._flavor != "black licorice"
