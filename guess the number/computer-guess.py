import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != 'c':
            computer_guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {computer_guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = computer_guess - 1
        elif feedback == 'l':
            low = computer_guess + 1

    print(f'Bilgisayar senin {computer_guess} sayini dogru tahmin etti!')


computer_guess(10)