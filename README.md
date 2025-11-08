# Kivy Weather App

## Overview

This is a **desktop weather application** built with **Kivy** that fetches and displays:

* **Current weather** (temperature, humidity, condition, wind speed)
* **5-day forecast** (morning and evening temperatures and conditions)

It uses the **OpenWeatherMap API** to get real-time data.

---

## Features

* Input a city name to get current weather and 5-day forecast
* Scrollable display for long results
* Handles invalid city input gracefully

---

## Requirements

* Python 3.x
* Libraries:

```bash
pip install kivy requests
```

> Make sure Kivy is installed correctly for your OS (Windows/Linux/Mac).

---

## Setup

1. **Clone or download the code**
2. **Replace `API_KEY`** with your own OpenWeatherMap API key:

```python
API_KEY = "your_api_key_here"
```

3. **Run the app**:

```bash
python your_file.py
```

---

## How to Use

1. Enter a **city name** in the text input field.
2. Click **Get Weather**.
3. Scroll to view current weather and the 5-day forecast.

---

## Notes

* Forecast shows temperatures for **09:00** (morning) and **18:00** (evening) for the next 5 days.
* Ensure internet connection is active.
* The app uses **metric units** (°C for temperature, m/s for wind speed).

---
