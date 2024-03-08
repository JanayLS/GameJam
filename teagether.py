from gasstation import *
from hp_checker import *
from GameJam import *
def story():
    x=0
    print("after entering the park you see a huge a rangement of attractions you guys cant wait")
    print(f'{friend1}\"ask which way that we goin\"')
    ride = input("which ride would you guys like to go to? bumpercars,ferris wheel, hall of mirrors or rollercoaster")
    while x <=1:
        if ride == 'bumpercars':
            print("place holder")
            x+=1
        elif ride == 'ferris wheel':
            print("place holder")
            x+=1
        elif ride == 'hall of mirrors':
            print("place holder")
            x+=1
        elif ride =='rollercoaster':
            print("place holder")
            x+=1
        elif ride == 'this way':
            print("holy mother of pearl\"the narrator\"yelled as lil nas x began to decend form the heavens above then suddley you see him grab a pole that leads to hell")
            print("you got theeeeee alive endng I guess, yeah yeah yeah lets just say you won")
            quit()
        else:
            print("maybe mispelled it, type one of the things in our selection")
            ride = input("which ride would you guys like to go to? bumpercars,ferris wheel, hall of mirrors or rollercoaster")

