import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
from wordcloud import WordCloud

plt.style.use('bmh')
df = pd.read_csv('netflix_data.csv')
df_1990 = df[df['release_year'] == 1990]


#variable declaration

x = df_1990['genre']
y = df_1990['duration']

# Genre with more duration
plt.xlabel( 'genre', fontsize=18)
plt.ylabel( 'duration(mins)',fontsize=16)
plt.bar(x, y)
plt.title("Genre with more duration")
plt.xticks(rotation=15, ha='right')
plt.show()

# Movies average duration
plt.figure(figsize=(10, 5))
plt.hist(df_1990['duration'].dropna(), bins=20, edgecolor="black")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.title(" Movies average duration")
plt.show()

#from wordcloud import WordCloud
text = " ".join(df_1990['description'].dropna())  # Combine all descriptions
wordcloud = WordCloud(width=800, height=400, background_color='black').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Common Words in Movie Descriptions (1990s)")
plt.show()



