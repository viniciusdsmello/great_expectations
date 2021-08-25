import warnings

from great_expectations.execution_engine import (
    PandasExecutionEngine,
    SparkDFExecutionEngine,
)
from great_expectations.execution_engine.sqlalchemy_execution_engine import (
    SqlAlchemyExecutionEngine,
)
from great_expectations.expectations.metrics.column_aggregate_metric_provider import (
    ColumnAggregateMetricProvider,
    column_aggregate_partial,
    column_aggregate_value,
)
from great_expectations.expectations.metrics.import_manager import F, sa


class ColumnMax(ColumnAggregateMetricProvider):
    metric_name = "column.max"

    @column_aggregate_value(engine=PandasExecutionEngine)
    def _pandas(cls, column, parse_strings_as_datetimes=None, **kwargs):
        if parse_strings_as_datetimes:
            warnings.warn(
                """The parameter "parse_strings_as_datetimes" is no longer supported and \
                will be deprecated in a future release. Please update code accordingly.
                """,
                DeprecationWarning,
            )

        return column.max()

    @column_aggregate_partial(engine=SqlAlchemyExecutionEngine)
    def _sqlalchemy(cls, column, parse_strings_as_datetimes=None, **kwargs):
        if parse_strings_as_datetimes:
            warnings.warn(
                """The parameter "parse_strings_as_datetimes" is no longer supported and \
                will be deprecated in a future release. Please update code accordingly.
                """,
                DeprecationWarning,
            )

        return sa.func.max(column)

    @column_aggregate_partial(engine=SparkDFExecutionEngine)
    def _spark(cls, column, parse_strings_as_datetimes=None, **kwargs):
        if parse_strings_as_datetimes:
            warnings.warn(
                """The parameter "parse_strings_as_datetimes" is no longer supported and \
                will be deprecated in a future release. Please update code accordingly.
                """,
                DeprecationWarning,
            )

        return F.max(column)
