# SPARKY

Sample web application built with FastAPI & Python 3.8

shows simple Flask-like structure with a Bootstrap template index.html

also has a background task scheduler (tasks.py) and error handler (errors.py)

Youtube tutorial: 

https://www.youtube.com/watch?v=Vcqc4GzDvbI

## how to run
use Pipenv to install dependencies (Pipfile)

    pipenv install

start the web server

    pipenv run sparky


## testing server load for background tasks
quick and dirty way to test server response, initiate multiple simultaneous curl calls from different hosts

    # will start 1000 curl calls to your background task route
    
    for i in {1..1000}; do curl -X POST "http://0.0.0.0:5700/task/run/NAME/$i" -H  "accept: application/json"; done

## additional resources

https://github.com/mjhea0/awesome-fastapi#tutorials