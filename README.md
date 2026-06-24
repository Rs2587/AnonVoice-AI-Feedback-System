# AI-Powered Anonymous Student Feedback & Complaint Analysis System

## 📌 Project Overview

The AI-Powered Anonymous Student Feedback & Complaint Analysis System is a Flask-based web application that enables students to submit complaints anonymously while providing administrators with powerful analytics and machine learning insights.

The system protects student identity using anonymous IDs and encrypted feedback storage. It automatically analyzes complaints using Machine Learning techniques such as Sentiment Analysis, Category Prediction, and KMeans Clustering to help administrators identify patterns and take action efficiently.

## 🎯 Problem Statement

In many educational institutions, students hesitate to submit complaints due to fear of identification or retaliation. Traditional feedback systems often lack anonymity, analytics, and intelligent complaint categorization.

This project addresses these issues by providing a secure and intelligent platform for anonymous complaint submission and analysis.

## ✨ Features

### Student Features

* Submit complaints anonymously
* Unique Anonymous ID generation
* Track complaint status
* View admin comments
* Secure encrypted feedback storage

### Admin Features

* Admin login dashboard
* View all complaints
* Search complaints
* Update complaint status
* Add admin comments
* Delete complaints
* Export reports to Excel and PDF

### Machine Learning Features

* Sentiment Analysis (Positive, Negative, Urgent)
* Automatic Category Prediction
* KMeans Complaint Clustering
* AI-Powered Complaint Insights

### Data Visualization

* Complaint Category Pie Chart
* Sentiment Distribution Pie Chart
* Dashboard Analytics


## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Backend

* Flask
* Python

### Database

* SQLite

### Machine Learning

* Scikit-Learn
* TF-IDF Vectorizer
* Multinomial Naive Bayes
* KMeans Clustering

### Data Analysis & Visualization

* Pandas
* Matplotlib

### Security

* Feedback Encryption
* Anonymous ID Generation

### Reporting

* Excel Export (Pandas)
* PDF Export (ReportLab)


## 📂 Project Structure
AnonVoice_Project_Structure/
│
├── app.py
├── README.md
│
├── database/
│   └── feedback.db
│
├── dataset/
│   ├── sentiment_data.csv
│   └── category_data.csv
│
├── models/
│   └── feedback.py
│
├── routes/
│   ├── admin_routes.py
│   └── feedback_routes.py
│
├── templates/
│   ├── submit_feedback.html
│   ├── admin_dashboard.html
│   ├── login.html
│   ├── check_status.html
│   └── complaint_status.html
│
├── utils/
│   ├── encryption.py
│   ├── anonymizer.py
│   ├── ml_sentiment.py
│   ├── category_predictor.py
│   └── cluster_helper.py
│
├── static/
│   └── charts/
│
└── screenshots/

