# Khant_DataCom_Final_Project_Personal_Dashboard
An interactive Streamlit dashboard tracking undergraduate academic journey and extracurricular leadership growth, built for the Data Communication and Ethics course at Parami University.

[cite_start]An interactive data dashboard analyzing the relationship between academic workload, academic performance, and extracurricular leadership efficiency over time. [cite_start]This project fulfills the final assessment requirements for the **Data Communication and Ethics (DATA 201)** course at **Parami University**.

## 📖 Project Overview
This project maps my transition from a broad liberal arts explorer into a focused data science student and student leader. By quantifiably tracking my undergraduate transcript metrics and weekly commitment hours across projects like CEDI, CIIF, and Borderless Futures, this dashboard visualizes how personal prioritization impacts overall productivity and academic stability.

## 📊 Key Insights & Visualizations
The application features 6 exploratory charts built using **Matplotlib** and **Seaborn** to tell the underlying data stories:
* **Global Coursework Balance:** A breakdown of foundational Humanities versus technical Data Science credits.
* **Workload Bandwidth:** A comparison tracking semester GPA variations against attempted credit loads.
* **Extracurricular Allocation:** A historical look at weekly hour investments per term.
* **Credit Load Distribution:** A frequency analysis of semester operational modes.
* **Performance Matrix:** A scatter analysis exploring my academic threshold under weight.
* **Leadership Efficiency Index:** A dual-metric evaluation pairing structural hour investments against realized project impacts.

## ⚖️ Ethical Integration
To uphold responsible data communication standards, the dashboard explicitly highlights:
* **Privacy Controls:** Complete anonymization of all third-party details, participant counts, and sensitive operational frameworks.
* **Limitation Disclosures:** Transparent acknowledgment of historical memory bias regarding self-estimated tracking hours and subjective grading scales.
* **Responsible Decision-Making:** Data-backed actionable conclusions to guide optimal credit-to-extracurricular balances in future semesters.

## 🛠️ Tech Stack & Setup
* **Language:** Python
* **Framework:** Streamlit (Hosted via Streamlit Community Cloud)
* **Data Processing:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn

### Local Installation
To run this dashboard locally, clone the repository and run the following commands in your terminal:
```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)

# Navigate into the project folder
cd YOUR_REPO_NAME

# Install dependencies
pip install -r requirements.txt

# Launch the Streamlit app
streamlit run app.py
