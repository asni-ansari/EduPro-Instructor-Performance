import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
teachers = pd.read_csv("data/Teachers.csv")
courses = pd.read_csv("data/Courses.csv")
transactions = pd.read_csv("data/Transactions.csv")

st.set_page_config(page_title="EduPro Dashboard", layout="wide")

st.title("Instructor Performance and Course Quality Evaluation")

# KPIs
col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Teacher Rating",
    round(teachers["TeacherRating"].mean(), 2)
)

col2.metric(
    "Average Course Rating",
    round(courses["CourseRating"].mean(), 2)
)

corr = teachers["YearsOfExperience"].corr(
    teachers["TeacherRating"]
)

col3.metric(
    "Experience Impact Score",
    round(corr, 2)
)

st.divider()

# Teacher Rating Distribution
st.subheader("Teacher Rating Distribution")

fig, ax = plt.subplots(figsize=(8,5))

ax.hist(
    teachers["TeacherRating"],
    bins=10
)

ax.set_xlabel("Teacher Rating")
ax.set_ylabel("Count")

st.pyplot(fig)

# Experience vs Rating
st.subheader("Experience vs Teacher Rating")

fig, ax = plt.subplots(figsize=(8,5))

ax.scatter(
    teachers["YearsOfExperience"],
    teachers["TeacherRating"]
)

ax.set_xlabel("Years of Experience")
ax.set_ylabel("Teacher Rating")

st.pyplot(fig)

# Expertise Analysis
st.subheader("Expertise-wise Performance")

expertise = teachers.groupby(
    "Expertise"
)["TeacherRating"].mean().sort_values()

st.bar_chart(expertise)

# Top Instructors
st.subheader("Top 10 Instructors")

top = teachers.sort_values(
    "TeacherRating",
    ascending=False
).head(10)

st.dataframe(top)


st.subheader("Top Expertise Areas")

expertise = teachers.groupby(
    "Expertise"
)["TeacherRating"].mean().sort_values(ascending=False)

st.bar_chart(expertise)


st.subheader("Top 10 Instructors")

top_teachers = teachers.sort_values(
    "TeacherRating",
    ascending=False
).head(10)

st.dataframe(top_teachers)