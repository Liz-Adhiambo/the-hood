# The -Hood
This is a web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.
## Author
Elizabeth Adhiambo

## User Stories
A user of the application can:
* Sign in / login to the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
*Change My neighborhood when I decide to move out.
*Only view details of a single neighborhood.


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| User Authentication | **On demand, verify emails before proceeding** | Access Admin dashboard |
| neigborhood feed | **Feed page** | Display of feeds of a particular Neigborhood |
| Display Businesses| **On  businesses link click** | A display of all Businesses in a particular Neighborhood are vewed |
| To edit neighborhood  | **Through profile page** | Click on Edit Neighborhood information and to update profile details|

| To delete an image  | **Through Admin dashboard** | click on image object and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search businesses by business name. The search form is case sensitive|


## Technologies used
* Python3.8.10
* Django 



## Installations

The following command installs all the application requirements
>``pip freeze -r requirements.txt``

## Setup
Run 
``https://github.com/Liz2222/the-hood.git``

or download the zip file from github.

After extracting the files, 

1. Navigate to the project folder
>`` cd name_of_folder`` 

2. Creating a virtual environment
>``virtualenv virtual``

3. Activating the virtual environment
>``source virtual/bin/activate``

4. Running the application
>``python3 manage.py runserverserver``

5. Running tests

 > ``python3 manage.py test.``

## [License]()

## Collaborate
For any collaborations, reach me on [adhiamboliz3@gmail.com]()