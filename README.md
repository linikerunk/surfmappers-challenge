# Surfmappers Upload Image
You have a couple of friends who are getting married soon and they asked to play with the trainers. They want to create a photo gallery where everyone can upload photos taken during the wedding.

1. - [x] a photo upload screen

2. - [x] a screen to display a gallery

3. - [x] a screen to approve the photos to view in the gallery.

4. - [x] Only photos that have been approved should be visible on the gallery page that will be visible to everyone.

5. - [ ] Photos must be stored on AWS S3.

🎯 The project needs to be developed in python using any framework of your choice. 🎯
# Deploy
https://surfmappers.herokuapp.com/

## How to Install 
```sh
python -m venv name_your_env
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Run the test

```sh
python pytest
```