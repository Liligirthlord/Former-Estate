from dataclasses import dataclass, field
from typing import Dict, Optional

@dataclass
class Room:
    name: str
    description: str
    exits: Dict[str, 'Room'] = field(default_factory=dict)

    def describe(self) -> str:
        exits = ', '.join(self.exits.keys()) or 'none'
        return f"{self.name}\n\n{self.description}\n\nExits: {exits}"

@dataclass
class Player:
    location: Room

class Game:
    def __init__(self):
        self.start_room = Room(
            "Entrance Hall",
            "You stand in a massive entrance hall with a dusty chandelier. A hallway leads north."
            "There is a stair leading up to the second floor."
        )
        self.hall = Room(
            "Hallway",
            "A long, dim hallway. Portraits line the walls; one frame is askew."
        )
        self.second_floor = Room(
             "Second Floor",
             "The second floor is dark and eerie, with creaking floorboards."
         )
        # Link rooms
        
        self.start_room.exits['north'] = self.hall
        self.hall.exits['south'] = self.start_room
        self.start_room.exits['up'] = self.second_floor
        self.second_floor.exits['down'] = self.start_room

        self.player = Player(location=self.start_room)
        self.running = True

    def handle_command(self, cmd: str) -> Optional[str]:
        parts = cmd.strip().lower().split()
        if not parts:
            return None
        verb = parts[0]
        if verb in ('quit', 'exit'):
            self.running = False
            return "Goodbye."
        if verb in ('look', 'l'):
            return self.player.location.describe()
        if verb == 'go' and len(parts) > 1:
            direction = parts[1]
            dest = self.player.location.exits.get(direction)
            if dest:
                self.player.location = dest
                return f"You go {direction}.\n\n{dest.describe()}"
            return "You can't go that way."
        if verb == 'help':
            return "Commands: look, go <direction>, help, quit"
        return "Unknown command. Type 'help' for commands."

    def run(self):
        print("Welcome to Former Estate (early prototype). Type 'help' for commands.")
        print(self.player.location.describe())
        try:
            while self.running:
                cmd = input("> ")
                out = self.handle_command(cmd)
                if out:
                    print(out)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting game.")

def start_game():
    """Start the game loop"""
    Game().run()

if __name__ == "__main__":
    Game().run()