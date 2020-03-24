# London Living API

## Premise
This API queries an external API (available [here](https://bpdts-test-app.herokuapp.com/))
to retrieve two separate lists of users. The first is a list of users who are registered as
living in London and the second is a list of users whose current latitude and longitude
coordinates are within 50 miles of London's centre.

The two lists are returned in a JSON response when a user queries the `users-in-london`
endpoint on the API.

## Technologies
The API is built using [FastAPI](https://github.com/tiangolo/fastapi) which is a high
performance web framework for building REST APIs in Python.

For distance calculation, the standard `math` library is used, `configparser` is used to
read in configuration and the `unittest` library is used to perform unit tests.

Using FastAPI also automatically produces a Swagger Schema for the API which can be
accessed at the `/docs#/` endpoint when the application is running.

## Running the code

### Getting started
To start with, please follow the below steps and then choose a subsection to get
instructions on what to do next:
1) Clone the repository onto your local machine
2) Navigate to the `src` directory

#### Running Locally
To run the code locally, use the following steps:
1) Run `pip install -r requirements.txt` to install the required packages
2) Run `uvicorn app.main:app --reload` to run the API and have it hot-reload whenever
a change is made
3) Browse to http://localhost:8000/docs#/ to view the Swagger documentation

#### Running the tests
1) Run `pip install -r requirements.txt` to install the required packages
2) Run `python -m unittest` to run the unit tests

#### Running using Docker
1) Run `docker build . -t london-livers` to build the Docker image (tagged with the
name "london-livers")
2) Run `docker run -p 80:80 -d london-livers` to run the Docker image, mapping the
container's port 80 to your machine's port 80 and running in detached mode
3) Browse to http://localhost:80/docs#/ to view the Swagger documentation 