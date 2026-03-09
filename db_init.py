import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
# ajout de 5 monstre dans la base de données avec ATK, DEF et HP definis avec mongodb
db = client["Game"]
db.create_collection("Monsters")
monsters_collection = db["Monsters"]
monsters = [
    {"id": 1, "name": "Goblin", "ATK": 5, "DEF": 2, "HP": 20},
    {"id": 2, "name": "Orc", "ATK": 10, "DEF": 5, "HP": 40},
    {"id": 3, "name": "Troll", "ATK": 15, "DEF": 10, "HP": 50},
    {"id": 4, "name": "Dragon", "ATK": 30, "DEF": 20, "HP": 300},
    {"id": 5, "name": "Vampire", "ATK": 20, "DEF": 15, "HP": 40}
]
monsters_collection.insert_many(monsters)

# script pour ajouter 10 personnage dans la base de données avec ATK, DEF et HP definis avec mongodb
db.create_collection("heroes")
heroes_collection = db["heroes"]
heroes = [
    {"id": 1, "name": "Knight", "ATK": 10, "DEF": 10, "HP": 100},
    {"id": 2, "name": "Archer", "ATK": 15, "DEF": 5, "HP": 80},
    {"id": 3, "name": "Mage", "ATK": 20, "DEF": 3, "HP": 60},
    {"id": 4, "name": "Assassin", "ATK": 25, "DEF": 2, "HP": 50},
    {"id": 5, "name": "Paladin", "ATK": 12, "DEF": 12, "HP": 120},
    {"id": 6, "name": "Berserker", "ATK": 30, "DEF": 0, "HP": 80},
    {"id": 7, "name": "Druid", "ATK": 18, "DEF": 8, "HP": 70},
    {"id": 8, "name": "Necromancer", "ATK": 22, "DEF": 4, "HP": 60},
    {"id": 9, "name": "Rogue", "ATK": 28, "DEF": 3, "HP": 55},
    {"id": 10, "name": "Monk", "ATK": 14, "DEF": 10, "HP": 90}
]
heroes_collection.insert_many(heroes)