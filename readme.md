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

- Create a virtual environment and install the dependencies:
  
  ```py
  python -m venv mlops
  .\mlops\Scripts\activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

#### Step 4: Create a pipeline YAML file
- In VS Code, create a folder `.github/workflows`.
- Inside, create a YAML file, e.g., `mlops-pipeline.yml`.
  ```yaml
  name: MLOps Pipeline

  on:
    push:
      paths:
        - 'data/**'       # trigger only when data changes
        - 'src/**'        # trigger only when source code changes

    jobs:
      retrain:
        runs-on: ubuntu-latest

        steps:
        - name: Checkout repository
            uses: actions/checkout@v3

        - name: Set up Python
            uses: actions/setup-python@v4
            with:
            python-version: '3.13.7'

        - name: Install dependencies
            run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
  ```
