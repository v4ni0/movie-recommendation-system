from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = str(BASE_DIR / "data" / "raw" / "movies.csv")
PROCESSED_DATA_PATH = str(BASE_DIR / "data" / "processed" / "cleaned_movies.csv")
INDEX_PATH = str(BASE_DIR / "models" / "movies_v1.index")
MODEL_NAME = "all-MiniLM-L6-v2"
TOP_K = 5
