
# Wine Quality Prediction

## Project Overview

This project is a **Wine Quality Prediction** tool that helps users predict the quality of wine based on various input parameters such as acidity, alcohol content, sugar levels, etc. The prediction is made using a **regression model** trained on a pre-existing dataset of wine quality scores, and the frontend interface is developed using **Tkinter** for easy user interaction.

## Features

- **Regression-based Model**: The project uses a machine learning regression model to predict wine quality based on several features.
- **Tkinter Frontend**: A user-friendly GUI built with Tkinter for inputting wine parameters and viewing predictions.
- **CSV Dataset**: The project uses a CSV file containing historical wine quality data to train and evaluate the model.

## Parameters Considered

The model takes the following wine characteristics as input:

1. **Fixed Acidity**: The level of fixed acids in the wine, which contributes to its tartness.
2. **Volatile Acidity**: The amount of volatile acids that can affect the wine's aroma and flavor.
3. **Citric Acid**: A key acid that adds freshness to the wine.
4. **Residual Sugar**: The amount of sugar remaining after fermentation.
5. **Chlorides**: The salt level in the wine, which can impact the taste.
6. **Free Sulfur Dioxide**: This preserves the wine and prevents oxidation.
7. **Total Sulfur Dioxide**: A measure of the total SO₂ levels, which also affects preservation.
8. **Density**: The wine's density, indicating sugar and alcohol content.
9. **pH Level**: The pH level indicates the wine's acidity.
10. **Sulphates**: These contribute to the wine's body and flavor.
11. **Alcohol Content**: The percentage of alcohol by volume.
12. **Wine Age**: The age of the wine can also impact its flavor and quality.

## Getting Started

### Prerequisites

To run this project, you'll need:

- **Python 3.x**
- **Tkinter** (Python’s standard GUI library)
- **Pandas**
- **Scikit-learn** (for the machine learning model)

### Installation

1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/unusualmold2003/winequality.git
   \`\`\`
2. Navigate to the project directory:
   \`\`\`bash
   cd winequality
   \`\`\`

### Running the Project

1. Ensure that the **wine_data.csv** file is in the root directory of the project.
2. Run the following command to launch the Tkinter interface:
   \`\`\`bash
   python 6.py
   \`\`\`
3. Input the required wine characteristics in the provided fields and click "Predict" to see the wine quality score.

## Model Details

The project uses a **linear regression model** to predict wine quality. The model was trained using a dataset of over 1,500 wine samples, with features like acidity, alcohol content, and others serving as predictors. The target variable is the wine's quality, rated on a scale from 0 to 10.

### Model Training

- **Algorithm**: Linear Regression
- **Evaluation**: Mean Squared Error (MSE), R² score

You can retrain the model with different algorithms like Random Forest, Decision Trees, or Gradient Boosting to further improve accuracy.
