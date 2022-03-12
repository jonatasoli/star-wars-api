from typing import List

from pydantic import BaseModel


class Film(BaseModel):
    title: str
    release_date: str


class Planet(BaseModel):
    name: str
    climate: str
    diameter: str
    population: str
    films: List[Film]


class PlanetList(BaseModel):
    result: List[Planet]


class PlanetNotFound(Exception):
    pass


class APINotFoundData(Exception):
    pass
