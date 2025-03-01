To Run: <br>
docker-compose up --build

Architecture:

Scheduling service ----> Fills schedule and responsible for live events(live event might be separate service) - the non user triggered engine.

Fighter service ----> Handles the fighter roster including getting their images and UI needed features

Prediction service -----> Handles the requests for guesses the clients make. Handles the clients fanatic points.

BFF -----> handles authentication and serves as a reverse proxy for the app.