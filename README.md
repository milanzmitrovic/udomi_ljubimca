

## This is preview of dashboard


https://user-images.githubusercontent.com/58112365/190418639-2fe95741-c32c-42a9-a092-f36bff300e3e.mov



https://user-images.githubusercontent.com/58112365/190418678-d03286f4-63cf-4b18-bc71-dfda72fdbf51.mov


###### Below we can see high level logic of User Service api
###### Detailed api specification, especially information about json specification, should be found in swagger/openapi documentation of User Service api (which is built into app).


# Animal association

#### /create_animal_association

- This route should be only open to register service.
- When user register, register service should send api request to user service.

- Check if animal association already exist
- keycloak_id is used to uniquely determine animal association.
- Authorization is based on keycloak_id. In other words, if you know keycloak_id, you can perform any action.

- Check length of fields. Keycloak_id can be of maximum of 100 numbers. Other fields have maximum of 50 characters.

- Parameters:
    - keycloak_id
    - email
    - association_name
    - association_username

#### /read_animal_association

- Check if animal association exist. 
- Returns relevant information.

- Parameters:
    - keycloak_id

#### /update_animal_association

- Check if animal association exist.
- Check if city_id exist. As a city_id you can input only already predefined city ids.
- Update relevant information.

- Checks length of fields. About association has maximum of 500, keycloak_id 100, others maximum 50 characters.

- Parameters:
    - keycloak_id
    - email
    - association_name
    - association_username
    - city_id
    - phone_number
    - about_association


#### /delete_animal_association

- Check if animal association exist.
- Set value of is_active field to be equal to 0.

- Parameters:
    - keycloak_id

#### /all_animal_associations

- There is no input parameters.
- Calling this api route will return information about all registered animal associations.

- No parameters.

# Private Users

#### /create_private_user

- This api route should be only open to register service.
- When user registers, registration service should send api request with corresponding information to user service.

- Checks if user already exist.
- keycloak_id is used to uniquely determine personal users.
- Authorization is based on keycloak_id. In other words, if you know keycloak_id, you can perform any action.

- Checks length of fields. Keycloak_id has maximum of 100 characters, other fields max 50.

- Parameters:
    - keycloak_id
    - name
    - surname
    - username
    - email

#### /read_private_user

- Check if private user exist.
- Return corresponding information.

- Parameters:
    - keycloak_id

#### /update_private_user

- Check if private user exist.
- Checks if city_id exists in database. As city_id, you can input only already determined cities.
- Update relevant information.

- Check length of fields. Keycloak_id max 100, about me max 500, other fields max 50 characters.

- Parameters:
    - keycloak_id
    - name
    - surname
    - username
    - email
    - city_id
    - about_me
    - date_of_bitth

# Private Users Like

#### /like_animal

- Check does user exist.
- Check does animal exist.
- Perform like.

- Parameters:
    - animal_id
    - keycloak_id

#### /dislike_animal

- Check does user exist.
- Check does animal exist.
- Check does specific user already liked specific animal.
- Perform dislike operation.

- Parameters:
    - animal_id
    - keycloak_id

#### /liked_animals_by_user

- Check does user exist.
- Returns all animals liked by specific user.

- Parameters:
    - keycloak_id



## To be done:

- Image and PDF file CRUD operations.
- API integration with animal service. Needed api route for checking if animal exists in database.
- Creating dockerfile and docker-compose files.

