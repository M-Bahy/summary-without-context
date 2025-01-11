from atproto import Client, client_utils
from dotenv import load_dotenv
from bidi.algorithm import get_display
import arabic_reshaper
import os

load_dotenv()

USERNAME = os.getenv("BLUESKY_USERNAME")
PASSWORD = os.getenv("BLUESKY_PASSWORD")


def main():
    client = Client()
    profile = client.login(USERNAME, PASSWORD)
    name = profile.display_name
    # Handle Arabic names
    if not name.isascii():
        reshaped_text = arabic_reshaper.reshape(name)
        name = get_display(reshaped_text)
    print(f"Hello {name} from Python SDK")

    # text = client_utils.TextBuilder().text('Hello World from ')
    # text = text.link('Python SDK', 'https://atproto.blue')
    # post = client.send_post(text)
    # client.like(post.uri, post.cid)

def in_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True  # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False  # Probably standard Python interpreter

if __name__ == "__main__":
    # main()
    print(in_notebook())
