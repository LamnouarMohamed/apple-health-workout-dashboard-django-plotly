# Apple Health Workout Simple Dashboard 🏃‍♂️📊

An interactive dashboard for visualizing **Walking & Running data** extracted from **Apple Health**, built using **Django** and **Dash Plotly**.

## 🔍 Overview

This project provides a web-based interface to filter and explore health data (e.g. running, walking) by **year**, **month**, and **activity type**. It uses:

- **Django** for backend form handling and routing
- **Plotly Dash** for interactive data visualizations
- **Apple Health data** as the source (exported in XML)

## 🎯 Features

- 📅 Select workouts by **year** and **month**
- 🏃 Choose between **Running** or **Walking** activity types
- 📈 Visualize trends and summaries using **Plotly charts**
- 🔒 Secure and modular Django integration with Dash
- ⚡ Lightweight and responsive design

## 🛠️ Tech Stack

- Python
- Django
- Dash & Plotly
- Apple Health XML

## 🚀 Getting Started
0. **How to Export Your Data from Apple Health:**
   - Open the Health app on your iPhone.
   - Tap your profile icon in the top-right corner.
   - Scroll down and select Export All Health Data.
   - Confirm the export — your iPhone will generate a .zip file.
   - Share the exported .zip file to your computer (via AirDrop, iCloud, or email).
   - Unzip the file — inside, you’ll find:
     * export.xml — the main file containing your health records.
     * Additional folders (e.g., electrocardiograms/, workouts/, etc.)
   - Place the export.xml file (or relevant CSV/XML files) in your project’s directory:
                <pre> 
                    sport/ 
                    │ 
                    ├── data/ 
                    │   └── export.xml 
                </pre>
1. **Load Apple Health Data into the Database :**
```
python manage.py populate_db
```
2. **Clone the repo:**

```bash
git clone https://github.com/LamnouarMohamed/apple-health-workout-dashboard-django-plotly.git
```

3. **Install dependencies:**

```
pip install -r requirements.txt
```

4. **Run the Django server:**
```
python manage.py runserver
```


