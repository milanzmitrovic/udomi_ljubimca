# User Service API

- API users:
    - Front end
    - Other APIs

## Create 

- Inputs:
    - Personal users:
        - Name
        - Surname
        - Email
        - Accept terms and condition (binary variable)
        - KeyCloak ID
        - User type (binary variable)
    - Animal associations:
        - Name
        - City
        - Email
        - Contact phone
        - Government ID number
        - Web site
        - Accept terms and conditions (binary variable)
        - KeyCloak ID
        - User type (binary variable)
- Outputs:
    1. If user already exists, return json with info/warning.
    2. If user does not exist, return confirmation about new user creation.
- Job:
    - Check if user already exists.
        1. If already exists, return json with that information.
        2. If user does not exist yet, creat new user. Return info about user creation.
    - Add table autoincrement primary key.
    - Add time stamp (point in time when user has been created.)

## Read 

- Inputs:
    - Personal users:
        - KeyCloak ID
        
    - Animal associations:
        - KeyCloak ID

- Outputs:
    - If user exists, return all info about him/her.
    - If user does not exist, return info/warning.
- Job:
    - Check if user with that KeyCloak ID exist in database.
        - If does not exist, send json with info/warning.
        - If user exists, send data about that user.

## Update 

- Optional inputs:
    - Personal users:
        - Name
        - Surname
        - email
        - user age
        - user city
        - About me
        - KeyCloak ID (required input)
    - Animal associations:
        - Name
        - City
        - Email
        - Contact phone
        - Government ID number (???????)
        - Web site
        - About association
        - Terms and conditions for animal adoption
        - KeyCloak ID (required input)
        
- Outputs:
    - If user does not exist, send info/warning.
    - Return json with information on what has been updated ???
    - or Return all information (both updated and old ones) ???
- Job:
    - Check if row with corresponding KeyCloak ID exists.
        - If row does not exist, send warning in json.
        - If exist, update corresponding fields. Send json with info about updates made.

## Delete (to be determined)

- Inputs:
- Outputs:
- Job:


