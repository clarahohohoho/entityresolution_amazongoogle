import pandas as pd

from main_tfidf import StringMatch


google_df = pd.read_csv('./data/Amazon-GoogleProducts/GoogleProducts.csv')
amazon_df = pd.read_csv('./data/Amazon-GoogleProducts/Amazon.csv')

google_name = google_df['name'].tolist()
amazon_name = amazon_df['title'].tolist()

# Application of StringMatch class, using default args
titlematch = StringMatch(google_name, amazon_name)
titlematch.tokenize()
match_df = titlematch.match()

match_df.to_csv('output.csv')