🌱 Automated Plant Watering System
Project Banner

A simple Streamlit-based application to simulate and manage plant watering automation, with data logging and dataset generation capabilities.

Features
💧 Moisture monitoring with adjustable threshold

⏲️ Configurable watering duration

📊 Data logging using pickle

📈 Dataset generation for analysis

🖥️ Simple web interface with Streamlit

Installation
Clone the repository:

Install the required packages:
pip install streamlit pandas numpy matplotlib

Usage
Running the Streamlit App
streamlit run plant_watering_app.py
Generating Sample Data
Run the generate_dataset.ipynb Jupyter notebook to create sample data in CSV format.

File Structure
Copy
automated-plant-watering/
├── plant_watering_app.py        # Main Streamlit application
├── generate_dataset.ipynb       # Jupyter notebook for dataset generation
├── watering_data.pkl            # Data storage file (created after first run)
└── plant_watering_dataset.csv   # Sample dataset (generated by notebook)
Data Model
The system stores the following information for each watering event:

timestamp: When the watering occurred

moisture_before: Soil moisture level before watering

duration: How long watering lasted (seconds)

threshold: Moisture threshold setting at time of watering

moisture_after: Soil moisture after watering (in generated dataset)

needed_watering: Whether watering was needed (in generated dataset)
