import random
from battle_engine.creatures import Creature
from battle_engine.skills import Skill
from battle_engine.status_effects import StatusType
from battle_engine.battle import run_battle

def main():
    tackle = Skill(name="Tackle", power=40, accuracy=100)
    ember = Skill(name="Ember", power=40, accuracy=100, status_effect=StatusType.BURN, status_chance=10)
    flamethrower = Skill(name="Flamethrower", power=90, accuracy=100, status_effect=StatusType.BURN, status_chance=10)
    
    water_gun = Skill(name="Water Gun", power=40, accuracy=100)
    hydro_pump = Skill(name="Hydro Pump", power=110, accuracy=80, status_effect=StatusType.WET, status_chance=30)
    
    vine_whip = Skill(name="Vine Whip", power=45, accuracy=100)
    sludge_bomb = Skill(name="Sludge Bomb", power=90, accuracy=100, status_effect=StatusType.POISON, status_chance=30)
    
    spark = Skill(name="Spark", power=65, accuracy=100, status_effect=StatusType.STUN, status_chance=30)
    thunderbolt = Skill(name="Thunderbolt", power=90, accuracy=100, status_effect=StatusType.STUN, status_chance=10)
    
    ice_beam = Skill(name="Ice Beam", power=90, accuracy=100, status_effect=StatusType.FREEZE, status_chance=10)

    charizard = Creature(
        name="Charizard", max_hp=78, hp=78, attack=84, defense=78, speed=100,
        skills=[tackle, ember, flamethrower]
    )
    
    blastoise = Creature(
        name="Blastoise", max_hp=79, hp=79, attack=83, defense=100, speed=78,
        skills=[tackle, water_gun, hydro_pump]
    )
    
    venusaur = Creature(
        name="Venusaur", max_hp=80, hp=80, attack=82, defense=83, speed=80,
        skills=[tackle, vine_whip, sludge_bomb]
    )
    
    pikachu = Creature(
        name="Pikachu", max_hp=35, hp=35, attack=55, defense=40, speed=90,
        skills=[tackle, spark, thunderbolt]
    )
    
    lapras = Creature(
        name="Lapras", max_hp=130, hp=130, attack=85, defense=80, speed=60,
        skills=[water_gun, ice_beam]
    )

    combatants = [charizard, blastoise, venusaur, pikachu, lapras]
    
    print("=== RPG BATTLE ENGINE ===")
    print("Escolha o seu Pokémon:")
    for i, c in enumerate(combatants):
        print(f"{i + 1}. {c.name} (HP: {c.hp}, ATK: {c.attack}, DEF: {c.defense}, SPD: {c.speed})")
        
    choice = -1
    while choice < 0 or choice >= len(combatants):
        try:
            choice = int(input(f"Escolha um numero (1-{len(combatants)}): ")) - 1
        except ValueError:
            pass
            
    c1 = combatants.pop(choice)
    c2 = random.choice(combatants) # Oponente aleatorio do restante
    
    print(f"\nVocê escolheu {c1.name}! O oponente escolheu {c2.name}!\n")
    
    logs = run_battle(c1, c2, interactive=True)
    if logs:
        for log in logs:
            print(log)

if __name__ == "__main__":
    main()
