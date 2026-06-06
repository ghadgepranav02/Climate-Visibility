from datetime import datetime
import os


MONGO_DATABASE_NAME = "visibility"

TARGET_COLUMN = "VISIBILITY"
CLUSTER_LABEL_COLUMN = "Cluster"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = os.path.join("artifacts")