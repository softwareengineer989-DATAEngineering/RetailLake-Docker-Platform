import argparse

from retail_lake.services.execution_service import PlatformExecutionService

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

    PlatformExecutionService.execute(
        args.pipeline
    )


if __name__ == "__main__":
    main()