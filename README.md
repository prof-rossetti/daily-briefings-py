# daily-briefings-py

## Setup

Fork this repo and clone it onto your local computer (for example to your Desktop), then navigate there from the command-line:

```sh
cd ~/Desktop/daily-briefings-py/
```

Create and activate a new Anaconda virtual environment, perhaps named "briefings-env":

```sh
conda create -n briefings-env python=3.7
conda activate briefings-env
```

Then, from within the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

Obtain API Keys from [AlphaVantage](https://www.alphavantage.co/support/#api-key) (stocks), [Open Weather](https://home.openweathermap.org/api_keys) (weather), and [SendGrid](https://app.sendgrid.com/settings/api_keys) (emails). Create a new file called ".env" in the root directory of this repo, and paste the following contents inside, using your own values as appropriate:

```sh
# .env example

ALPHAVANTAGE_API_KEY="_______"
MY_STOCKS="MSFT,ZM,WORK"

OPEN_WEATHER_API_KEY="___________"
MY_ZIP="10017"

SENDGRID_API_KEY="_______________"
MY_EMAIL_ADDRESS="hello@example.com"
```

## Usage

From within the virtual environment, ensure you can run each of the files and see them produce their desired results of: printing the latest closing prices, printing today's weather forecast, and sending an example email, respectively.

```sh
python app/stocks_service.py
#> THE LATEST CLOSING PRICE IS ...
```

```sh
python app/weather_service.py
#> TODAY'S WEATHER FORECAST IS ...
```

```sh
python app/email_service.py
#> SENDING EMAIL TO ...
```

> NOTE: the Sendgrid emails might first start showing up in spam, until you designate them as coming from a trusted source

Also demonstrate your ability to send the daily briefing email:

```sh
python -m app.daily_briefing # note the module-syntax invocation
```
