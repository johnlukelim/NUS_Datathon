Enhancing Survey Insight and Effectiveness - TEAM NAME
Objective
Develop an internal analytics tool to help surveyors extract insights from survey responses and improve survey design. The tool provides visual, statistical, and NLP-based insights to transform raw survey data into actionable intelligence.
Dataset
GRADSG survey dataset with ~2632 responses
Features: demographics, study information, employer perception, motivating factors, free-text responses
Status: Complete, Partial, Disqualified
Columns include: university, year, degree, gender, nationality, employer perception, attractiveness rating, motivating factors, free-text write-ins
Methodology
Data Cleaning

Removed unrealistic responses based on time taken for survey (<45 seconds)
Handled missing values
Standardised categorical features
Preprocessed free-text responses

Exploratory Data Analysis (EDA)

Completion patterns
Demographic distributions
Correlation and redundancy analysis
Word clouds for free-text responses

Segmentation & Pattern Analysis

Clustering on demographics and survey responses
Dropout analysis using decision tree
Identification of redundant or low-value questions

Insight Generation

Synthesised structured & unstructured insights
LLM-generated narratives summarising trends and actionable recommendations

Dashboard / Tool

Interactive dashboard to explore:
Completion rates
Demographic and behavioural segments
Question correlations
LLM insights
Results
Successfully developed a prototype internal analytics tool to support surveyor and research teams in extracting meaningful insights from applicant survey data
Automated data cleaning, exploratory analysis, and statistical summarisation has shown to significantly improve survey analysis workflows.
Operational benefits and analytical value, particularly in identifying data quality issues, distribution characteristics, and other statistically significant relationships.
Interactive tool for stakeholders to explore data
Tools & Libraries
Python: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn
NLP/LLM: NLTK, spaCy, OpenAI API (text embeddings & GPT)
Dashboard: Streamlit / Plotly Dash
Usage
Run data_cleaning.ipynb to preprocess the dataset
Run eda.ipynb for visualisation
Run clustering_analysis.ipynb for segmentation
Run insight_generation.ipynb to generate LLM insights
Run dashboard.py to launch interactive tool
