# Import the json module to read data from a JSON file
import json

# Main function which starts the game
def start():
	# Makes a list to store clues which will be collected by the player later in the game
    clues = []
	
	# Current case number
    case = 1
	
	# Controls the game loop whether it's running or not
    running = True
	
	# Tracks whether Mamie Smith is murdered or not
    mamieMurder = False
    
	# Opens and loads data from the JSON file
    with open("data.json", "r") as file:
        data = json.load(file)

	# Assigns JSON selections to variables
    details, locations1, locations2 = data[0], data[1], data[2]

	# Starting text of the game (The title)
    print("--- THE RED HERRING: A text based RPG ---")
	
	# Starting location
    current_loc = "Office"

	# Main game loop
    while running:
	
		# Use map that depends on the current case
        current_map = locations1 if case == 1 else locations2
		
		# Get current area data
        area = current_map[current_loc]
      
		# Event when entering restaurant (Mamie Smith gets murdered)	  
        if current_loc == "Restaurant" and not mamieMurder:
            print("You and your friend enter the restaurant. The air is filled with the sound of music, cheers, and laughter. Then, suddenly, the music stops.")
            print("The performer, Mamie Smith, clutches her throat, gasps for air, and collapses on stage.")
            print("The crowd screams. Congratulations, you've got yourself a new murder case to deal with.")
            mamieMurder = True

		# Display location now
        print(f"\n--- Location: {current_loc} ---")
        print(f"You are in {area['desc']}")
		
		# Show menu choices
        print("1-Investigate, 2-Talk, 3-Move, 4-Inventory")
        choice = input("> ")
	
		# Investigate option
        if choice == "1":
            print("\nInvestigate what?")
			
			# If choice 1 is picked, show items in current area
            for i, item in enumerate(area['items']):
                print(f"{i+1}. {item}")
            
            idx = input("Select number: ")
			
			# Check if the number is valid
            if idx.isdigit() and 0 < int(idx) <= len(area['items']):
                item_name = area['items'][int(idx)-1]
				
				# Show item description
                print(f"\n{details.get(item_name, 'Nothing too special about this one.')}")
                
				# Important clues list
                important = ["Old Photo", "Poisoned Glass", "Threatening Note", "Fingerprint", "Crimson Ring"]
                
				# Add clue to inventory if important
				if item_name in important and item_name not in clues:
                    print("You thoroughly examine the object and realize… it’s a clue. An important one. So, you put it in your inventory.")
                    clues.append(item_name)
		
		# Talk option
        elif choice == "2":
            print("\nTalk to whom?")
			
			# Show NPCs to talk in the area
            for i, npc in enumerate(area['npcs']):
                print(f"{i+1}. {npc}")
            
            idx = input("Select number: ")
			
			# Check valid input
            if idx.isdigit() and 0 < int(idx) <= len(area['npcs']):
                npc_name = area['npcs'][int(idx)-1]
				
				# Show NPC dialogue
                print(f"\n{npc_name}: '{details.get(npc_name, 'Hm? Oh, the collapse? I dont know anything, thats for sure.')}")

		# Move option
        elif choice == "3":
            print("\nWhere to?")
			
			# Get available exits
            valid_exits = area['exits']
			
			# Show the exits
            for i, exit_name in enumerate(valid_exits):
                print(f"{i+1}. {exit_name}")
            
            move_idx = input("Select number: ")
			
			# Move if the choice is valid
            if move_idx.isdigit() and 0 < int(move_idx) <= len(valid_exits):
                current_loc = valid_exits[int(move_idx)-1]
            else:
                print("You can't get there from here.")

		# Inventory option
        elif choice == "4":
            print(f"Inventory: {clues}")

		# Winning condition for case 1
        if case == 1 and len(clues) >= 3:
            print("\nThe first case has been successfully solved. Congratulations, detective, but I think there's another one waiting...")
            running = False  # End case 1 start case 2
start()