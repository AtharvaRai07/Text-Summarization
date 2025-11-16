import os
from src.textSummarizer.logger import logging
from transformers import AutoTokenizer
from datasets import load_from_disk
from src.textSummarizer.entity import DataTransformationConfig
from src.textSummarizer.logger import logging


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        logging.info("Converting examples to features...")
        input_embeddings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation = True)

        logging.info("Converting summaries to features...")
        with self.tokenizer.as_target_tokenizer():
            target_embeddings = self.tokenizer(example_batch['summary'], max_length=128, truncation = True)

        return {'input_ids': input_embeddings['input_ids'],
                'attention_mask': input_embeddings['attention_mask'],
                'labels': target_embeddings['input_ids']}

    def convert(self):
        logging.info("Loading dataset from disk...")
        dataset_samsum = load_from_disk(self.config.data_path)

        logging.info("Transforming dataset...")
        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)

        logging.info("Saving transformed dataset to disk...")
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset'))
