import os
import json

from .web_driver import get_web_driver, set_web_driver
from .screenshot import get_b64_screenshot
from openai import OpenAI
from dotenv import load_dotenv





def analyze_content(question):
    try:
        """
        This tool analyzes the current webpage screenshot and answers the user's question based on the information on the page.
        param: question: Question to answer based on the information on the current webpage screenshot.
        """
        load_dotenv()

        wd = get_web_driver()

        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        screenshot = get_b64_screenshot(wd)

        # save screenshot locally
        # with open("screenshot.png", "wb") as fh:
        #     fh.write(base64.b64decode(screenshot))

        messages = [
            {
                "role": "system",
                "content": "You are a teacher assitant checking work. Your primary task is to accurately answer questions in response to user queries based on webpage screenshots. When a user asks a question, analyze the provided screenshot of the webpage for relevant information and answer. Your goal is to answer the question correctly.",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{screenshot}",
                    },
                    {
                        "type": "text",
                        "text": f"{question}",
                    }
                ]
            }

        ]

        response = client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=messages,
            max_tokens=1024,
        )

        message = response.choices[0].message
        message_text = message.content

        set_web_driver(wd)

        return json.dumps({"data": message_text})
    except Exception as e:
        return json.dumps({"error": str(e)})