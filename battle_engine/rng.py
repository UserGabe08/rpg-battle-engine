import random

def calculate_hit(accuracy: int) -> bool:
    return random.randint(1, 100) <= accuracy

def calculate_crit(crit_chance: float) -> bool:
    return random.random() <= crit_chance

def calculate_status_proc(proc_chance: int) -> bool:
    if proc_chance <= 0:
        return False
    return random.randint(1, 100) <= proc_chance

def calculate_damage_variance(damage: int) -> int:
    variance = random.uniform(0.85, 1.0)
    return int(damage * variance)
