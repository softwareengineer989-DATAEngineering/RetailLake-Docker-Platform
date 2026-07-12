import argparse

from retail_lake.factory.pipeline_factory import PipelineFactory
from retail_lake.utils.logger import get_logger
from retail_lake.context.platform_context import PlatformContext
import retail_lake.registry.bootstrap

logger = get_logger("PlatformLauncher")


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "pipeline",
        help="Pipeline name"
    )

    args = parser.parse_args()

    logger.info("=" * 60)
    logger.info("RetailLake Platform Starting")
    logger.info("=" * 60)

    logger.info(f"Requested pipeline : {args.pipeline}")

    context = PlatformContext(args.pipeline)

    pipeline = PipelineFactory.create(
        args.pipeline,
        context
    )

    logger.info(f"Launching pipeline : {args.pipeline}")

    pipeline.start()

    pipeline.run()

    pipeline.finish()

    logger.info("=" * 60)
    logger.info("Platform Execution Finished")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()