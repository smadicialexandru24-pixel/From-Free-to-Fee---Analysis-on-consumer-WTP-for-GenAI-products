# From-Free-to-Fee---Analysis-on-consumer-WTP-for-GenAI-products
Repository for all the data processing for the named dissertation
# Dissertation Data Analysis: Consumer Privacy & AI Pricing Sensitivity

---

### Copy-Pasteable `README.md` Text

```markdown
# Dissertation Data Analysis: Consumer Privacy & AI Pricing Sensitivity

This repository contains the dataset, data cleaning pipelines, and statistical analysis scripts used for my dissertation. The project evaluates user behaviors regarding data privacy in high-stakes versus general professional fields, task-specific refusal rates for free generative AI tools, and consumer price tolerance using the Van Westendorp Price Sensitivity Meter (PSM).

## 📊 Repository Structure

To run the analyses successfully, organize your local directory as follows:
├── Data/
│   ├── H3_Data.xlsx
│   ├── Q18.xlsx
│   ├── Eng From free to fee responses.xlsx
│   └── ro_data.xlsx
├── Scripts/
│   ├── Script for H3.py
│   ├── script for Q18 plot.py
│   └── van westendrop PSM script.py
└── README.md

---

## 🛠️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
   cd your-repo-name

```

2. **Install Required Libraries:**
The scripts are written in Python 3 and require the following data science and statistical packages:
```bash
pip install pandas numpy matplotlib scipy openpyxl

```


3. **Data Path Configuration:**
*Note: By default, the scripts look for data files in your local Mac/Windows `Documents` folder using `os.path.expanduser('~')/Documents`. If you clone this repository, update the file path variables in the scripts to point to your data directory.*

---

## 🔬 Scripts & Analysis Pipeline

### 1. Hypothesis 3 Analysis: Privacy Choice by Stake Level (`Script for H3.py`)

* **Objective:** Test whether professionals in high-stakes fields (Legal, Healthcare, Finance) make different privacy choices compared to those in general fields (Tech, Creative, Academia).
* **Methodology:** * Groups respondents into categorical bins based on their `Professional_Field`.
* Generates a contingency table comparing `Stake_Level` against `Privacy_Choice` (Item 15).
* Executes a **Chi-Square Test of Independence** via `scipy.stats.chi2_contingency` to calculate the $p$-value.


* **Output:** Prints the frequency table and $p$-value to the console; exports a publication-grade clustered bar chart (`H3_Results_Chart.png`).

### 2. Hypothesis 2 Analysis: Multi-Response Refusal Frequencies (`script for Q18 plot.py`)

* **Objective:** Analyze and visualize why and where users refuse to use free AI tools based on specific high-risk tasks.
* **Methodology:** * Handles multi-response text data by splitting comma-separated strings (`.str.split(', ')`) and flattening them (`.explode()`).
* Calculates both total counts and sample percentages ($N=302$).


* **Output:** Prints descriptive statistics to the console and generates a horizontal bar chart (`Hypothesis_2_Plot.png`) tracking task categories against refusal percentages.

### 3. Pricing Strategy: Van Westendorp PSM (`van westendrop PSM script.py`)

* **Objective:** Determine the Optimal Price Point (OPP) and Indifference Price Point (IPP) for an AI subscription model across combined English and Romanian sample sizes.
* **Methodology & Data Cleaning:**
* **Data Consolidation:** Merges English and Romanian data subsets, aligning numerical responses for four key metrics: *Too Cheap*, *Cheap (Bargain)*, *Expensive*, and *Too Expensive*.
* **Logic Scrub:** Filters out logically invalid survey responses (e.g., cases where a user defined "Too Cheap" as a higher monetary value than "Expensive").
* **Statistical Outlier Filtering:** Utilizes Interquartile Range (IQR) filtering on the *Too Expensive* category. Establishes a generous statistical upper ceiling ($Q3 + 2.0 \times IQR$) to eliminate troll responses (e.g., $1,000 values) without deleting legitimate high-intent buyers.


* **Output:** Plots the four cumulative distribution curves to find pricing thresholds and saves the plot as `PSM_Graph_Refined.png`.

---

## 📈 Key Findings & Visualization Reproducibility

Running these scripts will automatically regenerate the statistical values and visual graphs utilized in Chapter 4 (Results & Analysis) of the dissertation.

* The Chi-Square test evaluates statistical significance ($\alpha = 0.05$).
* The Van Westendorp graph dynamically clips the X-axis to standard bounds to guarantee clean readability.
