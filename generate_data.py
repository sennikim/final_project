import pandas as pd
import numpy as np

# ── 1. Pantone Color of the Year (real historical data) ──────────────────────
pantone = [
    {"year": 2000, "color_name": "Cerulean",           "hex": "#9BB7D4", "rgb_r": 155, "rgb_g": 183, "rgb_b": 212},
    {"year": 2001, "color_name": "Fuchsia Rose",        "hex": "#C74375", "rgb_r": 199, "rgb_g": 67,  "rgb_b": 117},
    {"year": 2002, "color_name": "True Red",            "hex": "#BF1932", "rgb_r": 191, "rgb_g": 25,  "rgb_b": 50},
    {"year": 2003, "color_name": "Aqua Sky",            "hex": "#7BC4E2", "rgb_r": 123, "rgb_g": 196, "rgb_b": 226},
    {"year": 2004, "color_name": "Tigerlily",           "hex": "#E2583E", "rgb_r": 226, "rgb_g": 88,  "rgb_b": 62},
    {"year": 2005, "color_name": "Blue Turquoise",      "hex": "#53B0AE", "rgb_r": 83,  "rgb_g": 176, "rgb_b": 174},
    {"year": 2006, "color_name": "Sand Dollar",         "hex": "#DECDBE", "rgb_r": 222, "rgb_g": 205, "rgb_b": 190},
    {"year": 2007, "color_name": "Chili Pepper",        "hex": "#9B1B30", "rgb_r": 155, "rgb_g": 27,  "rgb_b": 48},
    {"year": 2008, "color_name": "Blue Iris",           "hex": "#5A5B9F", "rgb_r": 90,  "rgb_g": 91,  "rgb_b": 159},
    {"year": 2009, "color_name": "Mimosa",              "hex": "#EFC050", "rgb_r": 239, "rgb_g": 192, "rgb_b": 80},
    {"year": 2010, "color_name": "Turquoise",           "hex": "#45B5AA", "rgb_r": 69,  "rgb_g": 181, "rgb_b": 170},
    {"year": 2011, "color_name": "Honeysuckle",         "hex": "#D94F70", "rgb_r": 217, "rgb_g": 79,  "rgb_b": 112},
    {"year": 2012, "color_name": "Tangerine Tango",     "hex": "#DD4132", "rgb_r": 221, "rgb_g": 65,  "rgb_b": 50},
    {"year": 2013, "color_name": "Emerald",             "hex": "#009473", "rgb_r": 0,   "rgb_g": 148, "rgb_b": 115},
    {"year": 2014, "color_name": "Radiant Orchid",      "hex": "#B163A3", "rgb_r": 177, "rgb_g": 99,  "rgb_b": 163},
    {"year": 2015, "color_name": "Marsala",             "hex": "#964F4C", "rgb_r": 150, "rgb_g": 79,  "rgb_b": 76},
    {"year": 2016, "color_name": "Rose Quartz",         "hex": "#F7CAC9", "rgb_r": 247, "rgb_g": 202, "rgb_b": 201},
    {"year": 2016, "color_name": "Serenity",            "hex": "#92A8D1", "rgb_r": 146, "rgb_g": 168, "rgb_b": 209},
    {"year": 2017, "color_name": "Greenery",            "hex": "#88B04B", "rgb_r": 136, "rgb_g": 176, "rgb_b": 75},
    {"year": 2018, "color_name": "Ultra Violet",        "hex": "#5F4B8B", "rgb_r": 95,  "rgb_g": 75,  "rgb_b": 139},
    {"year": 2019, "color_name": "Living Coral",        "hex": "#FF6B6B", "rgb_r": 255, "rgb_g": 107, "rgb_b": 107},
    {"year": 2020, "color_name": "Classic Blue",        "hex": "#0F4C81", "rgb_r": 15,  "rgb_g": 76,  "rgb_b": 129},
    {"year": 2021, "color_name": "Illuminating",        "hex": "#F5DF4D", "rgb_r": 245, "rgb_g": 223, "rgb_b": 77},
    {"year": 2021, "color_name": "Ultimate Gray",       "hex": "#939597", "rgb_r": 147, "rgb_g": 149, "rgb_b": 151},
    {"year": 2022, "color_name": "Very Peri",           "hex": "#6667AB", "rgb_r": 102, "rgb_g": 103, "rgb_b": 171},
    {"year": 2023, "color_name": "Viva Magenta",        "hex": "#BB2649", "rgb_r": 187, "rgb_g": 38,  "rgb_b": 73},
    {"year": 2024, "color_name": "Peach Fuzz",          "hex": "#FFBE98", "rgb_r": 255, "rgb_g": 190, "rgb_b": 152},
]
df_pantone = pd.DataFrame(pantone)
df_pantone.to_csv("/home/claude/color-trend-dashboard/data/pantone_color_of_year.csv", index=False)

# ── 2. Fashion Color Trends by Season ────────────────────────────────────────
seasons = ["Spring/Summer", "Fall/Winter"]
fashion_years = list(range(2015, 2025))
fashion_colors = [
    {"color": "Cobalt Blue",     "hex": "#0047AB", "family": "Blue"},
    {"color": "Terracotta",      "hex": "#E2725B", "family": "Orange"},
    {"color": "Sage Green",      "hex": "#B2AC88", "family": "Green"},
    {"color": "Blush Pink",      "hex": "#FFB6C1", "family": "Pink"},
    {"color": "Butter Yellow",   "hex": "#FFFAA0", "family": "Yellow"},
    {"color": "Lilac",           "hex": "#C8A2C8", "family": "Purple"},
    {"color": "Rust",            "hex": "#B7410E", "family": "Orange"},
    {"color": "Emerald",         "hex": "#50C878", "family": "Green"},
    {"color": "Cream",           "hex": "#FFFDD0", "family": "Neutral"},
    {"color": "Slate Gray",      "hex": "#708090", "family": "Neutral"},
    {"color": "Dusty Rose",      "hex": "#DCAE96", "family": "Pink"},
    {"color": "Navy",            "hex": "#001F5B", "family": "Blue"},
    {"color": "Marigold",        "hex": "#EAA221", "family": "Yellow"},
    {"color": "Lavender",        "hex": "#E6E6FA", "family": "Purple"},
    {"color": "Forest Green",    "hex": "#228B22", "family": "Green"},
]
np.random.seed(42)
fashion_rows = []
for year in fashion_years:
    for season in seasons:
        sampled = np.random.choice(len(fashion_colors), size=5, replace=False)
        for rank, idx in enumerate(sampled, 1):
            c = fashion_colors[idx]
            fashion_rows.append({
                "year": year, "season": season,
                "rank": rank,
                "color_name": c["color"],
                "hex": c["hex"],
                "color_family": c["family"],
                "popularity_score": round(np.random.uniform(60, 100), 1),
                "runway_appearances": np.random.randint(10, 80),
            })
df_fashion = pd.DataFrame(fashion_rows)
df_fashion.to_csv("/home/claude/color-trend-dashboard/data/fashion_color_trends.csv", index=False)

# ── 3. Social Media Color Palette Trends ─────────────────────────────────────
platforms = ["Instagram", "Pinterest", "TikTok", "Twitter/X"]
aesthetics = ["Cottagecore", "Dark Academia", "Y2K", "Minimalist", "Maximalist",
              "Coastal Grandmother", "Clean Girl", "Dopamine Dressing", "Old Money", "Barbiecore"]
sm_colors = [
    {"color": "Soft Pink",    "hex": "#FFB7C5", "vibe": "warm"},
    {"color": "Dusty Mauve",  "hex": "#C4A4A4", "vibe": "warm"},
    {"color": "Sage",         "hex": "#A8C5A0", "vibe": "cool"},
    {"color": "Vanilla",      "hex": "#F3E5AB", "vibe": "warm"},
    {"color": "Caramel",      "hex": "#C68642", "vibe": "warm"},
    {"color": "Midnight",     "hex": "#191970", "vibe": "dark"},
    {"color": "Hot Pink",     "hex": "#FF69B4", "vibe": "bright"},
    {"color": "Electric Blue","hex": "#7DF9FF", "vibe": "bright"},
    {"color": "Oat",          "hex": "#E8D5B7", "vibe": "neutral"},
    {"color": "Clay",         "hex": "#B66A50", "vibe": "warm"},
]
sm_years = list(range(2019, 2025))
sm_rows = []
for year in sm_years:
    for platform in platforms:
        for aesthetic in np.random.choice(aesthetics, size=3, replace=False):
            c = sm_colors[np.random.randint(0, len(sm_colors))]
            sm_rows.append({
                "year": year,
                "platform": platform,
                "aesthetic": aesthetic,
                "color_name": c["color"],
                "hex": c["hex"],
                "vibe": c["vibe"],
                "engagement_score": round(np.random.uniform(50, 100), 1),
                "posts_millions": round(np.random.uniform(0.5, 15.0), 2),
            })
df_sm = pd.DataFrame(sm_rows)
df_sm.to_csv("/home/claude/color-trend-dashboard/data/social_media_color_trends.csv", index=False)

# ── 4. Film / Movie Color Palettes ───────────────────────────────────────────
genres = ["Drama", "Romance", "Sci-Fi", "Horror", "Comedy", "Action", "Animation"]
film_palettes = [
    {"dominant": "Teal",        "hex": "#008080", "mood": "Mysterious"},
    {"dominant": "Golden",      "hex": "#FFD700", "mood": "Nostalgic"},
    {"dominant": "Deep Red",    "hex": "#8B0000", "mood": "Passionate"},
    {"dominant": "Neon Purple", "hex": "#9B59B6", "mood": "Futuristic"},
    {"dominant": "Warm Orange", "hex": "#FF8C00", "mood": "Energetic"},
    {"dominant": "Icy Blue",    "hex": "#B0E0E6", "mood": "Calm"},
    {"dominant": "Charcoal",    "hex": "#36454F", "mood": "Gritty"},
    {"dominant": "Lime Green",  "hex": "#32CD32", "mood": "Playful"},
]
film_years = list(range(2010, 2025))
film_rows = []
for year in film_years:
    for genre in genres:
        p = film_palettes[np.random.randint(0, len(film_palettes))]
        film_rows.append({
            "year": year,
            "genre": genre,
            "dominant_color": p["dominant"],
            "hex": p["hex"],
            "mood": p["mood"],
            "avg_audience_score": round(np.random.uniform(55, 95), 1),
            "box_office_billion": round(np.random.uniform(0.1, 2.5), 2),
        })
df_film = pd.DataFrame(film_rows)
df_film.to_csv("/home/claude/color-trend-dashboard/data/film_color_palettes.csv", index=False)

# ── 5. Color Family Popularity Over Time (cross-industry) ───────────────────
color_families = ["Red", "Blue", "Green", "Yellow", "Purple", "Pink", "Orange", "Neutral"]
industries = ["Fashion", "Film", "Social Media", "Interior Design", "Graphic Design"]
pop_years = list(range(2010, 2025))
pop_rows = []
for year in pop_years:
    for industry in industries:
        for family in color_families:
            base = {"Red":50,"Blue":65,"Green":55,"Yellow":40,"Purple":45,"Pink":60,"Orange":35,"Neutral":70}
            trend = np.random.normal(0, 8)
            yearly_shift = (year - 2010) * np.random.uniform(-1, 2)
            score = min(100, max(5, base[family] + trend + yearly_shift))
            pop_rows.append({
                "year": year,
                "industry": industry,
                "color_family": family,
                "popularity_index": round(score, 1),
            })
df_pop = pd.DataFrame(pop_rows)
df_pop.to_csv("/home/claude/color-trend-dashboard/data/color_family_popularity.csv", index=False)

print("✅ All datasets generated successfully!")
for name, df in [("Pantone", df_pantone), ("Fashion", df_fashion),
                 ("Social Media", df_sm), ("Film", df_film), ("Popularity", df_pop)]:
    print(f"  {name}: {len(df)} rows")
