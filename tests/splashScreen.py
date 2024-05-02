import os

from appium.webdriver.common.appiumby import AppiumBy

import config

driver = config.main()

# Seus testes aqui
# Exemplo: 
element = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button')
element.click()

# Fechar a sessão do driver
driver.quit()