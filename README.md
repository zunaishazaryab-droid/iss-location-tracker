# ISS Location Tracker

A Python application that tracks the International Space Station (ISS) and sends an email notification when the ISS is overhead during nighttime.

## Description

This application checks if the International Space Station is passing over a specified location (defined by latitude and longitude) during nighttime. When both conditions are true, it sends an email notification alerting you to look up at the sky to potentially spot the ISS.

## Features

- Tracks real-time ISS position using the Open Notify API
- Determines sunrise and sunset times for your location using the Sunrise-Sunset API
- Sends email notifications when the ISS is overhead during nighttime
- Runs continuously with periodic checks (every 60 seconds)

## How It Works

1. The application periodically checks the current position of the ISS
2. It compares the ISS position with your defined location (within a ±5 degree range)
3. It determines if it's currently nighttime at your location
4. If the ISS is overhead and it's nighttime, an email notification is sent

## Requirements

- Python 3.x
- `requests` library
- Email account for sending notifications
- Internet connection to access APIs

## Setup

1. Clone this repository
2. Update the following constants in `main.py` with your information:
   - `MY_EMAIL`: Your email address
   - `MY_PASS`: Your email password or app password
   - `MY_LAT`: Your latitude
   - `MY_LONG`: Your longitude
3. Run the script using `python main.py`

## APIs Used

- [ISS Current Location API](http://api.open-notify.org/iss-now.json)
- [Sunrise-Sunset API](https://api.sunrise-sunset.org/json)

## Note

For Gmail users, you might need to use an app password instead of your regular password. Make sure to enable less secure apps or set up 2FA and generate an app password.
