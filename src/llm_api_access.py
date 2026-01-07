# ========================================================================
# Copyright 2025 Emory University
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

# Load environment variables from .env file
load_dotenv()


def test_llm_api() -> ChatCompletion:
    # Initialize the OpenAI client
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    # Create a simple chat completion
    response = client.chat.completions.create(
        model="gpt-5-nano",  # Using the fastest, cheapest model
        messages=[
            {"role": "user", "content": "Say 'Hello World'."}
        ]
    )

    return response


if __name__ == "__main__":
    r = test_llm_api()
    print(r.choices[0].message.content)
    print(r)
