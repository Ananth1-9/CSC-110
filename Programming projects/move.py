'''
Ananth Mugundhan
CSC110
Project -1
a simple mad lib where this acts as the host
'''
def create_story(person_one, street_name, person_two,
                  object_name, adjective, vehicle):
    '''This function returns a story with the given words filled in.
    Args:
        person_one (str): name of the first person
        street_name (str): name of the street
        person_two (str): name of the second person
        object_name (str): name of the object
        adjective (str): an adjective
        vehicle (str): type of vehicle
    Returns:
        return the story'''
    
    story_template = """{0} decided to move from their apartment on 5th
to a condo on {1}. They called their friend {2}
for help. However, they could not fit {3} into
the moving truck, so they had to rent a {4} {5}
in order to move it!"""
    
    return story_template.format(person_one, street_name, person_two, 
                                 object_name, vehicle, adjective)

def main():
    '''
    The words that will be used
    in the story are defined here and the story is printed.
    '''
    
    # Define the words for the story
    person_one = "Janet"
    street_name = "Loopdydoo Avenue"
    person_two = "Richard"
    object_name = "Christmas tree"
    adjective = "off-road"
    vehicle = "Horse-drawn carriage"

    # Call the function to create the story
    final_story = create_story(person_one, street_name, person_two, 
                              object_name, adjective, vehicle)
    
    # Print the completed story
    print(final_story)

# This line runs the main function when the script is executed
main()

