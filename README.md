### ![GA](https://cloud.githubusercontent.com/assets/40461/8183776/469f976e-1432-11e5-8199-6ac91363302b.png) 

### General Assembly, Software Engineering Immersive

# Project-4 - Know Your Heritage
## Overview:

My team created a Python and JavaScript app that showcases the wonders of the UNESCO’s World Heritage List. 

Using Flask, PostgreSQL, Marshmallow, React and multiple API's. The user is able to comment on sites and add their favourites to the wish list. 

We designed the wireframe, agreed on the SQL Data Relationships and collaborated to complete the MVP. We made use of Git and GitHub for version control and Heroku platform for deployment. 

The app was built within 7 days by a team of 2 people, applying all the concepts learned on the 4 modules of the course. This was the final project of the Software Engineering Immersive Course at General Assembly.  

I developed the nested connections with the different API’s, first to access the UNESCO list, second to retrieve the location-ID from Google API and third to retrieve the Google images using the location-ID to achieve the correct seeding. Built the home page and completed the styling of the app.

![app working](frontend/styles/heritage.gif)

## Brief:
- Work in a pair, using git to code collaboratively.
- Use a Python Flask API to serve your data from a PostgreSQL database
- Consume your API with a separate front-end built with React
- Use multiple data relationships and CRUD functionality for at least a couple of models
- Implement thoughtful user stories/wireframes that are significant enough to help you know which features are core MVP and which you can cut
- Be deployed online so it's publicly accessible.

Technologies Used:

* HTML5
* CSS
* JavaScript (ES6)
* Python 3
* Flask
* PostgresDB
* Marshmallow
* SQLalchemy
* Bcrypt & JWT
* React.js
* Webpack
* Node.js
* babel
* Axios
* Bulma
* Git
* GitHub
* Insomnia
* Heroku
* API’s
* Mapbox (React-MapGL)
* Cloudinary
* Google API's

## Approach taken:
The team’s project started with the idea of creating an application that would allow users to browse through the UNESCO's World Heritage list, comment on them, discovering nearby sites, as well as exploring its wonders across the world.

We collaborated at the start of the project by whiteboarding ideas and wireframing the MVP expected, also what stretch goals could be added to the application. 

We built the user and site schema together to make sure we both are on the same page. This allowed us to split the work efficiently.

We also decided that the application will allow unregistered users to use the core functionality of searching for locations by country.

Users could also register to add, edit and delete reviews to sites, creating a list of their favourite sites, accessing other users’ information, as well as editing user’s own information.

We found an API that contained the list of sites from the UNESCO's list, as it lacked of imaginery,we decided to use Google's API, to include more images.

The entired back end was built using Python and the front end using JavaScript.

### Functionality:

### - Back-End seed.py:

I took on the task of implementing the seed file. To start I created two users and two locations samples, so we could work on the layout and functionalities of the application. 

Although the API where I accessed the UNESCO data held important information about each site, this data only contained one thumbnail picture in low resolution of each site. I wanted to create an application that really displayed the beauty of each place, therefore, I took on the challenge of retrieving the images for the Google Places API.

This task had to be divided into 3 steps

1 - Retrieve the list of sites from the UNESCO API endpoint and seed it into our database, by mapping each data field and filter only the relevant information that will be used in the application

```
resp = requests.get(
        'https://data.opendatasoft.com/api/records/1.0/search/?dataset=world-heritage-list%40public-us&rows=60')
    # &facet=region&facet=states
    heritage_list = resp.json()
    heritage_filtered_records = heritage_list['records']
    result = []
    for x in heritage_filtered_records:
        result.append(heritage_filtered_records)
    result_1 = result[0]
    # pprint.pprint(heritage_filtered_records)

    def mapper(record):
      return {'region': record['fields']['region'],
                'name': record['fields']['site'],
                'latitude': record['fields']['coordinates'][0],
                'longitude': record['fields']['coordinates'][1],
                'country': record['fields']['states'],
                'province': record['fields'].get(
                  'location'),
                'description': record['fields']['short_description'],
                'thumbnail_id': record['fields']['image_url']['id'],
                # image=heritage_filtered_dictionary[''],
                'weblink': record['fields']['http_url'],
                'date_inscribed': record['fields']['date_inscribed'],
                'user': balta}

    filtered = (list(map(mapper, result_1)))
    # pprint.pprint(filtered)
```

2 - With the name of each site found in the previous fetch, I had to call the Google Places API, in order to retrieve the google ID for each location.

```
def google_id_mapper(record):
        name = record['name']
        resp_1 = requests.get(
            f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={name}&key={Google_API}')
    # &facet=region&facet=states
        google_dict = resp_1.json()
        # print(resp_1)
        # print(google_dict)
        if not google_dict['results']:
            google_place_id = 'ChIJO7l_l7f8cQ0Rf6IhEu_RjYA'
            record['place_id'] = google_place_id
            return record
       
        else:
            google_place_id = google_dict['results'][0]['place_id']
            record['place_id'] = google_place_id

            # google_result = google_dict['results'][0]
            return record



    filtered_with_id = (list(map(google_id_mapper, filtered)))
```

3 - Once the Google ID is retrieved, a third fetch was done to the Google Photos API, so multiple photos could be added to each location.


```
def google_id_mapper(record):
        name = record['name']
        resp_1 = requests.get(
            f'https://maps.googleapis.com/maps/api/place/textsearch/json?query={name}&key={Google_API}')
    # &facet=region&facet=states
        google_dict = resp_1.json()
        # print(resp_1)
        # print(google_dict)
        if not google_dict['results']:
            google_place_id = 'ChIJO7l_l7f8cQ0Rf6IhEu_RjYA'
            record['place_id'] = google_place_id
            return record
       
        else:
            google_place_id = google_dict['results'][0]['place_id']
            record['place_id'] = google_place_id

            # google_result = google_dict['results'][0]
            return record



    filtered_with_id = (list(map(google_id_mapper, filtered)))
```

### - Email Verification

To create the email verification functionality I used the [SendGrid Email API](https://sendgrid.com/docs/API_Reference/index.html). 


```python
def send(base_URL,sender,user):
  message = Mail(from_email = sender,
    to_emails = user.email,
    subject = "Email verification from WH",
    html_content = f'<a href="{base_URL}/verification/{user.id}">Please click here to verify your email address</a>'
    )
  try:
    sg = SendGridAPIClient(os.environ['SENDGRID_API_KEY'])
    response = sg.send(message)
  except Exception as e:
    print(str(e), message)
```
The email is sent upon successful login. 

```python
@router.route('/signup', methods=['POST'])
def signup():
    request_body = request.get_json()
    user = user_schema.load(request_body)
    email = user.email
    try:
      valid = validate_email(email)
      email = valid.email
    except EmailNotValidError as e:
      return str(e), 400
    try: 
      user.save()
    except exc.IntegrityError as e:
      return str(e.orig.args), 409
    send('https://know-your-heritage.herokuapp.com', 'whprojectapp2020@gmail.com', user)
    return user_schema.jsonify(user), 200
```


## Potential Future Features
- Ratings to be imported from google or tripadvisor.
- Adding a section of Popular locations nearby in the single plage
- Pagination and filtering options

## Challenges

This is the first project I have used `Python` for. One of the challenges was that in `Python` there is an extra layer of `serializers` between the objects   and their `JSON` form  compare to `javaScript`. Getting these right certainly took some time researching of best practices and reading up on the subject.

Working with a relational database was also a challenge that I had to overcome. After you understand the core concepts it is quite clear that it offers a robust solution for modeling complex domains. 

## Lessons learned
We used the Google Places API to get the pictures for the app. Unfortunately during our development period we used up the number of requests given by the API. We managed to get a new key for the deployment in time and had a successful demo. Paying attention to `API` quotas and monitoring your usage was certainly  one of the key lessons learned in this project. 

# Summary

We had lots more ideas that we couldn't fit in the timescale. Such as showing the sites on a scalable map page, displaying recommendations on the single page and extending the search functionality with additional filters. 

Overall,  we both enjoyed the project learned a lot especially about `Python`, `RDBMS`. We are excited to continue working on it, so these features will be added over time.

