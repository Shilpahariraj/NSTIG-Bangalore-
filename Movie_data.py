import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("IMDb_Dataset.csv")
print(df)

# Data cleaning
df.dropna(subset=["Genre", "IMDb Rating", "Star Cast"], inplace=True)
df['Genre'] = df['Genre'].str.split(',').str[0]  # Use first genre only for simplicity
df[' Star Cast'] = df['Star Cast'].fillna('')

# Title
st.title("🎬 Movie Data Explorer")
st.write("Explore IMDb movie trends by genre and actor")

# Genre dropdown
genres = sorted(df['Genre'].dropna().unique())
selected_genre = st.selectbox("Select Genre", ["All"] + genres)

# Actor search
actor_search = st.text_input("Search by Star Cast")

# Filter data
filtered_df = df.copy()

if selected_genre != "All":
    filtered_df = filtered_df[filtered_df['Genre'] == selected_genre]

if actor_search:
    filtered_df = filtered_df[filtered_df['Star Cast'].str.contains(actor_search, case=False, na=False)]

st.write(f"🎞️ Showing {len(filtered_df)} movies")

# Genre popularity bar plot
st.subheader("📊 Genre Popularity")
genre_counts = df['Genre'].value_counts().head(10)

fig1, ax1 = plt.subplots()
sns.barplot(x=genre_counts.values, y=genre_counts.index, ax=ax1)
ax1.set_xlabel("Number of Movies")
ax1.set_ylabel("Genre")
st.pyplot(fig1)

# Box plot for ratings by genre
st.subheader("⭐ Ratings by Genre")
top_genres = df['Genre'].value_counts().head(5).index
box_df = df[df['Genre'].isin(top_genres)]

fig2, ax2 = plt.subplots()
sns.boxplot(x='Genre', y='IMDb Rating', data=box_df, ax=ax2)
ax2.set_title("Box Plot of Ratings by Top Genres")
st.pyplot(fig2)