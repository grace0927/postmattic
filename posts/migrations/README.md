Reference Link: https://docs.djangoproject.com/en/2.1/intro/tutorial02/

By running makemigrations, you’re telling Django that you’ve made some changes to your models
```
shell>> python manage.py makemigrations polls
```

The sqlmigrate command takes migration names and returns their SQL
The sqlmigrate command doesn’t actually run the migration on your database - it just prints it to the screen so that you can see what SQL Django thinks is required.
```
python manage.py sqlmigrate polls 0001
```

run migrate again to create those model tables in your database
```
python manage.py migrate
```
