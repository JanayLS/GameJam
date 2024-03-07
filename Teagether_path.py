#
# Daniel Stots
# 3-7-24
# stick together path + endings
#

# users chose ferriswheel option.
# Some of this story is writen by Chat GBT
def ferriswheel_op():
    pass

# users chose buber-cars option.
def buber_cars_op():
    print("A you approach the bumper-cars area you noticed it's not normal is more like a arena.")
    print("""As you step into the abandoned bumper-cars arena though a barn like door, a thick mist hangs in the air,
    swirling around the decrepit vehicles like restless spirits. The once vibrant colors now appear muted and faded, 
    casting an eerie pall over the scene. The silence is broken only by the occasional creaking of metal and the faint
    echoes of laughter that seem to emanate from the shadows, creating an atmosphere of lingering dread and unease.\n""")
    buber_cars_loocking = input("Would you like to look around first? y/n")
    if buber_cars_loocking.lower() == 'y':
        print("")
    print("""Sudenly the barn door you shuts behind you. Then the laughter is getting loader and loader. You notes one 
        of the cars head lights flicker on. then the rest of them turnd on""")

filler_var_stick_together = True

if filler_var_stick_together == True:
    print("Ok guys were going to skick together.")
    print("We have to option to go to first the option 1 ferriswheel or option 2 the buber-cars?")
    together_path_1 = input("input 'op1' for the option 1 and 'op2' for option 2. ")
    while together_path_1.lower() != 'op1' or together_path_1.lower() != 'op2':
        if together_path_1.lower() == 'op1':
            print("Great idea! We should go to the ferriswheel first.")
            ferriswheel_op()
            break
        elif together_path_1.lower() == 'op2':
            print("Good idea! We should go to the buber-cars first.")
            buber_cars_op()
            break
        else:
            print("Sorry that was not one of the give out puts. please retry. ")
            together_path_1 = input("Error: Input 'op1' for the option 1 and 'op2' for option 2. ")