# MLOps

### 🎯 Goals of the project

### 👣 Steps

#### Step 1: Setup GitHub Repository
- Create a GitHub repository
- Clone the repository to you local machine
  
#### Step 2: Create a project structure
- Create a folder structure comparable to:
  ```
    mlops-demo/
    │
    ├── data/
    │   └── sample.csv
    ├── src/
    │   ├── train.py
    │   └── predict.py
    ├── requirements.txt
    └── README.md
  ```

#### Step 3: Setup dependencies
- Write the dependencies in the requirements.txt file
  ```
  pandas
  scikit-learn
  joblib
  ```
  
- Create a virtual environment and install the dependencies
  ``` python
  python -m venv mlops
  .\mlops\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

#### Step 4

