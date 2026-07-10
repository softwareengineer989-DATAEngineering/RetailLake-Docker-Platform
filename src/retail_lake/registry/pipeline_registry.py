PIPELINE_REGISTRY = {}


def register_pipeline(name: str, pipeline):
    if name in PIPELINE_REGISTRY:
        raise ValueError(f"Pipeline '{name}' already registered")

    PIPELINE_REGISTRY[name] = pipeline


def get_pipeline(name: str):
    if name not in PIPELINE_REGISTRY:
        raise ValueError(f"Pipeline '{name}' not found")

    return PIPELINE_REGISTRY[name]


def list_pipelines():
    return sorted(PIPELINE_REGISTRY.keys())