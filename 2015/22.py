from utils import *
inp = input_file(2015, 22).strip()

parsed_input = parser(inp, "{{ls }}: {{i}}")

boss_hp, boss_damage = parsed_input[0][-1], parsed_input[1][-1]

minsp = math.inf
def round(turn, player_hp, boss_hp, mana, s_turn, p_turn, r_turn, spent, hard=False):
    global minsp
    if spent >= minsp or (turn == 0 and mana < 53) or player_hp <= 0:
        return None
    if boss_hp - 3 * (p_turn != 0) <= 0:
        minsp = min(minsp, spent)
    else:
        if turn == 0:
            player_hp -= hard
            boss_hp -= 3 * (p_turn != 0)
            mana += 101 * (r_turn != 0)
            if mana  >= 53:
                round(1, player_hp, boss_hp - 4, mana - 53, max(0, s_turn - 1), max(0, p_turn - 1), max(0, r_turn - 1), spent + 53, hard)
            if mana >= 73:
                round(1, player_hp + 2, boss_hp - 2, mana - 73, max(0, s_turn - 1), max(0, p_turn - 1), max(0, r_turn - 1), spent + 73, hard)
            if mana >= 113 and s_turn <= 1:
                round(1, player_hp, boss_hp, mana - 113, max(0, 6), max(0, p_turn - 1), max(0, r_turn - 1), spent + 113, hard)
            if mana >= 173 and p_turn <= 1:
                round(1, player_hp, boss_hp, mana - 173, max(0, s_turn - 1), max(0, 6), max(0, r_turn - 1), spent + 173, hard)
            if mana >= 229 and r_turn <= 1:
                round(1, player_hp, boss_hp, mana - 229,  max(0, s_turn - 1), max(0, p_turn - 1), max(0, 5), spent + 229, hard)
        else:
            round(0, player_hp - max(1, boss_damage - 7 * (s_turn != 0)), boss_hp - 3 * (p_turn != 0), mana + 101 * (r_turn != 0), max(0, s_turn - 1), max(0, p_turn - 1), max(0, r_turn - 1), spent, hard)

minsp = math.inf
round(0, 50, boss_hp, 500, 0, 0, 0, 0)
p1 = minsp

minsp = math.inf
round(0, 50, boss_hp, 500, 0, 0, 0, 0, True)
p2 = minsp

output(p1, p2)