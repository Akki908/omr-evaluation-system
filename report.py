import pandas as pd


def generate_report(results_df, total_questions):

    report = {
        "Total Students": len(results_df),
        "Average Score": results_df["Score"].mean(),
        "Highest Score": results_df["Score"].max(),
        "Lowest Score": results_df["Score"].min(),
        "Total Questions": total_questions
    }

    return pd.DataFrame(report.items(), columns=["Metric", "Value"])