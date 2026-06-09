# 🎨 Color Trend Dashboard

> An interactive web dashboard analyzing visual color trends across Fashion, Film, Social Media, and Design industries.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red?logo=streamlit)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-purple?logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Project Overview

The **Color Trend Dashboard** is a Streamlit-based interactive visualization tool that explores how color trends evolve across different creative industries. Users can filter by year range, industry, genre, and platform to gain insights into visual culture and color aesthetics.

This project was built as a final project combining data analysis, interactive design, and artistic interest in color theory.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🌈 **Color Family Trends** | Line chart + heatmap of color popularity across industries over time |
| 👗 **Fashion Analysis** | Runway appearances, color family distribution, popularity scatter |
| 🎬 **Film Palettes** | Dominant colors by genre, mood distribution, audience score trends |
| 📱 **Social Media** | Engagement by aesthetic, platform treemap, posts volume over time |
| 🎨 **Pantone Archive** | Full archive of Pantone Color of the Year (2000–2024) with RGB analysis |
| 🖌️ **Color Inspector** | Pick any color → get RGB values, brightness, and closest Pantone match |
| 🗓️ **Interactive Filters** | Sidebar filters for year range, industry, genre, and platform |

---

## 🗂️ Project Structure

```
color-trend-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .streamlit/
│   └── config.toml                 # Streamlit theme configuration
├── data/
│   ├── generate_data.py            # Script to regenerate datasets
│   ├── pantone_color_of_year.csv   # Pantone Color of the Year (2000–2024)
│   ├── fashion_color_trends.csv    # Fashion runway color data by season
│   ├── social_media_color_trends.csv # Social media aesthetics & engagement
│   ├── film_color_palettes.csv     # Film genre dominant color data
│   └── color_family_popularity.csv # Cross-industry color popularity index
└── README.md
```

---

## 📊 Data Sources

| Dataset | Source |
|---|---|
| `pantone_color_of_year.csv` | Real Pantone historical data (2000–2024) |
| `fashion_color_trends.csv` | Simulated fashion industry trend data |
| `social_media_color_trends.csv` | Simulated social platform engagement data |
| `film_color_palettes.csv` | Simulated film genre palette data |
| `color_family_popularity.csv` | Simulated cross-industry popularity index |

> The Pantone dataset uses real historical color values. Other datasets are realistic simulations built for educational purposes.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/color-trend-dashboard.git
cd color-trend-dashboard
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the datasets

```bash
python data/generate_data.py
```

### 5. Run the app

```bash
streamlit run app.py
```

The app will open at **http://localhost:8501**

---

## 🌐 Deploy on Streamlit Cloud

1. Push this repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New app** → select your repo → set `app.py` as the main file
4. Click **Deploy**

> Make sure `requirements.txt` is in the root directory before deploying.

---

## 🛠️ Tech Stack

- **[Python 3.10+](https://python.org)** — Core language
- **[Streamlit](https://streamlit.io)** — Web dashboard framework
- **[Plotly](https://plotly.com)** — Interactive charts and visualizations
- **[Pandas](https://pandas.pydata.org)** — Data manipulation
- **[NumPy](https://numpy.org)** — Numerical operations

---

## 📸 Dashboard Preview

### 🌈 Color Families Tab
- Interactive line chart tracking 8 color families from 2010–2024
- Industry × Color Family heatmap

### 👗 Fashion Tab
- Horizontal bar chart: top colors by runway appearances
- Pie chart: color family distribution
- Scatter: popularity score vs runway presence
- Live color swatches for each trend color

### 🎬 Film Tab
- Bar chart: most common color per genre
- Pie chart: mood distribution across films
- Area chart: audience score trend over time

### 📱 Social Media Tab
- Bar chart: engagement score by aesthetic (Cottagecore, Y2K, etc.)
- Treemap: posts volume by platform and vibe
- Line chart: posts over time per platform

### 🎨 Pantone Archive Tab
- Visual card grid of all Pantone Colors of the Year
- RGB composition line chart
- Color Inspector tool with closest Pantone match finder

---

## 💡 Future Improvements

- [ ] Integrate real social media API data (Instagram Graph API, Pinterest Trends)
- [ ] Add Pantone color scraping via web automation
- [ ] Seasonal filter (Spring/Summer vs Fall/Winter) in fashion tab
- [ ] Export charts as PNG / PDF
- [ ] Dark mode toggle

---

## 👩‍🎨 About

Built as a final project exploring the intersection of **art, color theory, and data visualization**.  
As an art student, this project combines creative interests with practical data analysis skills using Python and Streamlit.

---

## 📄 License

MIT License — feel free to use and modify for educational purposes.
