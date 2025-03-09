from bs4 import BeautifulSoup

# Load the HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract table rows
rows = soup.find("tbody").find_all("tr")

# Store extracted data
weather_data = []
for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.replace("°C", "").strip())  # Convert temperature to integer
    condition = cols[2].text.strip()
    weather_data.append({"day": day, "temperature": temp, "condition": condition})

# Display weather data
print("5-Day Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

# Find the hottest day
hottest_day = max(weather_data, key=lambda x: x["temperature"])
print(f"\nHottest Day: {hottest_day['day']} ({hottest_day['temperature']}°C)")

# Find sunny days
sunny_days = [entry["day"] for entry in weather_data if entry["condition"] == "Sunny"]
print(f"Sunny Days: {', '.join(sunny_days)}")

# Compute the average temperature
avg_temp = sum(entry["temperature"] for entry in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {avg_temp:.2f}°C")
