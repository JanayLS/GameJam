#
# Daniel Stots
# 3-7-24
# stick together path + endings
#
from Draft_1 import randomness
from GameJam_1 import friend1

# users chose ferriswheel option.
# Some of this story is writen by Chat GBT
def Teaghether_path_main():
    def ferriswheel_op():
        pass

    # users chose buber-cars option.
    def buber_cars_op():
        print("A you approach the bumper-cars area you noticed it's not normal is more like a arena.")
        print("""As you step into the abandoned bumper-cars arena though a barn like door, a thick mist hangs in the air,
        swirling around the decrepit vehicles like restless spirits. The once vibrant colors now appear muted and faded, 
        casting an eerie pall over the scene. The silence is broken only by the occasional creaking of metal and the faint
        echoes of laughter that seem to emanate from the shadows, creating an atmosphere of lingering dread and unease.
        you and your friends start look around.\n""")

        print("You found a key!")
        print("""As you step into the abandoned bumper-cars arena, the creaking barn door slams shut behind you, 
            sealing you inside with an ominous finality. The laughter that once seemed distant now grows louder, 
            echoing off the decrepit walls as if mocking your presence. Your heart races as you watch in disbelief as one 
            by one, the headlights of the bumper-cars flicker to life, casting eerie shadows across the empty space. 
            With a shiver running down your spine, you realize you're not alone in this haunted attraction, and the 
            sinister energy crackling in the air sends a chill through your very soul.\n""")

        print("""As their engines roar to life, one bumper-car lurches forward like a charging beast, its headlights 
            piercing the darkness with malevolent intent. With adrenaline coursing through your veins, you sprint towards 
            the barn door, clutching the key tightly in your trembling hand. Every step feels like an eternity 
            as the laughter grows deafening, drowning out the sound of your pounding heart... """)
        print(input("would you like to enter the key fastly or slowly? y/n "))

        if randomness() == True:
            print("""As you finally reach the door, your hands shake with urgency as you 
                 insert the key into the lock. With a twist, the lock clicks open, and relief floods through you as you 
                 swing the door wide. Your friends rush to your side, and together you stumble out into the cool night air, 
                 leaving the haunted bumper-cars behind you. As the door slams shut with a bang has the car slammed into the 
                 door, you breathe a sigh of relief, grateful to have escaped the clutches of the sinister attraction, your 
                 hearts pounding with adrenaline and the exhilaration of a narrow escape.""")

        elif randomness() == False:
            print(""" Finally reaching the door, you fumble with the lock, desperation lending speed to your movements. 
                But just as you manage to insert the key into the lock, a sudden jolt sends it flying from your grasp, 
                clattering to the ground just out of reach. In that moment of panicked hesitation, the bumper-cars close 
                in, their relentless pursuit sealing your fate in the chilling embrace of the haunted park....\n""")
            print("You have died. Thanks for playing!")

    filler_var_stick_together = True

    if filler_var_stick_together == True:
        print("Ok guys were going to skick together.")
        print("We have to option to go to first the option 1 ferriswheel or option 2 the buber-cars?")
        together_path_1 = input("input 'op1' for the option 1 and 'op2' for option 2. ")
        while together_path_1.lower() != 'op1' or together_path_1.lower() != 'op2':
            if together_path_1.lower() == 'op1':
                print("Great idea! We should go to the ferriswheel first.\n")
                ferriswheel_op()
                break
            elif together_path_1.lower() == 'op2':
                print("Good idea! We should go to the buber-cars first.\n")
                buber_cars_op()
                break
            else:
                print("Sorry that was not one of the give out puts. please retry. ")
                together_path_1 = input("Error: Input 'op1' for the option 1 and 'op2' for option 2. ")
