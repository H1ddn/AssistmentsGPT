import pandas as pd

df = pd.read_csv("sample50.csv",encoding='latin-1')

minidf = df[['additional_problem_text','problem_text']]

df['question'] = minidf.values.tolist()

df["question"] = df["question"].apply(lambda x: [i for i in x if str(i) != "nan"])

df = df[['question', 'answer_text']]

for i in df.index:
    df.loc[i].to_json("jsons/row{}.json".format(i))