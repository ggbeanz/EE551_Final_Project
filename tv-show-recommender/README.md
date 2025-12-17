## TV Show Recommender

### Run Tests
From this directory:

- `python -m pytest -q`

### Preview Load The Kaggle TMDB Dataset
Keep the Kaggle CSV local (do not commit it to the repo). Run:

- `python load_preview.py --csv "C:\\path\\to\\TMDB_tv_dataset_v3.csv" --limit 1000 --show 10`

### Data Loading API
- `src/data_processor.py` provides `load_tv_shows_from_tmdb_csv(file_path, limit=1000)` which maps TMDB columns to `TVShow`.
