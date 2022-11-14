import pandas as pd

from app.db import create_record_flat
from app.schemas import Flat
from app.utils.ml.ml import run_preditcion_on_model

from .ml import normal_int


def read_df(df: pd.DataFrame, db) -> pd.DataFrame:
    predictions = list()

    for _, row in df.iterrows():
        prediction = run_preditcion_on_model(
            row['district'],
            row['metro_name'],
            row['metro_time'],
            row['metro_get_type'],
            row['size'],
            row['kitchen'],
            row['floor'],
            row['floors'],
            row['constructed'],
            row['fix'],
            row['type_of_building'],
            row['type_of_walls'],
        )
        predictions.append(normal_int(prediction[0]))

        dict_for_pydantic_model_flat = {
            'district': row['district'],
            'metro_name': row['metro_name'],
            'metro_time': row['metro_time'],
            'metro_get_type': row['metro_get_type'],
            'size': row['size'],
            'kitchen': row['kitchen'],
            'floor': row['floor'],
            'floors': row['floors'],
            'constructed': row['constructed'],
            'fix': row['fix'],
            'type_of_building': row['type_of_building'],
            'type_of_walls': row['type_of_walls'],
            'price': prediction
            * 1000000,  # multiplying by 1 000 000 to get price in millions
        }

        try:
            flat = Flat(**dict_for_pydantic_model_flat)
            create_record_flat(db, flat)
        except Exception as ex:
            print(ex, "POSTGRES OFF HIGH PROBABILITY")

    df['prediction'] = predictions

    return df
