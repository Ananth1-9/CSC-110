'''
Ananth Mugundhan
CSC110
Project -1
a simple mad lib where this acts as the host
'''

def create_story(person_one, person_two, pet_name, animal,
                  place, adjective, verb, adverb):
    '''This function returns a story with the given words filled in.
    Args:
        person_one (str): name of the first person
        person_two (str): name of the second person
        pet_name (str): name of the pet
        animal (str): type of animal
        place (str): name of the place
        adjective (str): an adjective
        verb (str): a verb
        adverb (str): an adverb
    Returns:
        returns the story'''

    story_template = """{0} and {1} were best friends.
One day {0} and {1} decided to go on a
vacation to {2}. However, they didn't know
what to do with their {3} pet {4} named {5}.
{5} had been causing problems, due to constant {6}ing.
{0} found a sitter for their pet, and {7} went on the trip."""
    
    return story_template.format(person_one, person_two, place, adjective, 
                                 animal, pet_name, verb, adverb)

def main():
    '''The words that will be used in the story
      are defined here and the story is printed.
      '''
    
    # Define the words for the story
    person_one = "Joe"
    person_two = "Lily"
    pet_name = "Poncho"
    animal = "polar bear"
    place = "Madagascar"
    adjective = "Ridiculous"
    verb = "plank"
    adverb = "spastically"
    
    # Call the function to create the story
    final_story = create_story(person_one, person_two, pet_name, 
                                  animal, place, adjective, verb, adverb)

    # Print the completed story
    print(final_story)

# This line runs the main function when the script is executed
main()