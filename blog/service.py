import random


class Game:
    def set_damage(self, damage: int):
        # Queryset
        i_get = f"I get damage - {damage}"
        i_set = self.get_damage()
        return i_get, i_set

    def get_damage(self):
        return f'i Kick - {random.randint(1,1000)}'


