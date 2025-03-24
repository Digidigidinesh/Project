import streamlit as st
import pickle
import pandas as pd
from datetime import datetime

# Data storage file
DATA_FILE = 'watering_data.pkl'

def load_data():
    try:
        with open(DATA_FILE, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)

def main():
    st.title("🌱 Basic Plant Watering System")
    
    # Settings
    threshold = st.sidebar.slider("Moisture Threshold (%)", 10, 50, 30)
    duration = st.sidebar.slider("Watering Duration (sec)", 1, 30, 5)
    
    # Simulate sensor input
    moisture = st.slider("Current Soil Moisture (%)", 0, 100, 25)
    
    # Display status
    st.subheader("Plant Status")
    if moisture < threshold:
        st.error(f"Needs watering! (Current: {moisture}%, Threshold: {threshold}%)")
    else:
        st.success(f"Moisture OK (Current: {moisture}%)")
    
    # Watering control
    if st.button("Water Plant Now"):
        new_record = {
            'timestamp': datetime.now(),
            'moisture_before': moisture,
            'duration': duration,
            'threshold': threshold
        }
        data = load_data()
        data.append(new_record)
        save_data(data)
        st.success(f"Watered for {duration} seconds!")
    
    # Show history
    st.subheader("Watering History")
    data = load_data()
    if data:
        df = pd.DataFrame(data)
        st.table(df.tail(5))  # Show last 5 records
    else:
        st.info("No watering history yet.")

if __name__ == "__main__":
    main()
