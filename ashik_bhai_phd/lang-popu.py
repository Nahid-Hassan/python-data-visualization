import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('survey_results_responses.csv')

# print(df.head())

ids = df['ResponseId']
lang_responses = df['LanguageHaveWorkedWith']

languages_counter = Counter()

for response in lang_responses:
    if isinstance(response, str):
        languages_counter.update(response.split(';'))

languages = []
popularity = []


for item in languages_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

# plt.bar(languages, popularity)
plt.barh(languages, popularity)
plt.show()