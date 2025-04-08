import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

API_KEY = "55124094102abc5baf3e1479f1aa176b"
BASE_CURRENT = "http://api.openweathermap.org/data/2.5/weather?"
BASE_FORECAST = "http://api.openweathermap.org/data/2.5/forecast?"

class WeatherApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.city_input = TextInput(hint_text='Enter city', size_hint_y=None, height=80)
        self.layout.add_widget(self.city_input)

        self.search_btn = Button(text="Get Weather", size_hint_y=None, height=80)
        self.search_btn.bind(on_press=self.fetch_weather)
        self.layout.add_widget(self.search_btn)

        self.result_label = Label(text='', size_hint_y=None, halign='left', valign='top')
        self.result_label.bind(texture_size=self.result_label.setter('size'))

        self.scroll_layout = GridLayout(cols=1, size_hint_y=None, padding=5, spacing=5)
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.scroll_layout.add_widget(self.result_label)

        scroll_view = ScrollView()
        scroll_view.add_widget(self.scroll_layout)
        self.layout.add_widget(scroll_view)

        return self.layout

    def fetch_weather(self, instance):
        city = self.city_input.text.strip()
        if not city:
            self.result_label.text = "Please enter a city name."
            return

        # Get current weather
        curr_url = f"{BASE_CURRENT}appid={API_KEY}&q={city}&units=metric"
        curr_response = requests.get(curr_url).json()

        if curr_response["cod"] != 200:
            self.result_label.text = "City not found."
            return

        temp = curr_response["main"]["temp"]
        humidity = curr_response["main"]["humidity"]
        desc = curr_response["weather"][0]["description"]
        wind = curr_response["wind"]["speed"]

        result_text = f"Current Weather in {city.capitalize()}:\n"
        result_text += f"Temperature: {temp}°C\nHumidity: {humidity}%\n"
        result_text += f"Condition: {desc.capitalize()}\nWind Speed: {wind} m/s\n"

        # Get forecast
        forecast_url = f"{BASE_FORECAST}appid={API_KEY}&q={city}&units=metric"
        forecast_response = requests.get(forecast_url).json()

        result_text += "\n5-Day Forecast:\n"
        forecast_data = forecast_response["list"]
        days = {}

        for item in forecast_data:
            dt_txt = item["dt_txt"]
            date, time = dt_txt.split(" ")
            if time in ["09:00:00", "18:00:00"]:
                if date not in days:
                    days[date] = []
                temp = item["main"]["temp"]
                desc = item["weather"][0]["description"]
                days[date].append((time, temp, desc))

        for date, entries in list(days.items())[:5]:
            result_text += f"\nDate: {date}\n"
            for time, temp, desc in entries:
                label = "Morning" if time.startswith("09") else "Evening"
                result_text += f"{label}: {temp}°C, {desc.capitalize()}\n"

        self.result_label.text = result_text

WeatherApp().run()
# trigger
