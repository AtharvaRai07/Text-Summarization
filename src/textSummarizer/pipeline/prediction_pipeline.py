from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": self.config.length_penalty,
                      "num_beams": self.config.num_beams,
                      "max_length": self.config.max_length}

        pipe = pipeline("summarization",model=self.config.model_path,tokenizer=tokenizer)

        print("Dialogue: \n")
        print(text)

        output = pipe(text, **gen_kwargs)[0]['summary_text']
        print("\n\nSummary: \n")
        print(output)

        return output

