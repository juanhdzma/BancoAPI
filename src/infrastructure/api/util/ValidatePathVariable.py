from typing import Type, TypeVar
from fastapi import Depends, Request

T = TypeVar('T')

def make_model(model_type: Type[T]) -> T:
    def _make_model(req: Request):
        path_params = req.path_params
        return model_type.model_validate(path_params)
    return Depends(_make_model)