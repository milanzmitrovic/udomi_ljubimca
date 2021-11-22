

# In final version, this is going to be request to animal api
def animal_present(animal_id: int):
    
    if animal_id < 10:
        return 'Animal exists'
    else:
        return 'Animal does not exist'

