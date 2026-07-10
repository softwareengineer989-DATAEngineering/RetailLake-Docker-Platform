import argparse

from retail_lake.factory.pipeline_factory import PipelineFactory

# Register all pipelines
import retail_lake.jobs.customer_pipeline


def main():

    parser = argparse.ArgumentParser(
        description="RetailLake Platform"
    )

    parser.add_argument(
        "pipeline",
        help="Pipeline name"
    )

    args = parser.parse_args()

    pipeline = PipelineFactory.create(args.pipeline)

    pipeline.start()

    pipeline.run()

    pipeline.finish()


if __name__ == "__main__":
    main()