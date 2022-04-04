# Daily Briefings App (Python)

Sends you a customized email every morning, with information of interest, such as the upcoming weather forecast for your zip code.

![](https://user-images.githubusercontent.com/1328807/77860069-173ef580-71db-11ea-83c6-5897bb9f4f51.png)

## Installation

Create a copy of this [template repo](https://github.com/prof-rossetti/daily-briefings-py), then clone or download your new repo onto your local computer (for example to the Desktop), and navigate there from the command-line:

```sh
cd ~/Desktop/daily-briefings-py/
```

Use Anaconda to create and activate a new virtual environment, perhaps called "briefings-env":

```sh
conda create -n briefings-env python=3.8
conda activate briefings-env
```

Then, within an active virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration

Follow these [SendGrid setup instructions](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/sendgrid.md#setup) to sign up for a SendGrid account, configure your account's email address (i.e. `SENDER_EMAIL_ADDRESS`), and obtain an API key (i.e. `SENDGRID_API_KEY`).

Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# these are example contents for the ".env" file:

# required vars:
SENDGRID_API_KEY="_______________"
SENDER_EMAIL_ADDRESS="_______________"

# optional vars:
#APP_ENV="development"
#COUNTRY_CODE="US"
#ZIP_CODE="10017"
#USER_NAME="Jon Snow"
```

## Usage

Printing today's weather forecast (to test the Weather.gov API):

```sh
python -m app.weather_service

# in production mode:
APP_ENV="production" COUNTRY_CODE="US" ZIP_CODE="20057" python -m app.weather_service
```

Sending an example email (to test the SendGrid service):

```sh
python -m app.email_service
```

> NOTE: the SendGrid emails might first start showing up in spam, until you designate them as coming from a trusted source (i.e. "Looks Safe")

Sending the weather forecast in an email:

```sh
python -m app.daily_briefing

# in production mode:
APP_ENV="production" COUNTRY_CODE="US" ZIP_CODE="20057" python -m app.daily_briefing
```


## Testing

Running tests:

```sh
pytest

# in CI mode:
CI=true pytest
```


## [Deploying](/DEPLOYING.md)

Follow the deployment instructions to deploy the app to a remote server and schedule the server to send you the weather forecast email every day.

## [License](/LICENSE.md)
