# ========================================================================
# Copyright 2025 REALITY Ministry
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================

__author__ = 'Jinho D. Choi'

import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletion

load_dotenv()


def single_interaction(client: OpenAI) -> ChatCompletion:
    return client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "user", "content": "Who are you?"}
        ]
    )


def multi_turn_interactions_0(client: OpenAI) -> ChatCompletion:
    return client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are a calculator."},
            {"role": "user", "content": "What is (2 + 3) * 4?"}
        ]
    )

def multi_turn_interactions_1(client: OpenAI) -> ChatCompletion:
    return client.chat.completions.create(
        model="gpt-5-nano",
        messages=[
            {"role": "system", "content": "You are a calculator."},
            {"role": "user", "content": "What is (2 + 3) * 4?"},
            {"role": "assistant", "content": "20"},
            {"role": "user", "content": "Can you show me the full derivation?"}
        ]
    )

if __name__ == "__main__":
    c = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # r = single_interaction(c)
    # print(r.choices[0].message.content)

    # r = multi_turn_interactions_0(c)
    # print(r.choices[0].message.content)

    r = multi_turn_interactions_1(c)
    print(r.choices[0].message.content)
