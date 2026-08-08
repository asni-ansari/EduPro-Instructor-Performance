# EduPro Instructor Performance and Course Quality Evaluation

## Project Overview

This project analyzes instructor performance and course quality on the EduPro online learning platform.

The analysis focuses on instructor ratings, teaching experience, expertise areas, course ratings, and enrollment patterns.

## Objectives

- Evaluate instructor performance.
- Analyze course quality.
- Study the relationship between teaching experience and instructor ratings.
- Identify high-performing expertise areas.
- Analyze the relationship between instructor ratings and enrollments.
- Provide data-driven recommendations for improving educational quality.

## Datasets

The project uses three main datasets:

- Teachers.csv
- Courses.csv
- Transactions.csv

### Dataset Size

| Dataset | Records |
|---|---:|
| Teachers | 60 |
| Courses | 60 |
| Transactions | 10,000 |

## Key Results

| KPI | Result |
|---|---:|
| Average Teacher Rating | 3.12 |
| Average Course Rating | 3.10 |
| Experience Impact Score | 0.598 |
| Teacher Rating vs Course Rating | -0.0016 |
| Enrollment Influence Ratio | 0.318 |

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit
- Jupyter Notebook

## Dashboard

The Streamlit dashboard provides:

- Instructor performance KPIs
- Teacher rating distribution
- Experience vs rating analysis
- Expertise-wise performance
- Top instructor leaderboard
- Course quality analysis

## Project Structure

```text
EduPro_Project/
│
├── data/
│   ├── Teachers.csv
│   ├── Courses.csv
│   ├── Transactions.csv
│   └── Users.csv
│
├── analysis.ipynb
├── app.py
├── requirements.txt
├── README.md
└── report/