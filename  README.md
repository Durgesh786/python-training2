- Setup virtual-environment
 
- Install dependency with below command
  - pip install -r requirements.txt


- Change DB setting from locla_setting.py file

- Run below commands for DB operations
  - python manage.py makemigrations
  - python manage.py migrate

- Create new app
  - navigate to the folder
  - run command : djang -admin startapp app_name
  - add to web_projects_app in settings.py
  - add urls.py file in newly created app
  - add models to models.py file
  - run command :  app_name app_neme2 app_neme3
                  python manage.py migrate
   
  
  

