import random
import more_itertools

print('')
print('------------------------------------------------Lets play roulette--------------------------------------------------------')
print('')
print('Rules:')
print('      You have unlimited amount of chips at each roulette spin. You can place your chips on a single number, '
      'on the first, \n      second or third set of 12 numbers or bet on Red or Black. You can place as many chips as you want each spin.\n      At the end u will see '
      'your total chips used in the spin and you profit or loss. You can do as many spin as u want.')
print('')
print('-------------------------------------------GOOD LUCK AND HAVE FUN---------------------------------------------------------')


def restart():

    singlenumberlist = [0, ]
    singlenumberamountbet = [0, ]
    onetwelvenumberlist = []
    onetwelveamountbet = []
    twelvetwentynumberlist = []
    twelvetwentybetamount = []
    twentythirtynumberlist = []
    twentythirtybetamount = []
    redbetamount = []
    color = []
    blackbetamount = []

    def betting_round():
            global spin
            while True:
                try:
                    print('')
                    bet = int(input('How many chips u want to bet now?: '))
                    if bet > 0:
                        break
                    else:
                        print('Can not be negative or zero.')
                except ValueError:
                    print('Enter a valid number')
                    continue
            print('-------------------PLACE YOUR BET------------------')
            print('-------->   1.  Single number bet.')
            print('-------->   2.  First 12 numbers from   1-12.')
            first12 = list(range(1, 13))
            print('-------->   3.  Second 12 numbers from  13-24.')
            second12 = list(range(13, 25))
            print('-------->   4.  Last 12 numbers from    25-36.')
            third12 = list(range(25, 37))
            print('-------->   5.  Red or Black numbers.')
            while True:
                try:
                    choice = int(input('Chose where to place your chips: Enter 1,2,3,4 or 5: '))
                    if choice == 0:
                        print('Cant be 0')
                    if choice > 5:
                        print('Choose 1,2,3,4 or 5')
                    if 0 < choice < 6:
                        break
                except ValueError:
                    print('Enter a valid choice')
            if choice == 1:
                while True:
                    try:
                        single = int(input('Where you want to put your chips from 0 to 36?: '))
                        if single < 37:
                            singlenumberlist.append(single)
                            singlenumberamountbet.append(bet)
                            # print(singlenumberamountbet)
                            # print(singlenumberlist)
                            # print(sum(singlenumberamountbet))
                            print('Your ' + str(bet) + ' chips are on the number ' + str(single) + ' for now')
                            break
                        if single > 37:
                            print('Not that many numbers on the roulette!')
                    except ValueError:
                        print('Enter a number from 0 to 36')
            if choice == 2:
                print('Ur chips are on the numbers from 1 to 12')
                onetwelvenumberlist.append(first12)
                onetwelveamountbet.append(bet)
                # print(onetwelvenumberlist)
                # print(onetwelveamountbet)
                # print(sum(onetwelveamountbet))
            if choice == 3:
                print('Ur chips are on the numbers from 13 to 24')
                twelvetwentynumberlist.append(second12)
                twelvetwentybetamount.append(bet)
                # print(twelvetwentynumberlist)
                # print(twelvetwentybetamount)
                # print(sum(twelvetwentybetamount))
            if choice == 4:
                print('Ur chips are on the numbers from 25 to 36')
                twentythirtynumberlist.append(third12)
                twentythirtybetamount.append(bet)
                # print(twentythirtynumberlist)
                # print(twentythirtybetamount)
                # print(sum(twentythirtybetamount))
            if choice == 5:
                while True:
                    red_or_black = str(input('Wanna put your chips on red or black? (answer red o black): '))
                    try:
                        if red_or_black == 'red':
                            print('Ur bet is on Red!')
                            color.append(red_or_black)
                            # print(color)
                            redbetamount.append(bet)
                            # print(redbetamount)
                            # print(sum(redbetamount))
                            break
                        if red_or_black == 'black':
                            print('Ur bet is on Black!')
                            color.append(red_or_black)
                            # print(color)
                            blackbetamount.append(bet)
                            # print(blackbetamount)
                            # print(sum(blackbetamount))
                            break
                        elif red_or_black != 'red' or red_or_black != 'black':
                            print('Enter either red or black!')
                    except NameError:
                        print('Enter either red or black!')
            while True:
                try:
                    another_bet = str(input("You have unlimited chips, do you wanna bet more? y/n: "))
                    if another_bet == 'y':
                        betting_round()
                        break
                    if another_bet == 'n':
                        print('Ok, Betting has ended. Good luck on the spin!')
                        print('')
                        print('')
                        break
                    else:
                        print('Answer with y or n: ')
                except NameError:
                    print('Please enter a valid y or n answer.')

    betting_round()
    # print(singlenumberamountbet)
    # print(singlenumberlist)
    # print(sum(singlenumberamountbet))
    # print(onetwelveamountbet)
    # print(onetwelvenumberlist)
    # print(sum(onetwelveamountbet))
    # print(twelvetwentybetamount)
    # print(twelvetwentynumberlist)
    # print(sum(twelvetwentybetamount))
    # print(twentythirtybetamount)
    # print(twentythirtynumberlist)
    # print(sum(twentythirtybetamount))
    # print(color)
    # print(blackbetamount)
    # print(redbetamount)
    onetwelvenumberlist = list(more_itertools.collapse(onetwelvenumberlist))
    twelvetwentynumberlist = list(more_itertools.collapse(twelvetwentynumberlist))
    twentythirtynumberlist = list(more_itertools.collapse(twentythirtynumberlist))
    # spin starts here
    print('JEU SONT FAIT RIEN VA PLUS!!!     BALL IS ROLLING      JEU SONT FAIT RIEN VA PLUS!!!')
    spin = random.randint(0, 36)
    print('---------------------------- The winning number is ' + str(spin) + '--------------------------------')
    print('')
    print('')
    if spin == 0:
        print('The worst number on the roulette came out. YOU LOST ALL YOUR CHIPS!')
        while True:
            try:
                play_again = input('Do you want to do another spin? answer with y or n: ')
                if play_again == 'y':
                    restart()
                    break
                if play_again == 'n':
                    print('Thanks for playing. Vaffanculo mo.')
                    exit()
            except ValueError:
                print('Enter either y or n!')
    else:
        pass
    if spin in singlenumberlist:
        # print(singlenumberlist.index(spin))
        # print(singlenumberamountbet[singlenumberlist.index(spin)])
        winning = 36 * singlenumberamountbet[singlenumberlist.index(spin)]
        print('Your have ' + str(singlenumberamountbet[singlenumberlist.index(spin)]) + ' on the single winning number!')
        print('Your winning is ' + str(winning))
    else:
        print('The winning number is: ' + str(spin) + ' and you didnt bet on it alone.')
        winning = 0
    if spin in onetwelvenumberlist:
        print('The ball landed in the first 12!')
        winning12 = 12 * sum(onetwelveamountbet)
        print('You have: ' + str(sum(onetwelveamountbet)) + ' on the first 12 numbers and your winning is: ' + str(winning12))
    else:
        print('The winning number is: ' + str(spin) + ' your chips are not in the first 12 numbers.')
        winning12 = 0
    if spin in twelvetwentynumberlist:
        print('The ball landed in the numbers from 12 to 24!')
        winning24 = 12 * sum(twelvetwentybetamount)
        print('You have: ' + str(sum(twelvetwentybetamount)) + ' on the 12 to 24 numbers and your winning is: ' + str(winning24))
    else:
        print('The winning number is: ' + str(spin) + ' your chips are not from 12 to 24 numbers.')
        winning24 = 0
    if spin in twentythirtynumberlist:
        print('The ball landed in the numbers from 24 to 36!')
        winning36 = 12 * sum(twentythirtybetamount)
        print('You have: ' + str(sum(twentythirtybetamount)) + ' on the 24 to 36 numbers and your winning is: ' + str(winning36))
    else:
        print('The winning number is: ' + str(spin) + ' your chips are not from 24 to 36 numbers.')
        winning36 = 0
    if spin % 2 == 0:
        print('The number is red!')
        winningcolor = sum(redbetamount) * 2
        print('The chips u have on red are ' + str(sum(redbetamount)) + ' and you double them for a total of: ' + str(winningcolor))
        winningcolor1 = 0
    else:
        print('The number is black!')
        winningcolor1 = sum(blackbetamount) * 2
        print('The chips u have on black are ' + str(sum(blackbetamount)) + ' and you double them for a total of:: ' + str(winningcolor1))
        winningcolor = 0
    totalbet = sum(singlenumberamountbet) + sum(onetwelveamountbet) + sum(twelvetwentybetamount) + sum(twentythirtybetamount) + sum(redbetamount) + sum(blackbetamount)
    print('')
    print('------------->>>   On this spin you bet a total of: ' + str(totalbet))
    totalwinning = winning + winningcolor + winningcolor1 + winning12 + winning24 + winning36
    print('... and on this spin your total winnings are ' + str(totalwinning) + '  <<<---------------------')
    print('')
    profit = totalwinning - totalbet
    if profit > 0:
        print('')
        print(' --------------------->>>   The profit of this spin is: ' + str(profit))
    else:
        print('')
        print('---------------------->>>   In this spin you LOST: ' + str(profit))
    while True:
        try:
            print('')
            play_again = input('Do you want to do another spin? answer with y or n: ')
            if play_again == 'y':
                restart()
                break
            if play_again == 'n':
                print('')
                print('Thanks for playing. Vaffanculo mo.')
                exit()
        except ValueError:
            print('Enter either y or n!')


restart()
