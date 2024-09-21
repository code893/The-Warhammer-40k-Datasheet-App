import os
import sys
import time

from PIL import Image

from loggingin import loginPage

repeat = True

def clear():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def custom_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)



class Model_stat:
    def __init__(self, model, object_control, movement, wounds, toughness, save, leadership, weapons, inv_s, pic):
        self.model = model
        self.object_control = object_control
        self.movement = movement
        self.wounds = wounds
        self.toughness = toughness
        self.save = save
        self.leadership = leadership
        self.inv_s = inv_s
        self.weapons = weapons
        self.pic = pic

    def displayU_stats(self):
        custom_print(f"\n\nModel: {self.model}")
        custom_print(f'\nMovement: {self.movement}"')
        custom_print(f"\nToughness: {self.toughness}")
        custom_print(f"\nSave: {self.save}+")
        if self.inv_s == "None":
            custom_print("\nInvulnerable Save: None")
        else:
            custom_print(f"\nInvulnerable Save: {self.inv_s}")
        custom_print(f"\nWounds: {self.wounds}")
        custom_print(f"\nLeadership: {self.leadership}+")
        custom_print(f"\nObject Control: {self.object_control}")
        custom_print(f"\n\nWeapons: {', '.join(self.weapons)}")
        img = Image.open(self.pic)
        img.show()
        img.close()

class Weapons:
    def __init__(self, name, attack, damage, range, weapon_skill, strength, armour_penetration):
        self.name = name
        self.range = range
        self.attack = attack
        self.damage = damage
        self.strength = strength
        self.weapon_skill = weapon_skill
        self.armour_penetration = armour_penetration
        # self.abilities = abilities

    def displayW_stats(self):
        custom_print(f"\n\nWeapon: {self.name}")
        custom_print(f'\nRange: {self.range}"')
        custom_print(f"\nAttacks: {self.attack}")
        if self.range == 0:
            custom_print(f"\nWeapon Skill: {self.weapon_skill}+")
        else:
            custom_print(f"\nBallistic Skill: {self.weapon_skill}+")
        custom_print(f"\nStrength: {self.strength}")
        custom_print(f"\nArmour Penetration: {self.armour_penetration}")
        custom_print(f"\nDamage: {self.damage}")
        # custom_print(f"\n\nAbilities: {self.abilities}")

# Define races with segments containing Space Marine models
imperium = {
    "Combat Patrol": [
        Model_stat("Infernus Squad", 1, 6, 2, 4, 3, 6, ["Bolt Pistol", "Pyreblaster", "SpaceMarine CC weapon"], "None", 'Pics/Infernus Squad.jpg'), 
        Model_stat("Terminator Squad", 1, 5, 3, 5, 2, 6, ["Power Sword", "Storm bolter", "Chainfist"], "4+",'Pics/Terminator Squad.jpg'),
        Model_stat("Captain in Terminator Armour", 1, 5, 6, 5, 2, 6, ["Storm bolter", "Combi-weapon", "Relic fist", "Relic weapon"], "4+", 'Pics/Captain in Terminator Armour.jpg'),
        Model_stat("Librarian in Terminator Armour", 1, 5, 5, 5, 2, 6, ["Combi-weapon", "Smite - witchfire", "Smite - focused witchfire",  "Storm bolter", "Force weapon"], "4+", 'Pics/Librarian in Terminator Armour.jpg'),
    ],

    "Other": [
        Model_stat("Librarian", 1, 6, 4, 4, 3, 6, ["Bolt Pistol", "Smite - witchfire", "Smite - focused witchfire",  "Force weapon"], "None", 'Pics/Librarian.jpg'),
        Model_stat("Captain", 1, 6, 5, 4, 3, 6, ["Bolt Pistol", "Heavy bolt pistol", "Master-crafted boltgun", "Neo-volkite pistol", "SpaceMarine CC weapon", "Master-crafted power weapon", "Power fist" ], "4+", 'Pics/Captain.jpg'),
        Model_stat("Infernus Squad", 1, 6, 2, 4, 3, 6, ["Bolt Pistol", "Pyreblaster", "SpaceMarine CC weapon"], "None", 'Pics/Infernus Squad.jpg'), 
        Model_stat("Terminator Squad", 1, 5, 3, 5, 2, 6, ["Power Sword", "Storm bolter", "Chainfist"], "4+", 'Pics/Terminator Squad.jpg'),
        Model_stat("Captain in Terminator Armour", 1, 5, 6, 5, 2, 6, ["Storm bolter", "Combi-weapon", "Relic fist", "Relic weapon"], "4+", 'Pics/Captain in Terminator Armour.jpg'),
        Model_stat("Librarian in Terminator Armour", 1, 5, 5, 5, 2, 6, ["Combi-weapon", "Smite - witchfire", "Smite - focused witchfire",  "Storm bolter", "Force weapon"], "4+", 'Pics/Librarian in Terminator Armour.jpg'),
                            # OC M  W  T  S  L  Weapon --> Inv S
    ]
}
necron ={
    "Combat Patrol": [               # OC M  W  T  S  L  Weapon --> Inv S
        Model_stat( "Necron Warriors", 2, 5, 1, 4, 4, 7,  ["Gauss flayer", "Gauss reaper", "Necron CC weapon"], "None",'Pics/Necron Warriors.jpg'),
        Model_stat( "Skorpekh Destroyers", 2, 8, 3, 6, 3, 7,  ["Skorpekh hyperphase weapons"], "None",'Pics/Skorpekh Destroyers.jpg'),
        Model_stat( "Canoptek Scarab swarms", 0, 10, 4, 2, 6, 8,  ["Feeder mandibles"], "None",'Pics/Canoptek Scarab Swarms.jpg'),
        Model_stat( "Canoptek Doomstalker", 4, 8, 12, 8, 3, 8,  ["Twin Gauss flayer", "Doomsday blaster", "Doomstalker limbs"], "4+",'Pics/Canoptek Doomstalker.jpg'),
        Model_stat("Overlord", 1, 6, 6, 6, 3, 6, ["Staff of light(range)", "Tachyon arrow", "Staff of light(melee)", "Overlord's blade", "Voidscythe",], "4+",'Pics/Overlord.jpg')
    ],
    "Other": [               # OC M  W  T  S  L  Weapon --> Inv S
        Model_stat( "Necron Warriors", 2, 5, 1, 4, 4, 7,  ["Gauss flayer", "Gauss reaper", "Necron CC weapon"], "None",'Pics/Necron Warriors.jpg'),
        Model_stat( "Skorpekh Destroyers", 2, 8, 3, 6, 3, 7,  ["Skorpekh hyperphase weapons"], "None",'Pics/Skorpekh Destroyers.jpg'),
        Model_stat( "Canoptek Scarab swarms", 0, 10, 4, 2, 6, 8,  ["Feeder mandibles"], "None",'Pics/Canoptek Scarab Swarms.jpg'),
        Model_stat( "Canoptek Doomstalker", 4, 8, 12, 8, 3, 8,  ["Twin Gauss flayer", "Doomsday blaster", "Doomstalker limbs"], "4+",'Pics/Canoptek Doomstalker.jpg'),
        Model_stat("Overlord", 1, 6, 6, 6, 3, 6, ["Staff of light(range)", "Tachyon arrow", "Staff of light(melee)", "Overlord's blade", "Voidscythe",], "4+",'Pics/Overlord.jpg'),
        Model_stat("Monolith", 8, 8, 22, 13, 2, 7, ["Death ray", "Gauss flux arc", "Particle whip", "Portal of Exile",], "None",'Pics/Monolith.jpg')
    ],
    
    "The Silent King": [
        Model_stat( "Szarekh", 6, 8, 16, 10, 2, 6,  ["Scepter of Eternal Glory", "Staff of Stars", "Weapons of the Final Triarch"], "4+",'Pics/Silent King.jpg'),
        Model_stat( "Triarchal Menhir", 1, 8, 5, 10, 2, 6,  ["Annhiliator beam", "Armoured bulk"], "4+",'Pics/Silent King.jpg'),
    ]                                 # OC M  W  T  S  L  Weapon --> Inv S
    
}

tyranids ={
    "Combat Patrol": [           # OC M  W  T  S  L  Weapon --> Inv S
        Model_stat( "Psychophage", 3, 8, 10, 9, 3, 8,  ["Psychoclastic torrent", "Talons and betentacled maw"], "None",'Pics/Psychophage.jpg'),
        Model_stat( "Termagaunts", 2, 6, 1, 3, 5, 8,  ["Fleshborer", "Shardlauncher", "Spike rifle", "Strangleweb", "Termagat devourer", "Termaguant spinefists", "Chitinous claws and teeth"], "None",'Pics/Termagaunts.jpg'),
    ],
    
    "Other": [           # OC M  W  T  S  L  Weapon --> Inv S
        Model_stat( "Psychophage", 3, 8, 10, 9, 3, 8,  ["Psychoclastic torrent", "Talons and betentacled maw"], "None",'Pics/Psychophage.jpg'),
        Model_stat( "Termagaunts", 2, 6, 1, 3, 5, 8,  ["Fleshborer", "Shardlauncher", "Spike rifle", "Strangleweb", "Termagat devourer", "Termaguant spinefists", "Chitinous claws and teeth"], "None",'Pics/Termagaunts.jpg'),
    ]
}

# Add more races as needed
races = {
    "Imperium": imperium,
    "Necron": necron,
    "Tyranids": tyranids,
    # "Orks": ork,
    # "Eldar": eldar,
}

weapons = [                          # A  D  R WS/BS S AP
    Weapons("Psychoclastic torrent", "D6", 1, 12, "N/A", 6, -1),
    Weapons("Talons and betentacled maw", "D6+1", 2, 0, 3, 6, -1),
    
    Weapons("Necron CC weapon", 1, 1, 0, 4, 4, 0),
    Weapons("Gauss flayer", 1, 1, 24, 4, 4, 0),
    Weapons("Gauss reaper", 2, 1, 12, 4, 4, 0),
    Weapons("Skorpekh hyperphase weapons", 4, 2, 0, 3, 7, -2),
    Weapons("Feeder mandibles", 6, 1, 0, 5, 2, 0),
    Weapons("Twin Gauss flayer", 1, 1, 24, 4, 4, 0),
    Weapons("Doomsday blaster", "D6+1", 3, 48, 4, 14, 3),
    Weapons("Doomstalker limbs", 3, 1, 0, 4, 6, 0),
    Weapons("Tachyon arrow", 1, "D6+2", 72, 2, 16, -5),
    Weapons("Staff of light(range)", 3, 1, 18, 2, 5, -2),
    Weapons("Staff of light(melee)", 4, 1, 0, 2, 5, -2),
    Weapons("Overlord's blade", 4, 2, 0, 2, 8, -3),
    Weapons("Voidscythe", 3, 3, 0, 3, 12, -3),
    Weapons("Death ray", 1, "D6+1", 24, 3, 12, -4),
    Weapons("Gauss flux arc", 3, 1, 24, 3, 6, -1),
    Weapons("Particle whip", "3D6", 3, 24, 3, 8, -1),
    Weapons("Portal of Exile", 6, 3, 0, 2, 8, -2),
    Weapons("Annhiliator beam", 1, 6, 24, 2, 14, -4),
    Weapons("Armoured bulk", 1, 1, 0, 4, 4, 0),
    Weapons("Staff of Stars", 12, 1, 24, 2, 6, -1),
    Weapons("Weapons of the Final Triarch", 12, 2, 0, 2, 8, -3),
    Weapons("Scepter of Eternal Glory", 2, 3, 0, 2, 10, -3),
                           # A  D  R WS/BS S AP
    
    Weapons("Bolt Pistol", 1, 1, 12, 2, 4, 0),
    Weapons("Heavy bolt pistol", 1, 1, 12, 2, 4, -1),
    Weapons("Pyreblaster", "D6", 1, 12, "N/A", 5, 0),
    Weapons("SpaceMarine CC weapon", 3, 1, 0, 3, 4, 0),
    Weapons("Boltgun", 2, 1, 24, 3, 4, 0),
    Weapons("Master-crafted boltgun", 2, 2, 24, 2, 4, -1),
    Weapons("Neo-volkite pistol", 1, 2, 12, 2, 5, 0),
    Weapons("Heavy Bolter", 3, 2, 36, 4, 5, -1),
    Weapons("Storm bolter", 2, 1, 24, 3, 4, 0),
    Weapons("Combi-weapon", 1, 1, 24, 4, 4, 0),
    Weapons("Relic fist", 5, 2, 0, 2, 8, -2),
    Weapons("Relic weapon", 6, 2, 0, 2, 5, -2),
    Weapons("Master-crafted power weapon", 6, 2, 0, 2, 5, -2),
    Weapons("Power fist", 6, 2, 0, 2, 8, -2),
    Weapons("Smite - witchfire", "D6", "D3", 24, 3, 5, -1),
    Weapons("Smite - focused witchfire", "D6", "D3", 24, 3, 6, -2),
    Weapons("Force weapon", 4, "D3", 0, 3, 6, -1)

    
]
repeat_W = True
def search_models(search_term):
    results = []
    seen_models = set()
    for race, subcategories in {"Imperium": imperium, "Necron": necron, "Tyranids": tyranids}.items():
        for subcategory, models in subcategories.items():
            for model in models:
                if search_term.lower() in model.model.lower() and model.model not in seen_models:
                    results.append((race, subcategory, model))
                    seen_models.add(model.model)
    return results

def find_weapon_by_name(name):
    for weapon in weapons:
        if weapon.name == name:
            return weapon
    return None



def starting_page():
    clear()
    custom_print("Welcome to The Warhammer 40k Datasheet app!\n")
    custom_print("This program allows you to select a race, segment, and model within them.\n")
    custom_print("You can then view detailed stats about the selected model and its weapons.\n\n")
    custom_print("Press Enter to continue...\n")
    input()

starting_page()
loginPage()
restart = True
restart_search = True
while restart == True:
    SearchSelect_choice = input("Would you like to 'Search' or 'Select' a model?").lower()
    if SearchSelect_choice == "search":
        restart_search = True
    else:
        restart_search = False
        repeat = True
    while restart_search == True:
        if SearchSelect_choice == "search":
            search_term = input("Enter the model name to search: ")
            search_results = search_models(search_term)
            clear()
            if search_results:
                custom_print(f"Search results for '{search_term}':\n\n")
                for race, subcategory, model in search_results:
                    custom_print(f"Race: {race}, Subcategory: {subcategory}")
                    model.displayU_stats()
                    weapon_repeat = "yes"
                    custom_print("\nWould you like to see weapon stats? (yes/no)")
                    if input().strip().lower() == "yes":
                        while weapon_repeat == "yes":
                            for idx, weapon_name in enumerate(model.weapons):
                                custom_print(f"\n{idx + 1} - {weapon_name}")
                            try:
                                choice_weapon = int(input("\nChoose a weapon number: ")) - 1
                                if choice_weapon < 0 or choice_weapon >= len(model.weapons):
                                    raise ValueError
                                selected_weapon = find_weapon_by_name(model.weapons[choice_weapon])
                                if selected_weapon:
                                    selected_weapon.displayW_stats()
                                else:
                                    custom_print("Weapon not found.")
                            except ValueError:
                                custom_print("\nInvalid input. Please enter a valid weapon number.")
        
                            weapon_repeat = input(f"\nWould you like to see weapon stats for {model.model} again? (yes/no)").strip().lower() == "no"
                            restart_search = False
                            repeat = False
                    else:
                        restart_search = False
                        repeat = False
            else:
                custom_print(f"No results found for '{search_term}'")
    while repeat:
        
            while True:
                try:
                    custom_print("Races:")
                    race_keys = list(races.keys())
                    for i, race in enumerate(race_keys):
                        custom_print(f"\n{i+1} - {race}")
                        
                    choice_race = int(input("\nChoose a race number: ")) - 1
                    if choice_race < 0 or choice_race >= len(races):
                        raise ValueError
                    break
                except ValueError:
                    custom_print("\nInvalid input. Please enter a valid race number.")
        
            selected_race = race_keys[choice_race]
            selected_segments = races[selected_race]
        
            custom_print(f"\nSegments in {selected_race}:")
            segment_keys = list(selected_segments.keys())
            for i, segment in enumerate(segment_keys):
                custom_print(f"\n{i+1} - {segment}")
        
            while True:
                try:
                    choice_segment = int(input("\nChoose a segment number: ")) - 1
                    if choice_segment < 0 or choice_segment >= len(selected_segments):
                        raise ValueError
                    break
                except ValueError:
                    custom_print("\nInvalid input. Please enter a valid segment number.")
        
            selected_segment = segment_keys[choice_segment]
            selected_models = selected_segments[selected_segment]
        
            custom_print(f"\nAvailable Models in {selected_segment}:")
            for i, marine in enumerate(selected_models):
                custom_print(f"\n{i+1} - {marine.model}")
        
            while True:
                try:
                    choice_model = int(input("\nChoose a model number: ")) - 1
                    if choice_model < 0 or choice_model >= len(selected_models):
                        raise ValueError
                    break
                except ValueError:
                    custom_print("\nInvalid input. Please enter a valid model number.")
        
            selected_marine = selected_models[choice_model]
            selected_marine.displayU_stats()
        
        
            while repeat_W:
                custom_print("\n\nAvailable Weapons:")
                model_weapons = [weapon for weapon in weapons if weapon.name in selected_marine.weapons]
                for i, weapon in enumerate(model_weapons):
                    custom_print(f"\n{i+1} - {weapon.name}")
        
                while True:
                    try:
                        weapon_choice = int(input("\nChoose a weapon number to display its stats: ")) - 1
                        if weapon_choice < 0 or weapon_choice >= len(model_weapons):
                            raise ValueError
                        break
                    except ValueError:
                        custom_print("\nInvalid input. Please enter a valid weapon number.")
        
                selected_weapon = model_weapons[weapon_choice]
                selected_weapon.displayW_stats()
        
                repeat_W = input("\nDo you want to choose another Weapon for this model? (yes/no): ").strip().lower() == 'yes'
        
            repeat = input("\nDo you want to choose another model? (yes/no): ").strip().lower()
            if repeat == "no":
                repeat = False
                restart = True
            else:
                repeat = True
