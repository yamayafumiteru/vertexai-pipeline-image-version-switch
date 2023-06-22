import os
from dataclasses import dataclass


@dataclass
class PipelineConfig:
    pipeline_image_tag: str = os.environ.get("PIPELINE_IMAGE_TAG", "test")
