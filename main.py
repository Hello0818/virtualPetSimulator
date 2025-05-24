from pet import Pet
import os

def main():

    print("Welcome to the Virtual Pet Simulator!")
    pet = None
    filename = None

    while True:
        choice = input("\nDo you want to load an existing pet? (y/n): ").strip().lower()
        if choice == 'y':
            filename = input("Enter the filename to load from: ").strip()
            pet = Pet.load_from_file(filename)
            if pet:
                break
            else:
                print("Failed to load pet. Please try again.")
        elif choice == 'n':
            name = input("What is your pet's name? ").strip()
            pet = Pet(name)
            filename = None
            break
        else:
            print("Please enter 'y' or 'n'.")
    
    pet.get_status()
    while True:
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Sleep")
        print("4. Save and Exit")
        print("5. Check status")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
             if filename:
                 pet.save_to_file(filename)
                 print(f"Pet saved to {filename}. Goodbye!")
                 break
             else:
                while True:
                    temp_filename = input("Enter a filename to save your pet: ").strip()
                    if not os.path.exists(temp_filename):
                        filename = temp_filename
                        break
                    else:
                        print("Filename already exists. Please enter a different one.")
                pet.save_to_file(filename)
                print(f"Pet saved to {filename}. Goodbye!")
                break
        elif choice == '5':
            pet.get_status()
        else:
            print("Invalid choice. Please choose 1-5.")

if __name__ == "__main__":
    main()