from abc import ABC, abstractmethod


class MazeFactory(ABC):
    @abstractmethod
    def create_room(self):
        pass
    
    @abstractmethod
    def create_wall(self):
        pass
    
    @abstractmethod
    def create_enemy(self):
        pass


class Room(ABC):
    @abstractmethod
    def describe(self):
        pass


class Wall(ABC):
    @abstractmethod
    def describe(self):
        pass


class Enemy(ABC):
    @abstractmethod
    def attack(self):
        pass


class WinterRoom(Room):
    def describe(self):
        return "Ви перебуваєте в засніженій кімнаті"

class WinterWall(Wall):
    def describe(self):
        return "Стіни покриті льодом"

class WinterEnemy(Enemy):
    def attack(self):
        return "На вас нападає сніговик"

class WinterMazeFactory(MazeFactory):
    def create_room(self):
        return WinterRoom()

    def create_wall(self):
        return WinterWall()

    def create_enemy(self):
        return WinterEnemy()


class DesertRoom(Room):
    def describe(self):
        return "Ви перебуваєте в піщаній кімнаті"

class DesertWall(Wall):
    def describe(self):
        return "Стіни зроблені з піщанику"

class DesertEnemy(Enemy):
    def attack(self):
        return "На вас нападає скорпіон"

class DesertMazeFactory(MazeFactory):
    def create_room(self):
        return DesertRoom()

    def create_wall(self):
        return DesertWall()

    def create_enemy(self):
        return DesertEnemy()


class JungleRoom(Room):
    def describe(self):
        return "Ви перебуваєте в джунглевій кімнаті"

class JungleWall(Wall):
    def describe(self):
        return "Стіни покриті лозами"

class JungleEnemy(Enemy):
    def attack(self):
        return "На вас нападає пантера"

class JungleMazeFactory(MazeFactory):
    def create_room(self):
        return JungleRoom()

    def create_wall(self):
        return JungleWall()

    def create_enemy(self):
        return JungleEnemy()


class MazeGame:
    def __init__(self, factory: MazeFactory):
        self.factory = factory

    def play(self):
        room = self.factory.create_room()
        wall = self.factory.create_wall()
        enemy = self.factory.create_enemy()

        print(room.describe())
        print(wall.describe())
        print(enemy.attack())


def main():
    theme = input("Оберіть тему (зима, пустеля, джунглі): ").lower()

    if theme == "зима":
        factory = WinterMazeFactory()
    elif theme == "пустеля":
        factory = DesertMazeFactory()
    elif theme == "джунглі":
        factory = JungleMazeFactory()
    else:
        print("Невідома тема")
        factory = WinterMazeFactory()

    game = MazeGame(factory)
    game.play()

if __name__ == "__main__":
    main()