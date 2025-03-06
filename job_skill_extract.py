import streamlit as st
import pandas as pd
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
from PIL import Image
nltk.download('punkt')
nltk.download('stopwords')

import nltk
try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

sw = set(stopwords.words('english'))

skills_list = ["python","sql","mysql","machine learning","deep learning","nlp","natural language processing","gan","generative adversarial network","gai","image processing",
             "computer vision","artificial intelligence","ai","ml","dl","iot","power bi","microsoft power bi","problem-solving","problem solving","problem solver"
             "critical thinking","ainlp","data","data science","data analysis","dara warehousing","data visualization","statistics","maths","r","excel",
             "teamwork","communication","preasure handling","tableau","pandas","numpy","scikit-learn","tensorflow","pytorch","keras","hadoop", "spark",
             "hive","aws","ec2","s3","sagemaker","data wrangling","experimental design","collaboration","data mining","java","c++","scala",
             "data modeling","agile methodology","supervised learning","supervised","unsupervised","unsupervised learning","internet of things",
             "generative ai","generative artificial intelligence","encoders","handle imbalance data","attention to detail","critical thinking",
               "adaptability","flexibility","self-motivation","self motivation","initiative","curiosity","learning mindset","time management","organization",
               "interpersonal skills","leadership","mentorship","innovation","creativity","ethical judgement","integrity","customer focus",
               "resilience","persistence"," insight sharing","experiment results","data exploration", "analysis","generative ai development","communication",
               "stable diffusion","dall·e","large language models","creative problem solving","content generation","langchain","classifiers","predictive models",
               "data preprocessing","data cleaning","data cleansing","data transformation","patterns","python libraries","seaborn","plotly","feature extraction","preprocessing",
               "pattern recognition","image generation","etl","mlops","mlflow","docker","kubernetes","opencv","mediapipe","reinforcement learning","big data","apache spark","kafka",
               "hadoop","matplotlib","jenkins","azure","machine learning studio","google cloud","vertex ai","power point","linear algebra","probability","calculus","nosql","mongodb",
               "neo4j","yolo","teamwork","vaes","responsible ai","time-series analysis, anomaly detection","geospatial data processing","hybrid","federated learning","hands-on experience",
               "tokenization","embeddings","sentiment analysis","sequence-to-sequence","rag pipelines","XGBoost","random forests","deep learning models","MidJourney",
              "hugging face","openai apis","ambitious","energetic","ensure integrity","rag","retrieval-augmented generation",
               "retrieval augmented generation","relational","non-relational databases","rest frameworks","cloud environments","teaching","teach","llm","forecasting",
               "anomaly detection","matlab","c","c#","model training","inference testing","fine tuning","waterfall","curious","tech-savvy","eda","problem understanding",
               "data collection","algorithm selection","model building","hyperparameter tuning","evaluation","deployment","monitoring of models","mitigate potential biases",
               "positive","proactive attitude","data augmentation","performance evaluation frameworks","gpt","analytical skills"]

def extract_skills(text):
    text = text.replace('\n', ' ').lower()
    tokens = word_tokenize(text)
    found_skills = set()
    for skill in skills_list:
        if ' ' not in skill:
            if skill in tokens:
                found_skills.add(skill)
        else:
            if skill in text:
                found_skills.add(skill)

    return list(found_skills)

# Streamlit app interface
st.markdown(
    """
    <style>
    .stApp {
        background-color: #E6F0FA;  
    }
    .stButton > button {
        background-color: #ADD8E6;  
        color: #333333;  
        border: 1px solid #ADD8E6;  
    }
    .stButton > button:hover {
        background-color: #87CEEB;  
        border: 1px solid #4682B4;
        color: #FFFFFF;  
    </style>
    """,
    unsafe_allow_html=True
)
img=Image.open('istockphoto-1723252472-612x612-removebg-preview.png')
st.image(img,width=450)

st.title("Job Description Skill Extractor")
st.write("Enter a job description below to extract key skills!")

# Text input from user
job_desc = st.text_area("Job Description", "Type or paste a job description here...")

# Button to process input
if st.button("Extract Skills"):
    if job_desc:
        skills = extract_skills(job_desc)
        st.write("**Extracted Skills:**", skills if skills else "No skills found from the list.")
    else:
        st.write("Please enter a job description.")
