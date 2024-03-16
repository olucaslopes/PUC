import os

from phrase_parser.layers.abstract_layer import Layer
from openai import OpenAI


class GptFallbackLayer(Layer):
    def __init__(self, parser):
        super().__init__(parser)
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        self.assistant = self.client.beta.assistants.retrieve("asst_jGm6qRc9qB8pjKT57qjiNzO4")
        self.thread = self.client.beta.threads.create()

    def apply_rule(self):
        message = self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=self.sentence
        )

        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id
        )

        run = self.client.beta.threads.runs.retrieve(
            thread_id=self.thread.id,
            run_id=run.id
        )

        message = self.client.beta.threads.messages.retrieve(
            thread_id=self.thread.id,
            message_id=message.id
        )

        return message

