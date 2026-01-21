# Enhancing Survey Insight and Effectiveness - TEAM NAME

## Objective
Develop an internal analytics tool to help surveyors extract insights from survey responses and improve survey design. The tool provides visual, statistical, and NLP-based insights to transform raw survey data into actionable intelligence.

## Dataset
- GRADSG survey dataset with ~2632 responses
- Features: demographics, study information, employer perception, motivating factors, free-text responses
- Status: Complete, Partial, Disqualified
- Columns include: university, year, degree, gender, nationality, employer perception, attractiveness rating, motivating factors, free-text write-ins

## Methodology
1. **Data Cleaning**
   - Removed disqualified responses
   - Handled missing values
   - Standardised categorical features
   - Preprocessed free-text responses

2. **Exploratory Data Analysis (EDA)**
   - Completion patterns
   - Demographic distributions
   - Correlation and redundancy analysis
   - Word clouds for free-text responses

3. **Segmentation & Pattern Analysis**
   - Clustering on demographics and survey responses
   - Dropout analysis using decision tree
   - Identification of redundant or low-value questions

4. **Insight Generation**
   - Synthesised structured & unstructured insights
   - LLM-generated narratives summarising trends and actionable recommendations

5. **Dashboard / Tool**
   - Interactive dashboard to explore:
     - Completion rates
     - Demographic and behavioural segments
     - Question correlations
     - LLM insights

## Results
- Identification of key drivers of employer attractiveness
- Segments most likely to drop out or skip questions
- Recommendations for survey improvement
- Interactive tool for stakeholders to explore data

## Tools & Libraries
- Python: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn
- NLP/LLM: NLTK, spaCy, OpenAI API (text embeddings & GPT)
- Dashboard: Streamlit / Plotly Dash

## Usage
1. Run `data_cleaning.ipynb` to preprocess the dataset
2. Run `eda.ipynb` for visualisation
3. Run `clustering_analysis.ipynb` for segmentation
4. Run `insight_generation.ipynb` to generate LLM insights
5. Run `dashboard.py` to launch interactive tool

## Team
- Declan (Data preprocessing + EDA)
- Richie (NLP & clustering)
- John (LLM insights + dashboard)
- Sean (Visualisation + reporting)
