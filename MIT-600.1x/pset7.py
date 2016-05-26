import random #as rand
import string

# Problem 7-1: The Adoption Center
class AdoptionCenter(object):
    """ The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        t1 = float(location[0])
        t2 = float(location[1])
        self.location = (t1, t2)
    def get_number_of_species(self, animal): 
        try:
            return self.species_types[animal]
        except KeyError:
            return 0
    def get_location(self):
        return self.location
    def get_species_count(self):
        return self.species_types.copy()
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if self.species_types[species] > 0:
            self.species_types[species] -= 1
        if self.species_types[species] == 0:
            del self.species_types[species]

# Problem 7-2: Meet the Adopter                        
class Adopter(object):
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
        return self.name
    def get_desired_species(self):
        return self.desired_species
    def get_score(self, adoption_center):
        return 1.0 * adoption_center.get_number_of_species(self.desired_species)

# Problem 7-3: The Flexible and Fearful Adopters
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        Adopter.__init__(self, name, desired_species)
        self.considered_species = considered_species
    def get_score(self, adoption_center):
        num_other = 0
        for animal in self.considered_species:
            num_other += adoption_center.get_number_of_species(animal)
        return Adopter.get_score(self, adoption_center) + .3 * num_other
    
class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species, feared_species):
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
    def get_score(self, adoption_center):
        return max(Adopter.get_score(self, adoption_center) - .3 * adoption_center.get_number_of_species(self.feared_species), 0.0)

# Problem 7-4: AllergicAdopter and MedicatedAllergicAdopter
class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
    def get_score(self, adoption_center):
        num_allerg = 0
        for animal in self.allergic_species:
            num_allerg += adoption_center.get_number_of_species(animal)
        if num_allerg > 0:
            return 0.0
        else:
            return Adopter.get_score(self, adoption_center)

class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
    def get_score(self, adoption_center):
        effectiveness = []
        for allergy in self.allergic_species:
            if adoption_center.get_number_of_species(allergy) > 0:
                effectiveness.append(self.medicine_effectiveness[allergy])
        try:
            return min(effectiveness) * Adopter.get_score(self, adoption_center)
        except:
            return Adopter.get_score(self, adoption_center)

# Problem 7-5: The Sluggish Adopter
class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = location
    def get_linear_distance(self, to_location):
        from math import sqrt
        return sqrt ((self.location[0] - to_location[0])**2 + (self.location[1] - to_location[1])**2)
    def get_score(self, adoption_center):
        distance = self.get_linear_distance(adoption_center.get_location())
        if distance < 1:
            return 1.0 * adoption_center.get_number_of_species(self.desired_species)
        elif distance < 3 and distance >= 1:
            return random.uniform(.7, .9) * adoption_center.get_number_of_species(self.desired_species)
        elif distance < 5 and distance >= 3:
            return random.uniform(.5, .7) * adoption_center.get_number_of_species(self.desired_species)
        else:
            return random.uniform(.1, .5) * adoption_center.get_number_of_species(self.desired_species)
        
# Probelm 7-6: Connecting Adopters and Adoption Centers    
def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    alphabetized = sorted(list_of_adoption_centers, key=lambda person: person.get_name())
    scores = []
    best_order = []
    for center in alphabetized:
        scores.append(adopter.get_score(center))
    while scores != []:
        i = scores.index(max(scores))
        best_order.append(alphabetized[i])
        #print alphabetized[i].get_name() + ' : ' + str(scores[i])
        scores.pop(i)
        alphabetized.pop(i)
    return best_order
           

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    alphabetized = sorted(list_of_adopters, key=lambda person: person.get_name())
    scores = []
    send_to = []
    for person in alphabetized:
        scores.append(person.get_score(adoption_center))
    for j in range(n):
        if scores == []:
            break
        else:
            i = scores.index(max(scores))
            send_to.append(alphabetized[i])
            scores.pop(i)
            alphabetized.pop(i)
    return send_to


