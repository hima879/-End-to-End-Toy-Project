# End-to-End Toy Project — Student Placement Predictor

A minimal end-to-end machine learning project: from data → model training → deployment.
Predicts whether a student will be **placed** based on their **CGPA** and **IQ**.

**🔗 Live demo:** https://va2nttsqbrxhlp3ij4t2dd.streamlit.app/

---

## Overview

This project walks through the full ML lifecycle on a tiny toy dataset:

1. Load & preprocess data (`placement.csv`)
2. Exploratory Data Analysis (EDA) + feature selection
3. Extract input (`cgpa`, `iq`) and output (`placement`) columns
4. Train/test split
5. Train a **Logistic Regression** classifier
6. Evaluate (~95% accuracy on the test set)
7. Deploy as an interactive **Streamlit** web app

---

## Project Structure

```
End-to-End-Toy-Project/
├── End_to_End_Toy.ipynb     # Jupyter notebook: EDA, training, evaluation
├── app.py                   # Streamlit app (loads model & serves predictions)
├── train.py                 # Standalone script to retrain the model
├── placement.csv            # Dataset (100 rows: cgpa, iq, placement)
├── requirements.txt         # Python dependencies
└── README.md
```

---

## Dataset

`placement.csv` contains 100 samples with the following columns:

| Column      | Type    | Description                              |
|-------------|---------|------------------------------------------|
| `cgpa`      | float   | Student's CGPA (3.3 – 8.5)               |
| `iq`        | float   | Student's IQ score (37 – 233)            |
| `placement` | int     | Target: `1` = placed, `0` = not placed   |

---

## Model

- **Algorithm:** Logistic Regression (`sklearn.linear_model.LogisticRegression`)
- **Features:** `cgpa`, `iq`
- **Target:** `placement`
- **Test accuracy:** ~95%

The trained model is serialized with `pickle` and served by the Streamlit app.

---

## Running Locally

```bash
# 1. Clone the repo
git clone https://github.com/hima879/-End-to-End-Toy-Project.git
cd -End-to-End-Toy-Project

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate         # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Retrain the model
python train.py

# 5. Launch the Streamlit app
streamlit run app.py
```

Then open http://localhost:8501 in your browser.

---

## Deployment

The app is deployed on **Streamlit Community Cloud**.

Whenever `main` is updated on GitHub, Streamlit Cloud automatically redeploys. To trigger a manual redeploy, open the app dashboard and click **Reboot**.

> **Note on scikit-learn version:** The pickled model is version-sensitive.
> `requirements.txt` pins the same `scikit-learn` version used to train the model
> to avoid `ModuleNotFoundError` / pickle incompatibilities at load time.

---

## Usage

1. Enter a student's **CGPA** and **IQ** in the sidebar/inputs.
2. Click **Predict Placement**.
3. The app returns:
   - Placement prediction (`PLACED` / `NOT PLACED`)
   - Confidence score (probability)

---

## Tech Stack

- **Python 3**
- **scikit-learn** — modeling
- **pandas / numpy** — data handling
- **Streamlit** — web app
- **pickle** — model serialization

---

## License

This is a toy/educational project. Feel free to use it however you like.
