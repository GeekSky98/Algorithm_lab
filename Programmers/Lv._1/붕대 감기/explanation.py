def solution(bandage, health, attacks):
    healing_cnt = 0
    current_time = 1
    current_health = health
    attack_index = 0
    while attack_index < len(attacks):
        if current_time == attacks[attack_index][0]:
            current_health -= attacks[attack_index][1]
            healing_cnt = 0
            attack_index += 1
            if current_health <= 0:
                return -1
        else:
            current_health += bandage[1]
            healing_cnt += 1
            if healing_cnt == bandage[0]:
                current_health += bandage[2]
                healing_cnt = 0
            current_health = min(current_health, health)

        current_time += 1

    return current_health