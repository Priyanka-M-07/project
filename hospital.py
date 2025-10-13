import streamlit as st
import random
import time

st.title("Hospital Sensor Live Monitoring")

st.write("Simulating live sensor data: Heart Rate,Temperature,Oxygen Level")

#Sensor data generator
def sensor_data_stream():
    while True:
        yield {
            "heart_rate": random.randint(60,100),
            "temperature": round(random.uniform(97.0, 100.0), 1),
            "oxygen_level": random.randint(90, 100)
        }
        time.sleep(1)

# Progress bars and text placeholders
heart_rate_bar = st.progress(0)
temperature_bar = st.progress(0)
oxygen_bar = st.progress(0)

heart_rate_text = st.empty()
temperature_text = st.empty()
oxygen_text = st.empty()

# Display the live data
for reading in sensor_data_stream():
    hr = reading["heart_rate"]
    temp = reading["temperature"]
    ox = reading["oxygen_level"]

    heart_rate_bar.progress(min(hr, 100))
    temperature_bar.progress(int(((temp-97)/3)*100))
    oxygen_bar.progress(ox)

    heart_rate_text.text(f"heart rate: {hr} bpm")
    temperature_text.text(f"temperature: {temp} °F")
    oxygen_text.text(f"oxygen level: {ox}%") 

time.sleep(1)