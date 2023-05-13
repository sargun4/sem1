import random
l = ['Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain', 'Bread',
     'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach',
     'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt',
     'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event', 'Faith', 'Fault',
     'Field', 'Fight', 'Final']
print('No. of words to guess from =',len(l))
n = random.randint(0, len(l)-1)
a = l[n].lower() 

l1 = [0, 0, 0, 0, 0]
m = random.randint(0, 4) #for showing 1 letter of the word to be guessed
l1[m] = a[m]
# print("Random word from this list = ",a)
d = 0
print("-------GUESS THE WORD-------")
while (d < 6):
    print("guesses left:", 6-d)
    s1 = ''
    for i in l1:
        if i == 0:
            s1 += '-'
        else:
            s1 += i
    print(s1)
    guess_str = input("Enter guess string: ")
    chars = set([])

    if guess_str == a:
        print("YOU WON")
        print(a)
        break

    else:

        for i in range(5):
            if a[i] == guess_str[i]:
                l1[i] = a[i]
            elif guess_str[i] in a and guess_str[i] not in l1: #for other characters present in str which r not at correct place
                chars.add(guess_str[i])
            else:
                pass

    print("Other characters present:", chars)

    d += 1
if d == 6:
    print("-----GUESSES EXPIRED-----")
else:
    pass
