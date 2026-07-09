# Cognifyz Internship - Data Science Projects

This repository contains data science and machine learning projects completed during the Cognifyz Technologies internship. The work progresses through three levels, with increasing complexity in data analysis and predictive modeling.

## 📋 Project Overview

This internship focuses on practical data science skills using a restaurant dataset, covering exploratory data analysis (EDA), statistical analysis, and machine learning model development.

## 📁 Repository Structure

```
cognifyz_internship/
├── README.md                                    # Project documentation
├── Dataset.csv                                  # Main restaurant dataset
├── test.py                                      # Testing utilities
├── level1_ All tasks.py                         # Level 1: Basic EDA
├── levell3_task1.py                             # Level 3: Predictive modeling
├── level3_task2.py                              # Level 3: Cuisine analysis
├── level3_task3.py                              # Level 3: Additional analysis
├── COGNIFYZ TECHNOLOGIES_internship.docx        # Internship documentation
├── COGNIFYZ TECHNOLOGIES level3 report.docx    # Level 3 final report
└── video llink.txt                              # Related video resources
```

## 📊 Dataset

**File:** `Dataset.csv`

The dataset contains restaurant information with the following key features:
- **Aggregate rating**: Restaurant quality ratings
- **Cuisines**: Types of cuisine offered
- **Average Cost for two**: Cost metric for pricing analysis
- **Price range**: Restaurant pricing tier
- **Votes**: Customer engagement metric

**Size:** ~2.2 MB

## 🎯 Project Levels

### Level 1: Exploratory Data Analysis (EDA)
**File:** `level1_ All tasks.py`

**Objectives:**
- Load and explore the dataset structure
- Analyze data types and missing values
- Generate statistical summaries
- Visualize rating distributions

**Key Tasks:**
- Dataset shape and column inspection
- Data type identification
- Missing value detection
- Distribution analysis with visualizations (histograms)
- Summary statistics

### Level 3: Advanced Analysis & Machine Learning
**Files:** 
- `levell3_task1.py`
- `level3_task2.py`
- `level3_task3.py`

#### Task 1: Predictive Modeling
**Objective:** Build regression models to predict restaurant aggregate ratings

**Models Implemented:**
1. **Linear Regression** - Baseline model
2. **Decision Tree Regressor** - Non-linear relationships
3. **Random Forest Regressor** - Ensemble method

**Features Used:**
- Average Cost for two
- Price range
- Votes

**Evaluation Metrics:**
- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)

#### Task 2: Cuisine Analysis
**Objective:** Analyze restaurant cuisines to identify trends and preferences

**Analysis Includes:**
- Average ratings by cuisine type
- Most popular cuisines (by customer votes)
- Restaurant count by cuisine
- Top 10 rankings for each metric

#### Task 3: Additional Analysis
**Objective:** Extended data exploration and insights

## 🛠️ Technologies & Libraries

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning models and metrics
- **Matplotlib** - Data visualization
- **NumPy** - Numerical computations

## 📈 Key Insights

The analysis covers:
- Rating distribution patterns across restaurants
- Cuisine popularity and customer preferences
- Correlation between cost, price range, votes, and ratings
- Model performance comparison for rating prediction
- Statistical relationships in restaurant data

## 📄 Documentation

- **COGNIFYZ TECHNOLOGIES_internship.docx** - Detailed internship overview and task descriptions
- **COGNIFYZ TECHNOLOGIES level3 report.docx** - Comprehensive analysis report for Level 3

## 🚀 How to Run

1. Ensure all dependencies are installed:
   ```bash
   pip install pandas scikit-learn matplotlib numpy
   ```

2. Place `Dataset.csv` in the project directory

3. Run individual task files:
   ```bash
   python "level1_ All tasks.py"
   python levell3_task1.py
   python level3_task2.py
   python level3_task3.py
   ```

## 📝 Notes

- Some file paths in Level 1 code may need adjustment based on local directory structure
- All analyses assume the Dataset.csv is in the same directory as the Python scripts
- Random state is set to 42 for model reproducibility

## 👤 Author

**Yarrabothulajayanth**

Cognifyz Technologies Data Science Internship

## 📚 Learning Outcomes

Through this internship project, skills developed include:
- Exploratory Data Analysis (EDA)
- Data preprocessing and cleaning
- Regression modeling
- Machine learning model evaluation
- Data visualization
- Statistical analysis
- Ensemble learning methods

---

*Last Updated: 2026*
