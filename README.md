# What Drives GitHub Repository Success? A Data-Driven Analysis of Open-Source Projects

## Overview

This repository contains the code and data analysis for the study **"What Drives GitHub Repository Success? A Data-Driven Analysis of Open-Source Projects."**

The project investigates factors associated with GitHub repository popularity using a dataset of the top 500 repositories ranked by stars. The analysis focuses on relationships between repository popularity, programming language distribution, repository size, and forking activity.

## Research Questions

* What factors are most associated with GitHub repository popularity (measured by stars)?
* Which programming languages are most commonly represented among highly popular repositories?
* What is the relationship between repository popularity and characteristics such as forks and repository size?
* What distinguishes the top 10% repositories from the rest?

## Dataset

The dataset was obtained from Kaggle:

* GitHub Top 500 Repositories by Stars
* Author: Muhammad Ibrahim Qasmi

The dataset contains repository-level information, including:

* Repository name
* Description
* Programming language
* Number of stars
* Number of forks
* Repository size

## Methodology

The analysis was performed using Python in a Jupyter Notebook environment.

Main steps:

1. Data cleaning and preprocessing
2. Exploratory data analysis (EDA)
3. Visualization of repository characteristics
4. Correlation analysis
5. Comparison of top 10% repositories with the remaining repositories

## Main Findings

* Repository popularity exhibits a highly skewed distribution.
* Stars and forks show a moderately strong positive correlation.
* Repository size has virtually no relationship with popularity.
* Python, TypeScript, and JavaScript are strongly represented among highly popular repositories.
* Community engagement appears to be more strongly associated with repository success than repository size.

## Research Paper

The final research paper is available as:

- `paper.pdf`

## Repository Structure

```text
.
├── data/
│   └── raw/
│       └── GitHub_Top_500_Repos_By_Stars.csv
├── notebooks/
│   └── github_success_analysis.ipynb
├── src/
│   └── clean_data.py
├── visuals/
│   ├── language_distribution.png
│   ├── stars_distribution.png
│   └── stars_vs_forks.png
│   └── stars_vs_sizes.png
├── paper.pdf
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Running the Analysis

```bash
jupyter notebook
```

Open the notebook and execute all cells.

## Feedback and Contact

This project was developed as part of an independent undergraduate research study. I welcome suggestions, constructive criticism, and discussions regarding the methodology, results, or potential extensions of this work.

If you would like to get in touch, you can contact me via:

* Email: [n.azizov@ufaz.az](mailto:n.azizov@ufaz.az)
* LinkedIn: https://linkedin.com/in/n1azizov

Thank you for your interest in this project.

## Author

Nadir Azizov

Bachelor of Science in Computer Science

French-Azerbaijani University (UFAZ)