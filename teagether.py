from beginner import *
from Teagether_path import ferriswheel_op
from Teagether_path import buber_cars_op
from banna import *

def story():

    x=0
    print("after entering the park you see a huge a rangement of attractions you guys cant wait")
    print(f'{friend1} asked \" which way that we goin\"')
    ride = input("which ride would you guys like to go to? bumpercars,ferris wheel, hall of mirrors:")
    while True :
        if ride == 'bumpercars':
            buber_cars_op()
            break



        elif ride == 'ferris wheel':
            ferriswheel_op()
            break

        elif ride == 'hall of mirrors':
            trapper()
            break

        elif ride == 'this way':
            print("holy mother of pearl\"the narrator\"yelled as lil nas x began to decend form the heavens above then suddley you see him grab a pole that leads to hell")
            print("you got theeeeee alive endng I guess, yeah yeah yeah lets just say you won")
            quit()
        else:
            print("maybe mispelled it, type one of the things in our selection")
            ride = input("which ride would you guys like to go to? bumpercars,ferris wheel, hall of mirrors or rollercoaster:")

