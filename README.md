# species_category_prediction
**Data Collection and Development of Machine Learning Pipelines in Cloud**

**🐾 Project Overview**

This project focuses on predicting the conservation status of various species using machine learning techniques. The model classifies species into one of several IUCN categories: Least Concern, Near Threatened, Vulnerable, Endangered, Critically Endangered, or Extinct.

**Key features used for prediction include:**

Habitat

Number of threats

Population trends

Existing category status

Data was collected from the website [https://www.iucnredlist.org/]() through automated web scraping. By analyzing patterns within this dataset using advanced algorithms, the goal is to provide actionable insights that support global conservation efforts.


![image](https://github.com/user-attachments/assets/0bdd4347-eba9-49fc-9ff0-3c573a10a7b0)

**SAMPLE CSV**


![image](https://github.com/user-attachments/assets/7558923b-c7b5-4d61-a6b5-44f6b909a73e)


**WEBSITE USED**

![image](https://github.com/user-attachments/assets/0824aab4-49c8-4e5d-95b7-77ca328e55b6)



![image](https://github.com/user-attachments/assets/984386be-e62a-4961-9b20-8798face3048)


**🧪 DATA PIPELINE**

![image](https://github.com/user-attachments/assets/d24eb30a-773a-405b-928f-cb2021169ffa)



**1. Data Collection (Scraping via Selenium)**

Automated data scraping is performed from the IUCN Red List website. The script extracts important species attributes such as name, habitat, number of threats, population trends, and category status.

**2. Clean Missing Data** 

Rows with null values in critical columns like habitat or category status are removed to ensure data integrity.

**3. Data Preprocessing**


Convert textual values (like population trends) into categorical codes or numerical equivalents.

Generation length is converted to integers.

Remaining missing values are replaced using appropriate strategies (like median imputation).

**4. Data Storage (Azure Blob)**

The cleaned dataset is stored in Microsoft Azure’s cloud storage for scalability and easy access during model training and deployment.

**5. Data Splitting**

The dataset is split into training and testing subsets — typically 70% for training and 30% for testing — to validate model performance.

**6. Model Building (Azure ML Studio)**

Multiple algorithms are evaluated, including:

Logistic Regression

Decision Forest

Multiclass Neural Network

Boosted Decision Tree (selected for deployment due to best performance)

**7. Train Model**

The model is trained on the training dataset, adjusting internal parameters to minimize prediction error.

**8. Feature Selection**

Only relevant columns such as habitat, threats, population trend, generation length, etc., are selected to improve model performance and reduce noise.

**9. Score Model**

The trained model is tested against the unseen 30% of the dataset to generate performance scores like accuracy, precision, recall, and F1 score.

**10. Evaluate Model**

Based on evaluation metrics, the best-performing model (Boosted Decision Tree) is selected for final deployment.

**11. Model Deployment (via REST API)**

The model is deployed using Azure and exposed via a REST API. This allows real-time predictions through tools like Postman or web applications.

**EVALUATION METRICS**

![image](https://github.com/user-attachments/assets/c908add8-c20e-460d-9319-154ad5a9a2f6)

FOR DIFFERENT ML MODELS



**🧠 ACCURACY OPTIMIZATION PROCESS**


**Data Collection**
Selenium was used to scrape diverse data from the IUCN Red List, including habitat type, threats, population trends, and conservation status of species.

**Data Cleaning**
The dataset was refined by removing duplicates, handling missing values with median imputation, converting generation lengths to integers, and dropping rows with critical null fields.
**
Algorithm Comparison**
Multiple machine learning algorithms were evaluated:

Multiclass Neural Network

Decision Forest

Multiclass Boosted Decision Tree

The Boosted Decision Tree demonstrated superior performance and was selected for final deployment.
**
📊 MODEL EVALUATION METRICS**


**Multiclass Neural Network Results**

Overall Accuracy: 0.5235

Micro Precision: 0.5235

Macro Precision: 0.3152

Micro Recall: 0.5235

Macro Recall: 0.3245

**Multiclass Boosted Decision Tree Results**

Overall Accuracy: 0.6185

Micro Precision: 0.6185

Macro Precision: 0.4254

Micro Recall: 0.6185

Macro Recall: 0.3982

**Performance Insight:**
The Boosted Decision Tree provided a 6–8% increase in accuracy and precision over previous models.
















