from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from os import getenv, path

load_dotenv()


def main():
    capabilities = dict(
        platformName=getenv('PLATFORM_NAME'),
        automationName=getenv('AUTOMATION_NAME'),
        deviceName=getenv('DEVICE'),
        app=path.join(path.dirname(__file__), 'artifact', getenv('LOCALE_APP'))
    )

    # URL do servidor Appium
    appium_server_url = getenv('APPIUM_SERVER')
    # Inicializar o driver do Appium
    driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))
    return driver
