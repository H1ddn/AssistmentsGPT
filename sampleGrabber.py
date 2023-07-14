import pandas as pd

df = pd.read_csv("segment_responses_additional_data_202306301430.csv",encoding='latin-1')

df = df.drop_duplicates(subset=['answer_text'])
df = df[~df.problem_text.str.contains('img')]
df = df[~df.answer_text.str.contains('img')]
df = df[~df.additional_problem_text.str.contains('img', na=False)]

sample = df.sample(50)

sample.to_csv('sample50.csv', index=False)