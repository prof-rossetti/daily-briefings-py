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
python app/daily_briefing.py
```
