import random

one_time_head = 0
two_time_head = 0
three_time_head = 0
four_time_head = 0
five_time_head = 0
six_time_head = 0
seven_time_head = 0
eight_time_head = 0
nine_time_head = 0
need_to_restart = 0
tosses = 0
consecutive_heads = 0
permutations = int(input('How many times u want to toss HEAD in a row: '))
while consecutive_heads != permutations:
    while True:
        random_coin_toss = random.randrange(0, 2)
        # print(random_coin_toss)
        tosses += 1
        if random_coin_toss == 1:
            if consecutive_heads == 1:
                one_time_head += 1
            if consecutive_heads == 2:
                two_time_head += 1
            if consecutive_heads == 3:
                three_time_head += 1
            if consecutive_heads == 4:
                four_time_head += 1
            if consecutive_heads == 5:
                five_time_head += 1
            if consecutive_heads == 6:
                six_time_head += 1
            if consecutive_heads == 7:
                seven_time_head += 1
            if consecutive_heads == 8:
                eight_time_head += 1
            if consecutive_heads == 9:
                nine_time_head += 1
            # print('After ', tosses, 'u got tail. You need to restart.')
            # print('Consecutive Head in this loop WAS ', consecutive)
            consecutive_heads = 0
            need_to_restart += 1
        if random_coin_toss == 0:
            consecutive_heads += 1
            if consecutive_heads == permutations:
                print('After ', tosses, 'tosses, the last', permutations, 'were HEAD in a row!')
                print('You had to restart', need_to_restart, 'times.')
                print('                       ---Restart report: ---\n ---> This report shows how many times in a row the sequences is hit before a fail and restart.')
                print('Example: 5 Head --> This number shows how many times is been reach 5 HEAD in a row and than hit Tail thus restart.')
                print('1 Head -->', one_time_head, '.... 2 Head -->', two_time_head, '.... 3 Head -->', three_time_head, '.... 4 Head -->', four_time_head, )
                print('5 Head -->', five_time_head, '  .... 6 Head -->', six_time_head, '.... 7 Head -->', seven_time_head, '.... 8 Head -->', eight_time_head, '.... 9 Head -->', nine_time_head, )
                break
