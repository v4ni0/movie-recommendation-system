"""Domain models for the recommendation system."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Movie:
    id: int
    title: str
    overview: str
    genres: str
    keywords: str
    poster_path: str | None = None


@dataclass(frozen=True, slots=True)
class Recommendation:
    id: int
    title: str
    score: float
