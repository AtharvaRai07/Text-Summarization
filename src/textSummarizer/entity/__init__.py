from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str


@dataclass
class ModelTraineConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: str  
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
