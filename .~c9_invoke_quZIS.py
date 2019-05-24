from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    
    def enter(self):
        print("Scene has not been set up yet.")
        exit(1)
    
class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map = scene_map
                      
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        # be sure to print out the last scene
        current_scene.enter()
        
class Death(Scene):
    
    quips = [
        "You got shot in the face.",
        "You really suck at this game.",
        "You are actually hot garbage at this game.",
        "Holy cow how bad can you be at this game?",
        "My grandma can do better than you."
        
        ]
    
    def enter(self):
        pass
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)
class SpaceShip(Scene):
    
    def enter(self):
        pass
        print(dedent("""
            The Space Pirates have invaded your planet and they destroyed your whole planet.
            You are the only survivor of your kind on your planet. Your last mission is to destroy
            the Space Pirates and they took your planet secret to destroying the whole universe and
            you have to get it back at all cost. You saw their ship about to take off, so you dash
            towards their ship and Brukz, a soilder of The Space Pirates stopped you. Brukz is a tall
            red octopus, black gooey teeth, and a eyepatch that has a laser attach to it. 
            """))
        
        action = input("> ")
        
        if action == "fire!":
            print(dedent("""
                You quickly pull out your blaster and fire at Brukz. He dodges it and shoots you
                in the ribs and you got injured then he shoots you multiple times and you die and
                he took your body and gave it to his to his friend and his friend ate you.
                """))
            return 'death'
            
        elif action == "Block!":
            print(dedent("""
                You take out your magic barrier and block Brukz shot and you shoot him in his eye.
                Brukz started screaming in pain and you shoot him again in his other eye and he dropped
                to the ground and blood started coming out both of his eyes and he died to blood lost.
                """)) 
            return 'Access to the ship'
        
        else:
            print("I Don't Speak English")
            return 'Spaceship'
            
class SpaceshipCode(Scene):
    
    def enter(self):
        pass
        print(dedent("""
            You starting running to the ship and you dolphin dive into the ship last second before the door. 
            You crouch behind and box and you scan the room for more evil doers.
            You see all of the evil doers leave the room that your in to a whole different room
            and you see one placing down your planet secret to destroy the universe and once he leave
            you run silently to the box. You find out the box has a 3 digit code and if you get it wrong 4 times
            then the box makes a loud noise.
            """)) 
        
        code = f"{randint(1,4)}{randint(1,4)}{randint(1,4)}"
        guess = input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
            
        if guess == code:
            print(dedent("""
                A green text appears and you get access to the box with your planet secret. 
                A white fog appears out of the box and you grab your planet secret and you
                blast the door open and you jump before the spaceship started deploying. To
                destroy the universe you have to activate it at the Cathedral. 
                """))
            return 'Cathedral'
        else:
            print(dedent("""
                The box makes a loud noise alerting all of the evil doers and they all rush to you. 
                You can't kill them all, so you got shot multiple times by the evil doers while taking 
                only 4 down and you die.
                """))
            return 'death'
            
            
class  Cathedral(Scene):
    
    def enter(self):
        pass
        print(dedent("""
            You bust open the Cathedral door with your blaster and you place the
            planet secret in the middle of the circle. You hear footsteps outside
            and a bunch of evil doers start shooting at you but you dodge all of the shots
            and the last shot almost hit you, but you quickly use your magic barrier. They keep
            shooting at you and you keep dodging and you started getting tired so you hide behind a broken
            stone wall
            """))
            
        action = input("> ")
        
        if action == "Keep Dodging"
           print(dedent("""
                You slowly start to get tired from dodging all of the lasers and you get shot in the legs, arms, ribs,
                and the head. You bleed out and die and they throw you into space back on their spaceships. 
                """))
            return 'death'
            
        elif action == "Grerrier":
            print(dedent("""
                You use your magic barrier to block all the shots and you throw a magic grenade. The enemy doesn't
                see the magic grenade because they are focus on killing you. The enemy gets blown up and you are safe
                to destroy the whole universe. 
                """))
            return 'destroying the whole universe'
        
    
class UniverseDestroyed(Scene):
    
    def enter(self):
        pass
        print(dedent("""
            You start your trial on destroying the whole universe but you start to see a list and the list
            says,
            1.) Бецоме Год
            2.) Дие 
            you can't read the list because its in a language you don't know. You have to
            put a number in from the list and see what happens.
            """))
        weird_list = randint(1,2)
        guess = input("[list #]> ")
        
        if int(guess) != weird_list:
            print(dedent("""
                You choose {guess} and you become god and you can create your own
                world with your own people and basically do anything you want. You
                are the ultimate being.
                """))
            return 'Mission Complete'
        else:
            print(dedent("""
                You choose {guess} and you just suddenly start crumbling and you feel pain
                and you just vanish. 
                """))
                
            return 'death'
    
class Finished(Scene):
    
    d
    
class Map(object):
    
    # def __init__(self, start_scene):
      #   pass
      #   pass
    # def next_scene(self, screne_name):
      #   pass
    # def opening_scene(self):
      #   pass
    
a_map = Map('centra_corridor')
a_game = Engine(a_map)
a_game.play()