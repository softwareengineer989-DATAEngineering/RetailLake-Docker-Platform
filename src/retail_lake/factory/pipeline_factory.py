from retail_lake.registry.pipeline_registry import get_pipeline


class PipelineFactory:

    @staticmethod
    def create(name, context):

        pipeline_class = get_pipeline(name)

        # if pipeline_class is None:
        #     raise ValueError(
        #         f"Pipeline '{name}' is not registered."
        #     )

        return pipeline_class(context)

