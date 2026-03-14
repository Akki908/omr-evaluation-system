import streamlit as st
import pandas as pd
from evaluator import evaluate
from report import generate_report

st.title("OMR Evaluation System")

answer_file = st.file_uploader("Upload Answer Key CSV", type=["csv"])
test_file = st.file_uploader("Upload Student Answers CSV", type=["csv"])

if answer_file and test_file:

    results, total_q = evaluate(answer_file, test_file)

    st.subheader("Results")
    st.dataframe(results)

    report = generate_report(results, total_q)

    st.subheader("Analysis Report")
    st.dataframe(report)

    results.to_csv("results.csv", index=False)
    report.to_csv("analysis_report.csv", index=False)

    st.success("Evaluation Complete!")