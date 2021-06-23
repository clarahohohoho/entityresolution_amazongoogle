# Entity Resolution between Amazon and Google datasets

An attempt to perform entity resolution between Amazon products and Google products. The link to the dataset can be found [here](https://dbs.uni-leipzig.de/research/projects/object_matching/benchmark_datasets_for_entity_resolution).

## Make virtual environment
To create, activate and install all relevant packages to virtual environment on Linux:
```
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

To activate virtual environment after creation for subsequent access:
```
source ./venv/bin/activate
```

## First approach: TFIDF

Trialed with the TFIDF approach, referencing this [article](https://medium.com/tim-black/fuzzy-string-matching-at-scale-41ae6ac452c2). Related files are the main_tfidf.py and test_tfidf.py files. Defaulted save path of output dataframe is './output.csv'.

### To run TFIDF approach:
```
python test_tfidf.py
```

### Results and afterthoughts:

WOW. The results really ran very quickly! It took about a second for the results to be generated, and after reviewing the results the results seem pretty promising! However, would still like to try out fuzzywuzzy, which includes techniques such as Levenshtein Distance, Jaro-Winkler etc. To my next trial!
