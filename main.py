import art
import game_data
import random

game_is_continue =True
curren_score = 0
while game_is_continue:
    f_person = random.choice(game_data.data)
    s_person = random.choice(game_data.data)
    if (s_person == f_person):
        f_person = random.choice(game_data.data)
    if f_person['follower_count'] > s_person['follower_count']:
        winner = f_person
    else:
        winner = s_person
    print(art.logo)
    print(f'Compare A:{f_person["name"]} {f_person["description"]} from {f_person["country"]}')
    print(art.vs)
    print(f'Compare B:{s_person["name"]} {s_person["description"]} from {s_person["country"]}')
    choise = input("Who has more followers(A/B)").lower()
    if(choise == 'a' and winner==f_person):
        curren_score += 1
        print(f'You right current score {curren_score}')
    elif(choise == 'b' and winner==s_person):
        curren_score += 1
        print(f'You right current score {curren_score}')
    else:
        print(f"Sorry, you lost, your score is {curren_score}")
        game_is_continue = False


