import random


def diff_RSP(person1, person1_choose, person2, person2_choose):
    tab_format = "\t" * 8
    if person1_choose == 'rock':
        if person2_choose == 'scissors':
            print(tab_format + "\033[1;31;46m%s\33[0m\tWIN" % person1)
        elif person2_choose == 'paper':
            print(tab_format + "\033[1;31;46m%s\33[0m\tWIN" % person2)
        else:
            print(tab_format + "\033[1;31;46mDRAW GAME\33[0m")
    elif person1_choose == 'scissors':
        if person2_choose == 'paper':
            print(tab_format + "\033[1;31;46m%s\33[0m\tWIN" % person1)
        elif person2_choose == 'rock':
            print(tab_format + "\033[1;31;46m%s\33[0m\tWIN" % person2)
        else:
            print(tab_format + "\033[1;31;46mDRAW GAME\33[0m")
    else:
        if person2_choose == 'rock':
            print(tab_format + "\033[1;31;46m%s\33[0m\tWIN" % person1)
        elif person2_choose == 'scissors':
            print(tab_format + "\033[1;31;46m%s\33[0m\tWIN" % person2)
        else:
            print(tab_format + "\033[1;31;46mDRAW GAME\33[0m")


dict = {'r': 'rock', 's': 'scissors', 'p': 'paper'}
print('*' * 80 + '\n' + '\t' * 4 + '\033[1;31;46mGUESS (rock、scissors、paper) with COMPUTER\33[0m' + '\n' + '*' * 80)
play_again = 'Y'
while not play_again == 'n':
    try:
        computer_choose = random.choice(list(dict.values()))
        person = input('please input a letter from(r,s,p) {r:rock  s:scissors  p:paper}  : ')
        while not person in list(dict.keys()):
            try:
                print('ATTENTION! The letter you enter is ineligible  ,please try again\n' + '*' * 80)
                person = input('please input a letter from(r,s,p) {r:rock  s:scissors  p:paper}  : ')
            except:
                pass
        you_choose = dict[person]
        print('You choose : \033[1;31;47m%s\33[0m' % you_choose)
        print('Computer choose : \033[1;31;47m%s\33[0m' % computer_choose)
        diff_RSP('COMPUTER', computer_choose, 'YOU', you_choose)
        print('*' * 80)

        play_again = input('Play again? (input n for stop): ')
    except:
        pass
else:
    print('*' * 80 + '\n' + "\t" * 8 + "\033[1;31;46mGAME OVER\33[0m")
