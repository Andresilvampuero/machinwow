"""
This is a boilerplate pipeline 'relleno_datos'
generated using Kedro 0.19.7
"""

from kedro.pipeline import Pipeline , node
from wow.pipelines.relleno_datos.nodes import fill_missing_values


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=fill_missing_values,
                inputs=["zones"],
                outputs="cleaned_zones1",
                name="fill_missing_values_node"
            ),
        ]
    )
