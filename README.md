# PurBeurre
PurBeurre is a Django application. The purpose is to search a product
in a list and the application will show you others products with a 
better nutriscore grade. If you create a account, you can save the 
substitutes products in your favorite list.

Link : https://purdebeurre.herokuapp.com/


## Packages

* Django : Python framework to build web app
* heroku : Cloud platform as a service supporting the application
* selenium : Launch automatically functional tests, you need to download
geckodriver in local for the browser


## How to setup the project 
* Clone the repository 
* Install virtual environment

        pip3 install virtualenv
        virutalenv venv
        source venv/bin/activate
* Install requirements

        pip3 install -r requirements.txt

* Run the project in Production with the heroku url
    

* Run the project in Development
    
    - Run the program in local
    
            python3 manage.py runserver
            
    - Launch unit tests 

            python3 manage.py test tests
            
     - Launch functional tests with selenium 
            
            export PATH=$PATH:'Your path'
            python3 manage.py test seleniumtests
