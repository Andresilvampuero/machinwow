"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from wow.pipelines.normalizar_datos.pipeline import create_pipeline as borrar_espacios, create_transformar_pipeline as normalizar
from wow.pipelines.relleno_datos.pipeline import create_pipeline as relleno
from wow.pipelines.recorte_outliners.pipeline import create_pipeline as outliers

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    pipelines["1"] = relleno()
    pipelines["2"] = borrar_espacios()
    pipelines["3"] = normalizar()
    pipelines["4"] = outliers()
    pipelines["__default__"] = sum(pipelines.values())
    return pipelines
