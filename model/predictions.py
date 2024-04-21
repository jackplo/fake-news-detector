from transformers import BertTokenizerFast, BertForSequenceClassification


class Prediction:
    tokenizer = BertTokenizerFast.from_pretrained("model/fake-news-bert-base-uncased")
    model = BertForSequenceClassification.from_pretrained("model/fake-news-bert-base-uncased", local_files_only=True)
    max_length = 512

    @classmethod
    def get_prediction(self, text, convert_to_label=False):
        inputs = self.tokenizer(text, padding=True, truncation=True, max_length=self.max_length, return_tensors="pt").to('cpu')
        outputs = self.model(**inputs)

        probs = outputs[0].softmax(1)

        d = {
            0: "reliable",
            1: "fake"
        }

        if convert_to_label:
            return d[int(probs.argmax())]
        else:
            return int(probs.argmax())
