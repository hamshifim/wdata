from pyspark.sql.types import StructField, DoubleType, IntegerType, StringType, FloatType, BooleanType


def field_to_struct(header, floats=[], doubles=[], integers=[], booleans=[]):

    field_type = StringType()

    match header:
        case a if a in floats:
            field_type = FloatType()
        case a if a in integers:
            field_type = IntegerType()
        case a if a in doubles:
            field_type = DoubleType()
        case a if a in booleans:
            field_type = BooleanType()

    return StructField(header, field_type)
