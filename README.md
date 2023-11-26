# Event Manager Project

Welcome to the Event Manager project! This application allows users to manage events.

## Setup Instructions

simply run the following cmd command (make sure that you have docker and docker compose installed):
```cmd
docker-compose up
```

## Architecture

The Backcend combines a Python Flask server, which all serves as a Socket-IO server,
it uses the common SqlAlchemy library to save it's data in a Postgresql database within 3 tables:

*Event* - table responsible for saving data on events
*User* - table responsible for saving data on users
*EventParticipant* - table responsible for saving on users that are participation on event (many to many table)

also there is a celery worker component which responsible for performing unsyncronized system tasks and a celery beat component
that is responsible for triggering task for the worker to collect, the tasks are thrown from the celery beat into a Redis broker, that the celery worker reads from.

## Performance Optimizations

To optimize havy-load api requests like /api/events which retreives all of the system events with options such as sorting or filtering by location,
I added indexes in the columns of Event table on the attributes that i allow to sort by within the route.

Furthermore, in the popularity sort by optimization i wasn't adding any index because the username column in User table is already indexes as it's the
table's primary key, and so getting all of the user participation in an event is does quite efficiently

## API

The application is accessible via the following api:

### Authentication

To access the features of the Event Manager, users need to sign in first by sending a POST request to the `/api/user` endpoint with the following body:

#### Sign In

**Endpoint:** `POST /api/user`

**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password",
  "displayName": "your_display_name",
  "email": "your_email"
}
```

Then they need to log in, and in response they will receive a jwt access token which they could perform requests with:

#### Log In

**Endpoint:** `POST /api/login`

**Request Body:**
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

### Events

To start working with events Event Manager, you can use the following endpoints:

#### Get all events

**Endpoint:** `GET /api/events`

#### Get specific event

**Endpoint:** `GET /api/events/<event_id:int>`

#### Create an event

**Endpoint:** `POST /api/events`

**Request Body:**
```json
{
  "name": "New Event Name",
  "description": "New Event Description",
  "location": "New Event Location",
  "date": "2023-12-02T14:30:00",
  "participants": ["Participant1Username", "Participant2Username"]
}
```

#### Update an event

**Endpoint:** `PUT /api/events`

**Request Body:**
```json
{
  "name": "Updated Event Name",
  "description": "Updated Event Description",
  "location": "Updated Event Location",
  "date": "2023-12-02T14:30:00",
  "participants": ["Participant1Username", "Participant2Username"]
}
```

#### Delete event

**Endpoint:** `DELETE /api/events<event_id:int>`

#### Subscribe to event

You'll be notified if the event gets updated or canceled:

**Endpoint:** `POST /api/events/<event_id:int>/subscribe`

#### Cancel event subscription

Cancel your subscription on:

**Endpoint:** `DELETE /api/events/<event_id:int>/subscribe`
