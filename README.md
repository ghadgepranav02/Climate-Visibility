
# Visibility Distance Prediction

A Flask-based machine learning pipeline for predicting visibility using weather data and MongoDB.

## What is included

- `app.py`: Flask app exposing `/train` and `/predict`
- `src/`: core pipeline and components
- `config/model.yaml`: model search hyperparameters
- `config/schema.yaml`: input validation schema
- `requirements.txt`: minimal runtime dependencies
- `Dockerfile`: optional container support

## Requirements

- Python 3.8+
- Either MongoDB or the provided local sample dataset

## Setup

1. Create and activate a Python environment

```bash
python -m venv venv
venv\Scripts\activate
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. (Optional) Set MongoDB environment variable if you want to use your own dataset

```powershell
$env:MONGO_DB_URL="<MONGODB_URL>"
```

If you do not set `MONGO_DB_URL`, the app will use the local sample file at `data/visibility_08012020_120000.csv`.

## Run the app

```bash
python app.py
```

Then open `http://localhost:8062/`

## Endpoints

- `GET /train`: run training pipeline
- `POST /predict`: make a visibility prediction from form input

## Notes

- The training pipeline loads data from MongoDB if configured, otherwise uses the local sample dataset.
- Model artifacts are saved locally.

## Conclusion

- This Project can be used in real-life by Users.
