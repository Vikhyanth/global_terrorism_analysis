Global Terrorism Data Analysis Project

--------------------------------------

**🌍 Project Overview**

-----------------------

This project leverages **Big Data Analytics** and **Data Mining** techniques to analyze global terrorism data. The goal is to uncover patterns, trends, and insights into terrorist activities worldwide. By visualizing and clustering incidents, the project identifies high-risk regions, common attack types, and other critical factors, providing actionable insights for informed decision-making.

**✨ Key Features**

------------------

*   **📊 Data Preprocessing**: Cleaned and normalized raw data by handling missing values and removing duplicates for accurate analysis.

*   **📈 Exploratory Data Analysis (EDA)**: Visualized trends in terrorist activities by region, attack type, success rate, and other factors using Python libraries like Matplotlib, Seaborn, and Plotly.

*   **🔍 Clustering Analysis**: Applied K-Means clustering to group incidents based on geographical locations (latitude and longitude).

*   **🗺️ Geographical Heatmap**: Created an interactive heatmap using Plotly to visualize the intensity of terrorism across different regions with a color scale ranging from green (low intensity) to red (high intensity).

*   **🤖 Predictive Modeling**: Built machine learning models (e.g., Logistic Regression) to predict the success of terrorist attacks based on features like attack type and suicide involvement.

**🛠️ Tools and Technologies**

------------------------------

*   **Programming Languages**: Python

*   **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Plotly, Scikit-learn

*   **Data Processing**: Apache Spark (optional for large datasets)

*   **Visualization Tools**: Plotly Express, Matplotlib

*   **Database Management**: PostgreSQL (optional for storing processed data)



**🚀 Steps to Reproduce**

-------------------------

1\.  bashgit clone https://github.com/your-username/global-terrorism-analysis.gitcd global-terrorism-analysis

2\.  bashpip install -r requirements.txt

3\.  Place the dataset (global\_terrorism.csv) in the data/ directory.

4\.  bashpython scripts/data\_preprocessing.py

5\.  Explore visualizations in the notebooks/eda.ipynb Jupyter Notebook.

6\.  bashpython scripts/clustering\_analysis.py

7\.  Generate geographical heatmaps using Plotly.

**🔑 Key Insights**

-------------------

*   Regions with the highest frequency of terrorist incidents include South Asia and the Middle East.

*   Bombings/Explosions are the most common attack type globally.

*   Success rates of attacks vary significantly based on attack type and target.

**📈 Visualizations**

---------------------

Examples of Generated Visualizations:

-------------------------------------

1\.  Bar chart of terrorist incidents by region.

2\.  Horizontal bar chart of attack types.

3\.  Geographical heatmap showing terrorism intensity across regions.

All visualizations are saved in the visualizations/ folder as .jpg files.

**🌟 Future Work**

------------------

*   Expand predictive modeling to include more features for better accuracy.

*   Integrate real-time data streams for live terrorism monitoring.

*   Develop an interactive dashboard for visualization results.

**👨‍💻 Skills Demonstrated**

-----------------------------

*   Data Cleaning & Preprocessing

*   Exploratory Data Analysis (EDA)

*   Clustering & Machine Learning

*   Data Visualization with Python

*   Big Data Processing
