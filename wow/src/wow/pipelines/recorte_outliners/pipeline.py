"""
This is a boilerplate pipeline 'recorte_outliners'
generated using Kedro 0.19.7
"""

from kedro.pipeline import Pipeline, node
from wow.pipelines.recorte_outliners.nodes import filter_outliers


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=filter_outliers,
                inputs="cleaned_wowah_data",
                outputs="wowah_data_procesado",
                name="filter_outliers_node"
            ),
        ]
    )
