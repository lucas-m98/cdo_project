This project is a simple sub-reddit search tool that uses the Django framework to create the UI and the
python requests library to handle to interfacing between Reddit and this web app.

In order to launch the application locally, all that needs to be done is run:

python manage.py runserver

(Possible need to use python3, depending on your environment)

This will stand-up the application at localhost/:8000 and can be used via a modern browser.

The application itself is very straight forward. The UI is combined with some Django logic that allows the 
python to interface with the HTML, allowing for some dynamic modifications to be done to the page. Using 
the input from the search-bar on the UI, the application will attempt to collect the "hot" posts from that
subreddit. If it fails, it will present the user with the error code it received. If it succeeds, then
the JSON received from the page is parsed into the internal "post" format that only contains the necessary
information to present to the user. This information is then used by Django to render the basic home.html
file with all of the collected components from the request. Once this is done, the page is served to the 
user who can then navigate the page to look for any posts that suit their fancy and click on the hyperlinked
title to be redirected to the post itself. 

The project is also hosted on an AWS EC2 instance with a public IP of 18.222.54.18. (:8000)

Because of the Django filler, the important files to note are:
- post.py
- reddit_api_call.py
- pull_reddit/views.py
- pull_reddit/forms.py
- pull_reddit/templates/pull_reddit/home.html
