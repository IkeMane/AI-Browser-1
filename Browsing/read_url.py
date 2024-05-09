import json
import os
import time
from urllib.parse import urlparse

from pydantic import Field
from selenium.common import WebDriverException


from .web_driver import get_web_driver, set_web_driver
from .analyze_content import analyze_content






def visit_url(url):
    """
    This tool reads a single URL and opens it in your current browser window. For each new source, go to a direct URL that you think might contain the answer to the user's question or perform a google search like 'https://google.com/search?q=search' if applicable. Otherwise, don't try to guess the direct url, use ClickElement tool to click on the link that you think might contain the desired information on the current web page. Remember, this tool only supports opening 1 URL at a time. Previous URL will be closed when you open a new one.
    param: url: URL to open
    """
    wd = get_web_driver()

    wd.get(url)

    time.sleep(2)

    # remove all popups
    js_script = """
    var popUpSelectors = ['modal', 'popup', 'overlay', 'dialog']; // Add more selectors that are commonly used for pop-ups
    popUpSelectors.forEach(function(selector) {
        var elements = document.querySelectorAll(selector);
        elements.forEach(function(element) {
            // You can choose to hide or remove; here we're removing the element
            element.parentNode.removeChild(element);
        });
    });
    """

    wd.execute_script(js_script)

    set_web_driver(wd)
    # page_content = analyze_content("What am I looking at?")
    return json.dumps({"data": f"Opened {url} in browser."})
