To run this web app, run the following commands...

pip install requirements.txt
python manage.py runserver

This is how the tasks for the final deliverable can be tested...

run this command to create an admin (admins create and manage events)...
python manage.py createsuperuser

Go to the following url...
http://127.0.0.1:8000/admin

Here you can click event and create a new event

Go to the following url...
http://127.0.0.1:8000/discussions/

You can now do the following...
1. At the home page click enter event
2. Click post view and enter in some text. It will appear at the bottom of the event page
3. From another account, enter the event and click respond to that post
4. Once in the one on one discussion, you can send messages and propose common ground by first typing something in the field
4. From the other account, click "My Discussions" in the header and click the top newest one
5. From here, you can accept the other user's common ground
6. When accepting, each user gets 1 common ground point (shows next to name in header) and you are taken back to the event
7. Click "Published" to see concluded discussions.