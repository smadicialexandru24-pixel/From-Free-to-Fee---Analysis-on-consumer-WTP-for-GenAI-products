# From-Free-to-Fee---Analysis-on-consumer-WTP-for-GenAI-products
Repository for all the data processing for the named dissertation
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

2. Install Required Libraries:
 The scripts are written in Python 3 and require the following data science and statistical packages:

Bash
pip install pandas numpy matplotlib scipy openpyxl

3. Data Path Configuration:
Note: By default, the scripts look for data files in your local Mac/Windows Documents folder using os.path.expanduser('~')/Documents. If you clone this repository, update the file path variables in the scripts to point to your data directory.
