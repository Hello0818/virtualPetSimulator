import json

class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 52   
        self.hunger = 52      
        self.energy = 52      

    def feed(self):
        if self.hunger > 0:
            self.hunger = max(self.hunger - 20, 0)
            self.happiness = min(self.happiness + 5, 100)
            print(f"Successful breeding, {self.name}'s hungry-20.")
        else:
            print(f"{self.name} is not hungry!")

    def play(self):
        if self.energy >= 10:
            self.happiness = min(self.happiness + 20, 100)
            self.energy = max(self.energy - 10, 0)
            self.hunger = min(self.hunger + 15, 100)
            print(f"You are playing with {self.name}!")
        else:
            print(f"{self.name} has no energy to play.")

    def sleep(self):
        self.energy = min(self.energy + 20, 100)
        self.hunger = min(self.hunger + 10, 100)
        print(f"{self.name} took a nap and feels more rested.")

    def get_status(self):
        print(f"\n----- {self.name}'s status -----")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100\n")

    def save_to_file(self, filename):
        data = {
            'name': self.name,
            'hunger': self.hunger,
            'happiness': self.happiness,
            'energy': self.energy
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            pet = Pet(data['name'])
            pet.hunger = data['hunger']
            pet.happiness = data['happiness']
            pet.energy = data['energy']
            return pet
        except FileNotFoundError:
            return None
