import time
import random
from battle_engine.creatures import Creature
from battle_engine.skills import Skill
from battle_engine.status_effects import StatusEffect
from battle_engine.rng import calculate_hit, calculate_status_proc, calculate_damage_variance

def calculate_damage(attacker: Creature, defender: Creature, skill: Skill) -> int:
    if skill.power == 0:
        return 0
    # Formula baseada no Pokemon (simplificada)
    level = 50
    base_damage = (((2 * level / 5 + 2) * skill.power * (attacker.attack / defender.defense)) / 50) + 2
    return calculate_damage_variance(int(base_damage))

def perform_attack(attacker: Creature, defender: Creature, skill: Skill) -> list[str]:
    logs = [f"\n[{attacker.name}] usa {skill.name}!"]
    
    if not calculate_hit(skill.accuracy):
        logs.append(f"O ataque de {attacker.name} falhou!")
        return logs

    damage = calculate_damage(attacker, defender, skill)
    if damage > 0:
        defender.hp = max(0, defender.hp - damage)
        logs.append(f"[{defender.name}] recebe {damage} de dano! ({defender.hp}/{defender.max_hp} HP)")

    if defender.is_alive() and skill.status_effect and calculate_status_proc(skill.status_chance):
        duration = 3 if skill.status_effect.name != "STUN" else 1
        res = defender.apply_status(StatusEffect(skill.status_effect, duration))
        if res:
            logs.append(res)
            
    return logs

def run_battle(c1: Creature, c2: Creature, interactive: bool = False) -> list[str]:
    logs = [f"BATALHA INICIO: {c1.name} vs {c2.name}!\n"]
    
    turn = 1
    while c1.is_alive() and c2.is_alive():
        logs.append(f"\n--- TURNO {turn} ---")
        
        # Ordem dos turnos por speed
        first, second = (c1, c2) if c1.speed >= c2.speed else (c2, c1)
        
        for attacker, defender in [(first, second), (second, first)]:
            if not attacker.is_alive() or not defender.is_alive():
                continue
                
            logs.extend(attacker.process_status_effects())
            if not attacker.is_alive():
                logs.append(f"[{attacker.name}] desmaiou pelo dano de status!")
                break
                
            if attacker.can_act_this_turn(logs):
                # Se for interativo e for o turno da criatura do jogador (c1)
                if interactive and attacker == c1:
                    print("\n".join(logs)) # Mostra o que aconteceu ate agora
                    logs.clear()
                    print(f"\nSua vez! O que [{c1.name}] deve fazer?")
                    for i, skill in enumerate(c1.skills):
                        print(f"{i + 1}. {skill.name} (Poder: {skill.power}, Chance de Acerto: {skill.accuracy}%)")
                    
                    choice = -1
                    while choice < 0 or choice >= len(c1.skills):
                        try:
                            choice = int(input("Escolha um ataque (1-{}): ".format(len(c1.skills)))) - 1
                            if choice < 0 or choice >= len(c1.skills):
                                print("Opcao invalida.")
                        except ValueError:
                            print("Digite um numero valido.")
                    
                    skill = c1.skills[choice]
                else:
                    skill = random.choice(attacker.skills)
                    
                logs.extend(perform_attack(attacker, defender, skill))
                
        turn += 1
        # time.sleep(1) removido para eficiência da API

    winner = c1 if c1.is_alive() else c2
    loser = c2 if c1.is_alive() else c1
    logs.append(f"\nFIM DE BATALHA! {loser.name} desmaiou. {winner.name} vence com {winner.hp} HP restante!")
    return logs

