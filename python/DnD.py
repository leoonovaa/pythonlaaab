import json
import os

class Game:
    def __init__(self):
        self.rooms = {
            'hall': {'description': 'You are in the hall. You can go forward in kithen and go left in living room', 'items': ['book'], 'forward': 'kitchen', 'left': 'living room'},
            'kitchen': {'description': 'You are in the kitchen. You can go back in hall .', 'items': [], 'back': 'hall'},
            'living room': {'description': 'You are in the living room. You see a sofa. You can go right in hall, and forward in bedroom', 'items': ['lattern'], 'right': 'hall', 'forward': 'bedroom'},
            'bedroom': {'description': 'You are in the bedroom. There is a bed here. You can go back in living room', 'items': ['potion'], 'back': 'living room'}
        }
        self.current_room = 'hall'
        self.inventory = []

    def move(self, direction):
        if direction in self.rooms[self.current_room]:
            self.current_room = self.rooms[self.current_room][direction]
            print(f"You moved to the {self.current_room}.")
        else:
            print("You can't move in that direction.")

    def look(self):
        print(self.rooms[self.current_room]['description'])
        if self.rooms[self.current_room]['items']:
            print(f"You see items: {', '.join(self.rooms[self.current_room]['items'])}")
        else:
            print("There are no items here.")

    def take(self, item):
        if item in self.rooms[self.current_room]['items']:
            self.inventory.append(item)
            self.rooms[self.current_room]['items'].remove(item)
            print(f"You took the {item}.")
        else:
            print(f"There is no {item} here.")

    def save_game(self, filename='savegame.json'):
        try:
            save_data = {
                'current_room': self.current_room,
                'inventory': self.inventory
            }
            with open(filename, 'w') as f:
                json.dump(save_data, f)
            print(f"Game saved to {filename}.")
        except IOError as e:
            print(f"Error saving game: {e}")


    def load_game(self, filename='savegame.json'):
        if not os.path.exists(filename):
            print("Save file not found.")
            return
        try:
            with open(filename, 'r') as f:
                save_data = json.load(f)
            self.current_room = save_data['current_room']
            self.inventory = save_data['inventory']
            print(f"Game loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading game: {e}")

    def show_inventory(self):
        if self.inventory:
            print(f"Your inventory: {', '.join(self.inventory)}")
        else:
            print("Your inventory is empty.")

def main():
    game = Game()
    
    while True:
        command = input("\nEnter a command (move, look, take, inventory, save, load, quit): ").strip().lower()
        if command == 'move':
            direction = input("Enter a direction (forward, back, left, right): ").strip().lower()
            game.move(direction)
        elif command == 'look':
            game.look()
        elif command == 'take':
            item = input("Enter an item to take: ").strip().lower()
            game.take(item)
        elif command == 'inventory':
            game.show_inventory()  
        elif command == 'save':
            game.save_game()
        elif command == 'load':
            game.load_game()
        elif command == 'quit':
            print("You quitted the game")
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()