from __future__ import annotations

import pandas as pd

from src.models import Movie
from src.config import PROCESSED_DATA_PATH


class MovieRepository:
    def __init__(self, data: pd.DataFrame) -> None:
        self._data = data

    def __len__(self) -> int:
        return len(self._data)

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._data

    def get_by_indices(self, indices: list[int]) -> list[Movie]:
        rows = self._data.iloc[indices]
        return [
            Movie(
                id=int(row["id"]),
                title=str(row["title"]),
                overview=str(row.get("overview", "")),
                genres=str(row.get("genres", "")),
                keywords=str(row.get("keywords", "")),
                poster_path=row.get("poster_path"),
            )
            for _, row in rows.iterrows()
        ]

    def get_by_id(self, movie_id: int) -> Movie | None:
        match = self._data[self._data["id"] == movie_id]
        if match.empty:
            return None
        row = match.iloc[0]
        return Movie(
            id=int(row["id"]),
            title=str(row["title"]),
            overview=str(row.get("overview", "")),
            genres=str(row.get("genres", "")),
            keywords=str(row.get("keywords", "")),
            poster_path=row.get("poster_path"),
        )

    def content_series(self) -> list[str]:
        return self._data["content"].tolist()
