### ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) General Assembly, Software Engineering Immersive
 
# Know Your Heritage 
A PostgreSQL, Python, Flask & React Full Stack Application which showcases UNESCO's world heritage list. The user is able to comment on sites and add their favourites to the wish list. 

Deployed on Heroku: know-your-heritage.herokuapp.com


## Overview
The concept was to work remotely in a group of two for 7 days to create a full-stack web application. Using the Flask Framework to serve data from a PostgreSQL database to a React front end. The application must demonstrate the use of multiple relationships and CRUD functionality for the intended models. Plan and create an Entity Relationship Diagram, prior to moving on to development.
 
## Brief
- Build a full-stack application by making your own database using PostgreSQL
- Build a complete product - multiple relationships and CRUD functionality for the models
- Navigate the database using Python & Flask with SQLAlchemy
- Work with REST-ful design to serve data programmatically
- Build a professional front end design with React
- Collaborate via Git and GitHub
- Deploy the application online

 
## Technologies Used

- Python & Flask
- PostgreSQL
- Marshmallow & SQLalchemy
- React & Javascript
- Bulma
- Bcrypt & JWT
- Insomnia 
- Git and GitHub 
- Heroku

   
## Approach Taken

First we used a virtual whiteboard to flesh out the basic structure and functions that we wanted to implement and also figure out the stretch goals. We created an entity relationship diagram;
built the user and site schema together to make sure we both are on the same page. This allowed us to split the work efficiently.
My focus was on the back end which heavily relies  on `serializers` to populate response bodies. I was working on the `CRUD` controller functions and also the email verification. Later on helped to create the wishlist both backend and frontend.

## Method
 



## Challenges

This is the first project I have used `Python` for. One of the challenges was that in `Python` there is an extra layer of `serializers` between the objects   and their `JSON` form  compare to `javaScript`. Getting these right certainly took some time researching of best practices and reading up on the subject.

Working with a relational database was also a challenge that I had to overcome. After you understand the core concepts it is quite clear that it offers a robust solution for modeling complex domains. 

We used the Google Places API to get the pictures for the app. Unfortunately during our development period we used up the number of requests given by the API. We managed to get a new key for the deployment in time and had a successful demo. Paying attention to `API` quotas and monitoring your usage was certainly  one of the key lessons learned in this project. 


# Summary

We had lots more ideas that we couldn't fit in the timescale. Such as showing the sites on a scalable map page, displaying recommendations on the single page and extending the search functionality with additional filters. 

Overall,  we both enjoyed the project learned a lot especially about `Python`, `RDBMS`. We are excited to continue work on it, so these features will be added over time.
 

