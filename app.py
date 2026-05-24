import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set widescreen layout for the dashboard web page
st.set_page_config(page_title="My Holistic Journey", page_icon="🚀", layout="wide")

# Apply clean background styling defaults for plots
sns.set_theme(style="whitegrid", palette="muted")

# =====================================================================
# DATA LOADING
# =====================================================================
@st.cache_data
def load_growth_data():
    df = pd.read_csv('khant_growth_journey.csv')
    df['Semester_GPA'] = pd.to_numeric(df['Semester_GPA'], errors='coerce')
    return df

@st.cache_data
def load_raw_journey():
    # This dataset uses 'IP' instead of empty for Spring 2026 GPA
    return pd.read_csv('Khant_Journey.csv')

@st.cache_data
def load_hobbies():
    return pd.read_csv('khant_hobbies.csv')

df_growth = load_growth_data()
df_raw = load_raw_journey()
df_hobbies = load_hobbies()

# =====================================================================
# SIDEBAR
# =====================================================================
st.sidebar.image("parami.jpg", width=100)
st.sidebar.header("Khant's Dashboard Filters")
st.sidebar.write("Filter the academic timeline:")

all_years = df_growth['Academic_Year'].unique()
selected_years = st.sidebar.multiselect(
    "Select Academic Year(s):",
    options=all_years,
    default=all_years
)

filtered_df = df_growth[df_growth['Academic_Year'].isin(selected_years)]
df_gpa = filtered_df.dropna(subset=['Semester_GPA'])

st.sidebar.divider()
st.sidebar.info("💡 **Tip:** Navigate through the tabs to explore both my academic focus and my personal hobbies!")

# =====================================================================
# HEADER SECTION: Project Overview
# =====================================================================
st.title("🚀 Khant's Journey: Academic Focus & Personal Balance")
st.markdown("""
Welcome to my Data Communication & Ethics Final Project. 
This dashboard tracks my transformation at Parami University, from a broad undergraduate explorer into a focused data science student and leader. But a person is more than just grades and credit hours! To provide a complete narrative, this dashboard incorporates **three distinct datasets**, exploring both my rigorous academic experience and the personal hobbies (music, movies, and art) that fuel my creativity and keep me balanced.
""")

st.divider()

# Create overarching tabs for the whole app
tab_academic, tab_hobbies, tab_ethics = st.tabs([
    "📚 Academic Focus", 
    "🎨 Personal Balance (Hobbies)",  
    "⚖️ Ethics & Disclosures"
])

# =====================================================================
# TAB 1: THE ACADEMIC FUNNEL (Original Dashboard logic, made aesthetic)
# =====================================================================
with tab_academic:
    st.header("The Academic Focus: From Broad to Targeted")
    st.markdown("As I progressed through my degree, my course load shifted dramatically from general humanities to specialized technical data credits.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("1. The Overall Credit Split")
        fig1, ax1 = plt.subplots(figsize=(6, 6))
        total_tech = filtered_df['Tech_Data_Credits'].sum()
        total_hum = filtered_df['Hum_Soc_Credits'].sum()
        
        if total_tech == 0 and total_hum == 0:
            st.write("No data available for the selected years.")
        else:
            ax1.pie([total_tech, total_hum], labels=['Tech/Data Credits', 'Hum/Soc Credits'],
                    autopct='%1.1f%%', colors=['#4C72B0', '#55A868'], startangle=90, explode=[0.05, 0])
            ax1.set_title("Total Credit Distribution")
            st.pyplot(fig1)
            st.caption("*Insight:* Shows the cumulative balance of my coursework.")

    with col2:
        st.subheader("2. The Semesterly Shift")
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        if not filtered_df.empty:
            x = np.arange(len(filtered_df['Semester']))
            width = 0.35
            ax2.bar(x - width/2, filtered_df['Tech_Data_Credits'], width, label='Tech & Data', color='#4C72B0')
            ax2.bar(x + width/2, filtered_df['Hum_Soc_Credits'], width, label='Humanities & Social', color='#55A868')
            ax2.set_xticks(x)
            ax2.set_xticklabels(filtered_df['Semester'], rotation=45)
            ax2.set_ylabel("Credits")
            ax2.set_title("Tech vs. Hum/Soc Credits per Semester")
            ax2.legend()
            st.pyplot(fig2)
        st.caption("*Insight:* The explicit transition from humanities-heavy early terms to purely technical later terms.")

    st.divider()

    st.header("Workload vs. Academic Performance")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("3. Semester GPA Trend")
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        if not df_gpa.empty:
            sns.barplot(data=df_gpa, x='Semester', y='Semester_GPA', ax=ax3, palette='Blues_d')
            ax3.set_ylim(0, 4.0)
            for i, v in enumerate(df_gpa['Semester_GPA']):
                ax3.text(i, v + 0.05, str(round(v, 2)), ha='center', va='bottom')
            plt.xticks(rotation=45)
            st.pyplot(fig3)
        else:
            st.warning("No GPA data available for selected years.")

    with col4:
        st.subheader("4. Extracurricular Hours vs. Leadership Impact")
        fig4, ax4 = plt.subplots(figsize=(8, 5))
        if not filtered_df.empty:
            sns.scatterplot(data=filtered_df, x='Est_Club_Hours_Weekly', y='Leadership_Impact_Score',
                            hue='Academic_Year', s=150, palette='deep', ax=ax4)
            ax4.set_title("Efficiency in Leadership")
            st.pyplot(fig4)
        st.caption("*Insight:* Paradoxically, fewer hours later in my journey yielded higher impact, showing the value of deep focus.")


# =====================================================================
# TAB 2: PERSONAL BALANCE (HOBBIES)
# =====================================================================
with tab_hobbies:
    st.header("🎨 Beyond Academics: The Art of Balance")
    st.markdown("""
    Managing a highly technical 20-credit semester and leadership roles like **Borderless Futures** requires a strong mental reset. 
    My secondary dataset explores my personal tastes—the movies, series, songs, and art that I use to recharge. Let's explore the distribution of my 30 tracked favorites.
    """)
    
    col_a, col_b, col_c = st.columns(3)
    col_a.metric("Total Favorites Tracked", len(df_hobbies))
    col_b.metric("Top Music Artist", df_hobbies[df_hobbies['Category'] == 'Song']['Artist'].mode()[0])
    col_c.metric("Average Rating", f"{df_hobbies['Rating_Out_Of_10'].mean():.1f} / 10")

    st.divider()

    col5, col6 = st.columns([1.5, 1])
    
    with col5:
        st.subheader("Hobby Distribution by Category")
        fig_h1, ax_h1 = plt.subplots(figsize=(10, 5))
        sns.countplot(data=df_hobbies, y='Category', palette='pastel', order=df_hobbies['Category'].value_counts().index, ax=ax_h1)
        ax_h1.set_xlabel("Number of Items")
        ax_h1.set_ylabel("Category")
        st.pyplot(fig_h1)
        st.caption("*Storytelling Insight:* Music dominates my list. Songs are the easiest to integrate into a busy routine—whether I'm writing Python scripts or studying Data Communications, artists like Taylor Swift and Alan Walker are usually playing in the background.")

    with col6:
        st.subheader("Rating Quality")
        fig_h2, ax_h2 = plt.subplots(figsize=(6, 5))
        sns.boxplot(data=df_hobbies, x='Category', y='Rating_Out_Of_10', palette='Set2', ax=ax_h2)
        ax_h2.set_ylabel("Rating (out of 10)")
        st.pyplot(fig_h2)
        st.caption("*Storytelling Insight:* I am highly selective with my time. Most ratings are 8 or above, meaning I only commit my limited free time to top-tier entertainment like *Game of Thrones* or *Inception*.")

    st.subheader("Explore the Favorites Database")
    st.dataframe(df_hobbies, use_container_width=True)


# =====================================================================
# TAB 3: ETHICS & DISCLOSURES
# =====================================================================
with tab_ethics:
    st.header("⚖️ Ethics & Responsibility Disclosures")
    st.markdown("As developed in the initial project phases, data communication must be responsible.")
    
    st.markdown("""
    ### **🔒 Privacy Protections**
    * **Data Bounds:** This application utilizes my public undergraduate academic metrics and aggregated tracking estimations.
    * **Anonymization and Controls:** Third-party personal details, institutional grading logs, and private team operations regarding initiatives like **Borderless Futures** or **CIIF** have been excluded or anonymized.

    ### **⚠️ Bias & Limitations**
    * **Historical Memory Bias:** Extracurricular hours for Year 1 are retroactively estimated from past recollections, introducing tracking noise.
    * **Subjective Metric Scales:** The *Leadership Impact Score* and the *Hobby Ratings* rely on a personal 1–10/1-5 self-assessment, which is an internal qualitative perception.
    * **Data Completeness Note:** The Spring 2026 dataset reflects an "In Progress" semester. GPA evaluations are omitted (NaN) to ensure data truthfulness.

    ### **📊 Visualization Choices**
    * **Pie Chart:** Selected to visualize a static, binary parts-to-a-whole breakdown of total credit splits.
    * **Bar Charts:** Used discrete columns to prevent viewers from inferring continuous chronological step changes between distinct semester blocks.
    * **Scatter & Box Plots:** Used to isolate coordinate trends (efficiency) and distributions (hobby quality) cleanly.
    """)

# Footer
st.divider()
st.markdown("<p style='text-align: center; color: gray;'>Designed by Khant Razar Kyaw for DATA 201 | Including Academic & Personal Datasets</p>", unsafe_allow_html=True)
