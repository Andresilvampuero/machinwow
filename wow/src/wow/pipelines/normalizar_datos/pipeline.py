"""
This is a boilerplate pipeline 'normalizar_datos'
generated using Kedro 0.19.7
"""

from kedro.pipeline import Pipeline, pipeline, node
from wow.pipelines.normalizar_datos.nodes import strip_column_names, convert_columns_to_int, process_wowah_data


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=strip_column_names,
                inputs="locations",
                outputs="cleaned_locations",
                name="strip_column_names_locations"
            ),
            node(
                func=strip_column_names,
                inputs="wowah_data",
                outputs="cleaned_wowah_data",
                name="strip_column_names_wowah_data"
            ),
            node(
                func=strip_column_names,
                inputs="cleaned_zones1",
                outputs="cleaned_zones2",
                name="strip_column_names_zones"
            )
        ]
    )
def create_transformar_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=convert_columns_to_int,
                inputs="cleaned_zones2",
                outputs="zones_procesado",
                name="convert_columns_to_int_zones"
            ),
            node(
                func=process_wowah_data,
                inputs="cleaned_wowah_data",
                outputs="processed_wowah_data",
                name="process_wowah_data_node"
            ),
        ]
    )

