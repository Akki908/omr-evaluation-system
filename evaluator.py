import pandas as pd

def evaluate(answer_file, test_file):
    answer_key = pd.read_csv(answer_file, header=None).iloc[0].tolist()
    students = pd.read_csv(test_file)

    sid_column = students.columns[0]  # first column is student ID

    results = []
    for _, row in students.iterrows():
        sid = row[sid_column]
        answers = row[1:].tolist()  # all columns after first
        score = sum(1 for a, b in zip(answers, answer_key) if a == b)
        results.append({"StudentID": sid, "Score": score})

    results_df = pd.DataFrame(results)
    return results_df, len(answer_key)