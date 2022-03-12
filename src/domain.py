from typing import List

from pydantic import BaseModel


class Film(BaseModel):
    title: str
    release_date: str


class Planet(BaseModel):
    name: str
    climate: str
    diameter: int
    population: int
    films: List[Film]


class PlanetList(BaseModel):
    result: List[Planet]
