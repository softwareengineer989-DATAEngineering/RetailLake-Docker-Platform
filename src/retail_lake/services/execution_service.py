from retail_lake.factory.pipeline_factory import PipelineFactory
from retail_lake.context import PlatformContext

class PlatformExecutionService:

    @staticmethod
    def before_execution(pipeline_name: str):

        print(f"[Platform] Preparing pipeline: {pipeline_name}")

    @staticmethod
    def after_execution(pipeline_name: str):

        print(f"[Platform] Finished pipeline: {pipeline_name}")

    @staticmethod
    def execute(pipeline_name: str):

        PlatformExecutionService.before_execution(
            pipeline_name
        )

        context = PlatformContext(
            pipeline_name
        )

        pipeline = PipelineFactory.create(
            context.pipeline_name,
            context
        )

        pipeline.start()

        pipeline.run()

        pipeline.finish()

        PlatformExecutionService.after_execution(
            pipeline_name
        )