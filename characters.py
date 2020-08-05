"""
Eesa Aamer 
ICS4U
20/12/19
Assignment 6 - Part 2
This program contains the classes the define character properties, attributes and methods. Both classes
of characters have a base class, that contains basic properties that all characters from the class
inherit. Each character contains their own unique attacks. The difference between the two classes is that
Marvel characters have more options for attacks, which typically do more damage than DC attacks. However,
DC characters have a stronger shield, alongside a confidence trait, which can be used to multiply
the strength of their attacks. Also, the damage that Marvel characters make are not always the same,
it is randomized to even the playing field with the DC characters. 
"""

import random
# Marvel base character class
class Marvel_Character:
    def __init__(self, name, max_hp, shield):
        self.name = name
        self.max_hp = max_hp
        self.shield = shield
    
    def damage(start, end): 
        """ 
        (int, int) --> int
        Returns a random integer that lies between the two arguments.
        >>> 1,4 
        3
        >>> 4, 1023
        67
        """
        hit_points = random.randint(start, end)
        return hit_points

    def __repr__(self): 
        """ Returns the stats of the character created"""
        return "{self.max_hp} HP, {self.shield} Shield Strength".format(self=self)

# Iron Man character class 
class IronMan(Marvel_Character):
    def __init__(self, name, max_hp, shield):
        super().__init__(name, max_hp, shield) # Inheriting from parent class 
    
    def Unibeam(self, opponent): # Defines an attack function
        """
        (instance, instance) --> string
        Returns a string indicating how much damage was done to both characters when Iron Man uses Unibeam.
        """
        damage1 = IronMan.damage(10, 14) # Randomizes a damage point counter
        damage2 = IronMan.damage(15, 20) # Randomizes a damage point counter
        if opponent.shield > 0: # Checks if shield is still stable 
            opponent.max_hp -= damage1 # Opponent health is decreased
            opponent.shield -= damage1 # Opponent shield strength is decreased 
            # Prints scenario to console
            print("\nIron Man uses Unibeam! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage1))
        else:
            opponent.max_hp -= damage2 # Opponent health is decreased
             # Prints scenario to console
            print("\nIron Man uses Unibeam! and {} shield is down! Health goes down by {} HP".format(opponent.name, damage2))

    def FocusShot(self, opponent): # Defines an attack function
        """
        (instance, instance) --> string
        Returns a string indicating how much damage was done to both characters when Iron Man uses FocusShot.
        """
        self.max_hp -= 8 # Takes away health from user
        damage1 = IronMan.damage(2, 6) # Randomizes a damage point counter
        damage2 = IronMan.damage(10, 13) # Randomizes a damage point counter
        if opponent.shield > 0: # Checks if shield is still stable
            opponent.max_hp -= damage1 # Opponent health is decreased
            opponent.shield -= damage1 # Opponent shield strength is decreased
            # Prints scenario to console
            print("\nIron Man uses Focus Shot! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage1))
            print("Iron Man loses 8 HP during the attack\n")
        else:
            opponent.max_hp -= damage2
            # Prints scenario to console
            print("\nIron Man uses Unibeam! and {} shield is down! Health goes down by {} HP".format(opponent.name, damage2))
            print("Iron Man loses 8 HP during the attack\n")

    def SmartBomb(self, opponent): # Function format follows format used by functions before
        """
        (instance, instance) --> string
        Returns a string indicating how much damage was done to both characters when Iron Man uses SmartBomb.
        """
        self.max_hp -= 10
        damage1 = IronMan.damage(5, 8)
        damage2 = IronMan.damage(20, 25)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage1
            print("\nIron Man uses Smart Bomb! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage1))
            print("Iron Man loses 10 HP during the attack\n")
        else:
            opponent.max_hp -= damage2
            print("\nIron Man uses Smart Bomb! and {} shield is down! Health goes down by {} HP".format(opponent.name, damage2))
            print("Iron Man loses 10 HP during the attack\n")

    def RepulsorBlast(self, opponent): # Function format follows format used by functions before
        """
        (instance, instance) --> string
        Returns a string indicating how much damage was done to both characters when Iron Man uses RepulsorBlast.
        """
        self.max_hp -= 5
        damage1 = IronMan.damage(6, 9)
        damage2 = IronMan.damage(19, 21)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage1
            print("\nIron Man uses Repulsor Blast! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage1))  
        else:
            opponent.max_hp -= damage2
            print("\nIron Man uses Repulsor Blast! and {} shield is down! Health goes down by {} HP".format(opponent.name, damage2))
    
    move_desc = ['Unibeam [1]\n Weak when opponent has a shield, however deadly if opponent is exposed', 
                'Focus Shot [2]\n Regular attack, however does moderate damage to user', 
                'Smart Bomb [3]\n Powerful attack if opponent has no shield, however does significant damage to user', 
                'Repulsor Blast [4]\n More powerful than Focus Shot, and does less damage to user'] # Description of all attacks from character
    move_set = {"1": Unibeam, "2": FocusShot, "3": SmartBomb, "4": RepulsorBlast} # Set of attacks that can be called using user input


# Captain America character class 
class CaptainAmerica(Marvel_Character): # Class follows idential format as classes before
    
    def __init__(self, name, max_hp, shield):
        super().__init__(name, max_hp, shield)
    
    def AmericanShield(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the increase in shield points when Captain America uses American Shield.
        """
        self.shield += 20
        print("\nCaptain America strengthens his shield by 20 points\n")
    
    def ShieldThrow(self, opponent): 
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Captain America uses Shield Throw.
        """
        self.shield -= 8
        damage1 = CaptainAmerica.damage(2, 4)
        damage2 = CaptainAmerica.damage(10, 12)
        damage3 = CaptainAmerica.damage(12, 14)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage2
            print("\nCaptain America uses Shield Throw! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage2))
            print("Captain America's shield is damaged by 8 points in the process\n")
        else:
            opponent.max_hp -= damage3
            print("\nCaptain America uses Shield Throw and {} shield is down! Health goes down by {} HP".format(opponent.name, damage3))
            print("Captain America's shield is damaged by 8 points in the process\n")

    def PatrioticJab(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Captain America uses Patriotic Jab.
        """
        damage1 = CaptainAmerica.damage(5, 7)
        damage2 = CaptainAmerica.damage(14, 16)
        self.max_hp -= 5
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage1
            print("\nCaptain America uses Patriotic Jab! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage1))
            print("Captain America loses 5 HP in the process\n")
        else:
            opponent.max_hp -= damage2
            print("\nCaptain America uses Patriotic Jab and {} shield is down! Health goes down by {} HP".format(opponent.name, damage2))
            print("Captain America loses 5 HP in the process\n")

    def FalconKick(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Captain America uses Falcon Kick.
        """
        self.max_hp -= 10
        damage1 = CaptainAmerica.damage(10, 12)
        damage2 = CaptainAmerica.damage(21, 24)
        damage3 = CaptainAmerica.damage(24, 27)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage2
            print("\nCaptain America uses Falcon Kick! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage1))
            print("Captain America loses 10 HP in the process\n")
        else:
            opponent.max_hp -= damage3
            print("\nCaptain America uses Falcon Kick and {} shield is down! Health goes down by {} HP".format(opponent.name, damage3))
            print("Captain America loses 10 HP in the process\n")


    move_desc = ['American Shield [1]\n Increases users shield strength', 
                'Shield Throw [2]\n Does moderate damage to opponent, however decreases user shield strength', 
                'Patriotic Jab [3]\n Can do significant damage to opponent, however also does moderate damage to user', 
                'Falcon Kick [4]\n Deadly attack, however does significant damage to user']  
    move_set = {"1": AmericanShield, "2": ShieldThrow, "3": PatrioticJab, "4": FalconKick}


# Black Widow character class 
class BlackWidow(Marvel_Character): # Class follows idential format as classes before
    def __init__(self, name, max_hp, shield):
        super().__init__(name, max_hp, shield)
    
    def Taser(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Black Widow uses Taser.
        """
        damage1 = BlackWidow.damage(1, 4)
        damage2 = BlackWidow.damage(14, 17)
        damage3 = BlackWidow.damage(3, 5)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage2
            print("\nBlack Widow uses Taser! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage2))
        else:
            opponent.max_hp -= damage3
            print("\nBlack Widow uses Taser and {} shield is down! Health goes down by {} HP".format(opponent.name, damage3))
    
    def Spy(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Black Widow uses Spy.
        """
        self.shield += 8
        opponent.shield -= 10
        print("\nBlack Widow uses Spy! She gains 8 shield points while {} loses 10".format(opponent.name))

    def DoubleLegTakedown(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Black Widow uses Double Leg Takedown.
        """
        self.max_hp -= 4
        damage1 = BlackWidow.damage(5, 7)
        damage2 = BlackWidow.damage(10, 15)
        damage3 = BlackWidow.damage(13, 18)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage2
            print("\nBlack Widow uses Double Leg Takedown! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage2))
            print("Black Widow loses 4 HP in the process\n")
        else:
            opponent.max_hp -= damage3
            print("\nBlack Widow uses Taser and {} shield is down! Health goes down by {} HP".format(opponent.name, damage3))
            print("Black Widow loses 5 HP in the process\n")
            

    def RussianElbowStrike(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Black Widow uses Russian Elbow Strike.
        """
        self.max_hp -= 8
        damage1 = BlackWidow.damage(10, 12)
        damage2 = BlackWidow.damage(19, 22)
        damage3 = BlackWidow.damage(22, 25)
        if opponent.shield > 0:
            opponent.max_hp -= damage1
            opponent.shield -= damage2
            print("\nBlack Widow uses Russian Elbow Strike! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, damage1, damage2))
            print("Black Widow loses 8 HP in the process\n")
        else:
            opponent.max_hp -= damage3
            print("\nBlack Widow uses Taser and {} shield is down! Health goes down by {} HP".format(opponent.name, damage3))
            print("Black Widow loses 8 HP in the process\n")


    move_desc = ['Taser [1]\n Does small damage to opponent health, however does significant damage to shield strength', 
                'Spy [2]\n Increases user shield and decreases opponent shield strength', 
                'Double Leg Takedown [3]\n Moderate attack, does small damage to user health', 
                'Russian Elbow Strike [4]\n Powerfull attack, does significant damage to user health']     
    move_set = {"1": Taser, "2": Spy, "3": DoubleLegTakedown, "4": RussianElbowStrike}

# DC base character class 
class DC_Character: 
    def __init__(self, name, max_hp, shield, confidence):
        self.name = name
        self.max_hp = max_hp
        self.shield = shield
        self.confidence = confidence

        # Damage is based on confidence trait of each character 

    def __repr__(self): # Describes character stats 
        return "{self.max_hp} HP, {self.shield} Shield Strength, {self.confidence} Confidence Boost".format(self=self)

# Batman character class
class Batman(DC_Character):
    def __init__(self, name, max_hp, shield, confidence):
        super().__init__(name, max_hp, shield, confidence) # Inherits from parent class 

    def MindGames(self, opponent): # Defines attack function
        """
        (instance, instance) --> string
        Returns a string indicating the increase in character confidence when Batman uses Mind Games.
        """
        self.confidence *= 1.25 # Increases confidence trait by 25% 
        opponent.shield -= (10 * self.confidence) # Decreases opponent shield strength by 10 x character confidence
        # Displays scenario result to console 
        print("\nBatamn meditates, boosting his confidence by 25%, while lowering his {} shield by {} points\n".format(opponent.name, str((10 * self.confidence))))
    
    def BatarangSwipe(self, opponent): # Function follows format of previous functions 
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Batman uses Batarang Swipe.
        """
        self.max_hp -= 2
        if opponent.shield > 0:
            opponent.max_hp -= (2 * self.confidence)
            opponent.shield -= (7 * self.confidence)
            print("\nBatman uses Batarang Swipe! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, (5 * self.confidence), (7 * self.confidence)))
            print("Batman injures himself, losing 2 health points\n")
        else:
            opponent.max_hp -= (10 * self.confidence)
            print("\nBatman uses Batarang Swipe and {}'s shield is down! Health goes down by {} HP".format(opponent.name, (5 * self.confidence)))
            print("Batman injures himself, losing 2 health points\n")

    def RoundhouseKick(self, opponent): # Function follows format of previous functions 
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Batman uses Roundhouse Kick.
        """
        self.max_hp -= 10
        if opponent.shield > 0:
            opponent.max_hp -= (2 * self.confidence)
            opponent.shield -= (13 * self.confidence)
            print("\nBatman uses Roundhouse Kick! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, (10 * self.confidence), (13 * self.confidence)))
            print("Batman injures himself, losing 10 health points\n")
        else:
            opponent.max_hp -= (15 * self.confidence)
            print("\nBatman uses Roundhouse Kick and {}'s shield is down! Health goes down by {} HP".format(opponent.name, (15 * self.confidence)))
            print("Batman injures himself, losing 10 health points\n")

    move_desc = ['Mind Games [1]\n User meditates and boosts his confidence while lowering opponents shield', 
                'Batarang Swipe [2]\n Small attack, user takes minimal damage', 
                'Roundhouse Kick [3]\n Powerful attack, user takes significant damage '] # Descriptions of all attacks 
    move_set = {"1": MindGames, "2": BatarangSwipe, "3": RoundhouseKick} # Set of moves so that user input can trigger them 

# Wonder Woman character class
class WonderWoman(DC_Character): # Class follows format of previous classes 
    def __init__(self, name, max_hp, shield, confidence):
        super().__init__(name, max_hp, shield, confidence)

    def AmazonsRise(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the increase in character confidence when Wonder Woman uses Amazon's Rise.
        """
        self.confidence *= 1.10
        opponent.shield -= (10 * self.confidence)
        print("\nWonder Woman meditates, boosting her confidence by 25%, while lowering her {} shield by {} points\n".format(opponent.name, str((10 * self.confidence))))
    
    def LassoSlam(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Wonder Woman uses Lasso Slam.
        """
        self.max_hp -= 4
        if opponent.shield > 0:
            opponent.max_hp -= (2 * self.confidence)
            opponent.shield -= (10 * self.confidence)
            print("\nWonder Woman uses Lasso Slam! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, (2 * self.confidence), (10 * self.confidence)))
            print("Wonder Woman injures herself, losing 4 health points\n")
        else:
            opponent.max_hp -= (12 * self.confidence)
            print("\nWonder Woman uses Lasso Slam and {} shield is down! Health goes down by {} HP".format(opponent.name, (12 * self.confidence)))
            print("Wonder Woman injures herself, losing 4 health points\n")
    
    def WarriorsJab(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Wonder Woman uses Warriors Jab.
        """
        self.max_hp -= 15
        if opponent.shield > 0:
            opponent.max_hp -= (1 * self.confidence)
            opponent.shield -= (17 * self.confidence)
            print("\nWonder Woman uses Warriors Jab {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, (1 * self.confidence), (19 * self.confidence)))
            print("Wonder Woman injures herself, losing 15 health points\n")
        else:
            opponent.max_hp -= (19 * self.confidence)
            print("\nWonder Woman uses Warriors Jab and {} shield is down! Health goes down by {} HP".format(opponent.name, (19 * self.confidence)))
            print("Wonder Woman injures herself, losing 15 health points\n")
        
    move_desc = ['Amazons Rise [1]\n User meditates and boosts her confidence while lowering opponents shield ', 
                'Lasso Slam [2]\n Small attack, user takes minimal damage', 
                'Warriors Jab [3]\n Powerful attack, user takes significant damage']
    move_set = {"1": AmazonsRise, "2": LassoSlam, "3": WarriorsJab}

class Superman(DC_Character): # Class follows format of previous classes 
    def __init__(self, name, max_hp, shield, confidence):
        super().__init__(name, max_hp, shield, confidence)

    def ManOfSteel(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the increase in character confidence when Superman uses Man of Steel.
        """
        self.confidence *= 1.4
        opponent.shield -= (5 * self.confidence)
        print("\nSuperman meditates, boosting her confidence by 25%, while lowering her {} shield by {} points\n".format(opponent.name, str((10 * self.confidence))))
    
    def KryptonianStrike(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Superman uses Kryptonian Strike
        """
        self.max_hp -= 10
        if opponent.shield > 0:
            opponent.max_hp -= (3 * self.confidence)
            opponent.shield -= (10 * self.confidence)
            print("\nSuperman uses Kryptonian Strike! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, (3 * self.confidence), (10 * self.confidence)))
            print("Superman injures himself, losing 10 health points\n")
        else:
            opponent.max_hp -= (20 * self.confidence)
            print("\nSuperman uses Kryptonian Strike and {} shield is down! Health goes down by {} HP".format(opponent.name, (20 * self.confidence)))
            print("Superman injures himself, losing 10 health points\n")
    
    def FistofJustice(self, opponent):
        """
        (instance, instance) --> string
        Returns a string indicating the damage done to both characters when Batman Fist of Justic.
        """
        self.max_hp -= 20
        if opponent.shield > 0:
            opponent.max_hp -= (9 * self.confidence)
            opponent.shield -= (20 * self.confidence)
            print("\nSuperman uses Fist of Justice! {}'s health goes down {} HP and shield goes down {} points".format(opponent.name, (9 * self.confidence), (20 * self.confidence)))
            print("Superman injures himself, losing 20 health points\n")
        else:
            opponent.max_hp -= (22 * self.confidence)
            print("\nSuperman uses Kryptonian Strike and {} shield is down! Health goes down by {} HP".format(opponent.name, (22 * self.confidence)))
            print("Superman injures himself, losing 20 health points\n")

    move_desc = ['Man Of Steel [1]\n User meditates and boost his confidence while lowering opponents shield', 
                'Kryptonian Strike [2]\n Small attack, user takes minimal damage', 
                'Fist of Justice [3]\n Powerful attack, user takes significant damage']
    move_set = {"1": ManOfSteel, "2": KryptonianStrike, "3": FistofJustice}