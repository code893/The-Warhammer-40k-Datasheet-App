import os
import sys
import time
import random

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from datetime import datetime, timedelta


import requests

# file_url = "https://drive.google.com/file/d/1htvWh6MfESgso1-oqY7mfY23Vw8Q9fuc/view?usp=sharing"
# response = requests.get(file_url)
# with open('filename', 'wb') as f:
#     f.write(response.content)




repeat = True
repeat_W = True


def clear():
    # Clear the console based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def custom_print(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)

def roll_dice(num_dice, target_number):
    results = []
    passes = 0

    for _ in range(num_dice):
        roll = random.randint(1, 6)  # Roll a 6-sided die
        results.append(roll)
        if roll >= target_number:
            passes += 1

    return results, passes

def main():
  repeat_W = True
  restart = True
  restart_search = True
  while restart == True:
      SearchSelect_choice = input("Would you like to 'Search' or 'Select' a model, 'Roll' die or see a list of all Weapon 'Abilities'?\n").lower()
      if SearchSelect_choice == "search":
          restart_search = True
      elif SearchSelect_choice == "roll":
          dice_roller()
      elif SearchSelect_choice == "abilities":
          print("Go to here:")
          print("https://wahapedia.ru/wh40k10ed/the-rules/core-rules/#Weapon-Abilities\n")
          main()
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
                      time.sleep(3)
                      weapon_repeat = "yes"
                      custom_print("\nWould you like to see weapon stats? (yes/no)")
                      if input().strip().lower() == "yes":
                          while weapon_repeat == "yes":
                              for idx, weapon_name in enumerate(model.weapons):
                                  custom_print(f"\n{idx + 1} - {weapon_name}")
                              try:
                                  choice_weapon = int(input("\nChoose a weapon number: \n")) - 1
                                  if choice_weapon < 0 or choice_weapon >= len(model.weapons):
                                      raise ValueError
                                  selected_weapon = find_weapon_by_name(model.weapons[choice_weapon])
                                  if selected_weapon:
                                      selected_weapon.displayW_stats()
                                  else:
                                      custom_print("Weapon not found.")
                              except ValueError:
                                  custom_print("\nInvalid input. Please enter a valid weapon number.")

                              weapon_repeat = input(f"\nWould you like to see weapon stats for {model.model} again? (yes/no)\n").strip().lower() == "no"
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

                      choice_race = int(input("\nChoose a race number: \n")) - 1
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
                  time.sleep(3)
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

                  repeat_W = input("\nDo you want to choose another Weapon for this model? (yes/no): \n").strip().lower() == 'yes'

              repeat = input("\nDo you want to choose another model? (yes/no): ").strip().lower()
              if repeat == "no":
                  repeat = False
                  restart = True
              else:
                  repeat = True

def dice_roller():

    # Get number of dice from the user
    while True:
        try:
            num_dice = int(input("How many dice do you want to roll? "))
            if num_dice <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Get target number from the user
    while True:
        try:
            target_number = int(input("What number do you need to roll to pass? (2-6) "))
            if target_number < 2 or target_number > 6:
                print("Please enter a number between 2 and 6.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")

    # Roll the dice and get results
    results, passes = roll_dice(num_dice, target_number)

    # Display results
    print("\nDice Roll Results:")
    for i, result in enumerate(results, start=1):
        print(f"Die {i}: {result}")

    print(f"\nNumber of dice that passed (rolled {target_number}+): {passes} out of {num_dice}")
    main()




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
        # img = Image.open(self.pic)
        # new_size = (300, 300)  # Width, Height in pixels
        # resized_img = img.resize(new_size)
        # display(resized_img)
        image = mpimg.imread(self.pic)
        plt.imshow(image)
        plt.axis('off')
        plt.show()

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
        # custom_print(f"\nAbilities: {self.abilities}")

# Define races with segments containing Space Marine models
imperium = {
    "Combat Patrol": [
        Model_stat("Infernus Squad", 6, 4, 3, 2, 6, 1, ["Bolt Pistol", "Pyreblaster", "SpaceMarine CC weapon"], "None", 'Infernus Squad.jpg'), 
        Model_stat("Terminator Squad", 5, 5, 2, 3, 6, 1, ["Power Sword", "Storm bolter", "Chainfist"], "4+", 'Terminator Squad.jpg'),
        Model_stat("Captain in Terminator Armour", 5, 5, 2, 6, 6, 1, ["Storm bolter", "Combi-weapon", "Relic fist", "Relic weapon"], "4+", 'Captain in Terminator Armour.jpg'),
        Model_stat("Librarian in Terminator Armour", 5, 5, 2, 5, 6, 1, ["Combi-weapon", "Smite - witchfire", "Smite - focused witchfire",  "Storm bolter", "Force weapon"], "4+", 'Librarian in Terminator Armour.jpg'),
    ],

    "Other": [
        Model_stat("Librarian", 6, 4, 3, 4, 6, 1, ["Bolt Pistol", "Smite - witchfire", "Smite - focused witchfire", "Force weapon"], "None", 'Librarian.jpg'),
        Model_stat("Captain", 6, 4, 3, 5, 6, 1, ["Bolt Pistol", "Heavy bolt pistol", "Master-crafted boltgun", "Neo-volkite pistol", "SpaceMarine CC weapon", "Master-crafted power weapon", "Power fist"], "4+", 'Captain.jpg'),
        Model_stat("Infernus Squad", 6, 4, 3, 2, 6, 1, ["Bolt Pistol", "Pyreblaster", "SpaceMarine CC weapon"], "None", 'Infernus Squad.jpg'), 
        Model_stat("Terminator Squad", 5, 5, 2, 3, 6, 1, ["Power Sword", "Storm bolter", "Chainfist"], "4+", 'Terminator Squad.jpg'),
        Model_stat("Captain in Terminator Armour", 5, 5, 2, 6, 6, 1, ["Storm bolter", "Combi-weapon", "Relic fist", "Relic weapon"], "4+", 'Captain in Terminator Armour.jpg'),
        Model_stat("Librarian in Terminator Armour", 5, 5, 2, 5, 6, 1, ["Combi-weapon", "Smite - witchfire", "Smite - focused witchfire",  "Storm bolter", "Force weapon"], "4+", 'Librarian in Terminator Armour.jpg'),
    ]
}

necron = {
    "Combat Patrol": [
        Model_stat("Necron Warriors", 5, 4, 4, 1, 7, 2, ["Gauss flayer", "Gauss reaper", "Necron CC weapon"], "None", 'Necron Warriors.jpg'),
        Model_stat("Skorpekh Destroyers", 8, 6, 3, 3, 7, 2, ["Skorpekh hyperphase weapons"], "None", 'Skorpekh Destroyers.jpg'),
        Model_stat("Canoptek Scarab swarms", 10, 2, 6, 4, 8, 0, ["Feeder mandibles"], "None", 'Canoptek Scarab Swarms.jpg'),
        Model_stat("Canoptek Doomstalker", 8, 8, 3, 12, 8, 4, ["Twin Gauss flayer", "Doomsday blaster", "Doomstalker limbs"], "4+", 'Canoptek Doomstalker.jpg'),
        Model_stat("Overlord", 6, 6, 3, 6, 6, 1, ["Staff of light(range)", "Tachyon arrow", "Staff of light(melee)", "Overlord's blade", "Voidscythe"], "4+", 'Overlord.jpg')
    ],

    "Other": [
        Model_stat("Necron Warriors", 5, 4, 4, 1, 7, 2, ["Gauss flayer", "Gauss reaper", "Necron CC weapon"], "None", 'Necron Warriors.jpg'),
        Model_stat("Skorpekh Destroyers", 8, 6, 3, 3, 7, 2, ["Skorpekh hyperphase weapons"], "None", 'Skorpekh Destroyers.jpg'),
        Model_stat("Canoptek Scarab swarms", 10, 2, 6, 4, 8, 0, ["Feeder mandibles"], "None", 'Canoptek Scarab Swarms.jpg'),
        Model_stat("Canoptek Doomstalker", 8, 8, 3, 12, 8, 4, ["Twin Gauss flayer", "Doomsday blaster", "Doomstalker limbs"], "4+", 'Canoptek Doomstalker.jpg'),
        Model_stat("Overlord", 6, 6, 3, 6, 6, 1, ["Staff of light(range)", "Tachyon arrow", "Staff of light(melee)", "Overlord's blade", "Voidscythe"], "4+", 'Overlord.jpg'),
        Model_stat("Monolith", 8, 13, 2, 22, 7, 8, ["Death ray", "Gauss flux arc", "Particle whip", "Portal of Exile"], "None", 'Monolith.jpg')
    ],

    "The Silent King": [
        Model_stat("Szarekh", 8, 10, 2, 16, 6, 6, ["Scepter of Eternal Glory", "Staff of Stars", "Weapons of the Final Triarch"], "4+", 'Silent King.jpg'),
        Model_stat("Triarchal Menhir", 8, 10, 2, 5, 6, 1, ["Annhiliator beam", "Armoured bulk"], "4+", 'Silent King.jpg')
    ]
}

tyranids = {
    "Combat Patrol": [
        Model_stat("Psychophage", 8, 9, 3, 10, 8, 3, ["Psychoclastic torrent", "Talons and betentacled maw"], "None", 'Psychophage.jpg'),
        Model_stat("Termagaunts", 6, 3, 5, 1, 8, 2, ["Fleshborer", "Shardlauncher", "Spike rifle", "Strangleweb", "Termagat devourer", "Termaguant spinefists", "Chitinous claws and teeth"], "None", 'Termagaunts.jpg')
    ],

    "Other": [
        Model_stat("Psychophage", 8, 9, 3, 10, 8, 3, ["Psychoclastic torrent", "Talons and betentacled maw"], "None", 'Psychophage.jpg'),
        Model_stat("Termagaunts", 6, 3, 5, 1, 8, 2, ["Fleshborer", "Shardlauncher", "Spike rifle", "Strangleweb", "Termagat devourer", "Termaguant spinefists", "Chitinous claws and teeth"], "None", 'Termagaunts.jpg')
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
     # A  D  R WS/BS S AP
weapons = [
    Weapons("Psychoclastic torrent", 12, "D6", "N/A", 6, -1, 1),
    Weapons("Talons and betentacled maw", 0, "D6+1", 3, 6, -1, 2),

    Weapons("Necron CC weapon", 0, 1, 4, 4, 0, 1),
    Weapons("Gauss flayer", 24, 1, 4, 4, 0, 1),
    Weapons("Gauss reaper", 12, 2, 4, 4, 0, 1),
    Weapons("Skorpekh hyperphase weapons", 0, 4, 3, 7, -2, 2),
    Weapons("Feeder mandibles", 0, 6, 5, 2, 0, 1),
    Weapons("Twin Gauss flayer", 24, 1, 4, 4, 0, 1),
    Weapons("Doomsday blaster", 48, "D6+1", 4, 14, -3, 3),
    Weapons("Doomstalker limbs", 0, 3, 4, 6, 0, 1),
    Weapons("Tachyon arrow", 72, 1, 2, 16, -5, "D6+2"),
    Weapons("Staff of light(range)", 18, 3, 2, 5, -2, 1),
    Weapons("Staff of light(melee)", 0, 4, 2, 5, -2, 1),
    Weapons("Overlord's blade", 0, 4, 2, 8, -3, 2),
    Weapons("Voidscythe", 0, 3, 3, 12, -3, 3),
    Weapons("Death ray", 24, 1, 3, 12, -4, "D6+1"),
    Weapons("Gauss flux arc", 24, 3, 3, 6, -1, 1),
    Weapons("Particle whip", 24, "3D6", 3, 8, -1, 3),
    Weapons("Portal of Exile", 0, 6, 2, 8, -2, 3),
    Weapons("Annhiliator beam", 24, 1, 2, 14, -4, 6),
    Weapons("Armoured bulk", 0, 1, 4, 4, 0, 1),
    Weapons("Staff of Stars", 24, 12, 2, 6, -1, 1),
    Weapons("Weapons of the Final Triarch", 0, 12, 2, 8, -3, 2),
    Weapons("Scepter of Eternal Glory", 0, 2, 2, 10, -3, 3),

    Weapons("Bolt Pistol", 12, 1, 2, 4, 0, 1),
    Weapons("Heavy bolt pistol", 12, 1, 2, 4, -1, 1),
    Weapons("Pyreblaster", 12, "D6", "N/A", 5, 0, 1),
    Weapons("SpaceMarine CC weapon", 0, 3, 3, 4, 0, 1),
    Weapons("Boltgun", 24, 2, 3, 4, 0, 1),
    Weapons("Master-crafted boltgun", 24, 2, 2, 4, -1, 2),
    Weapons("Neo-volkite pistol", 12, 1, 2, 5, 0, 2),
    Weapons("Heavy Bolter", 36, 3, 4, 5, -1, 2),
    Weapons("Storm bolter", 24, 2, 3, 4, 0, 1),
    Weapons("Combi-weapon", 24, 1, 4, 4, 0, 1),
    Weapons("Relic fist", 0, 5, 2, 8, -2, 2),
    Weapons("Relic weapon", 0, 6, 2, 5, -2, 2),
    Weapons("Master-crafted power weapon", 0, 6, 2, 5, -2, 2),
    Weapons("Power fist", 0, 6, 2, 8, -2, 2),
    Weapons("Smite - witchfire", 24, "D6", 3, 5, -1, "D3"),
    Weapons("Smite - focused witchfire", 24, "D6", 3, 6, -2, "D3"),
    Weapons("Force weapon", 0, 4, 3, 6, -1, "D3")
]


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
    custom_print("You can then view detailed stats about the selected model and its weapons.\n")
    custom_print("It also has dice roller.\n\n")
    custom_print("Press Enter to continue...\n")
    input()

    # now = datetime.now()
    # now = now + timedelta(hours=1)
    # formatted_now = now.strftime(f"%Y-%m-%d %H:%M:%S")
    # file = open("Logs.txt", "a")
    # file.write(f"\nUsed -> {formatted_now}")
    # file.close()



starting_page()
main()
