import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def main():

    #driver = webdriver.Chrome('---location of chromedriver---').
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.new-innov.com/login/sso/whc")
    time.sleep(2)

    uname = "net-id".  #***
    pword = "net-id-password"   #***

    unameArea = driver.find_element("id", "username")
    unameArea.send_keys(uname)

    pwdArea = driver.find_element("id", "password")
    pwdArea.send_keys(pword)
    time.sleep(1)

    action = ActionChains(driver)
    login = driver.find_element("name", "_eventId_proceed")
    action.move_to_element(login).perform()
    login.click()
    time.sleep(20)

    '''
    action = ActionChains(driver)

    driver.switch_to.frame(driver.find_element("id","duo_iframe"))
    enterPass = driver.find_element("id","passcode")
    action = ActionChains(driver)
    action.move_to_element(enterPass).perform()
    enterPass.click()
    time.sleep(2)

    typePass = driver.find_element("name","passcode")
    typePass.send_keys("last-9-digits") #***

    loginDuo = driver.find_element("id","passcode")
    action.move_to_element(loginDuo).perform()
    loginDuo.click()
    time.sleep(10)
    '''

    driver.get("https://www.new-innov.com/EvaluationForms/EvaluationFormsHost.aspx?Control=CompleteEvals")
    time.sleep(7)

    evals = driver.find_elements(By.CLASS_NAME, "sessionColumn")

    action = ActionChains(driver)

    for i in range(0, len(evals)):

        item = driver.find_elements(By.CLASS_NAME, "sessionColumn")[0]
        action.move_to_element(item).perform()
        item.click()
        time.sleep(7)

        #agrees = driver.find_elements(By.XPATH, "//input[@data-id = '61795'")
        agrees = driver.find_elements(By.CLASS_NAME, "ni-radio")

        counter = 0

        name = agrees[0].get_attribute("name")

        time.sleep(2)
        for question in agrees:

            if(counter == 0):
                name = question.get_attribute("name")
                print(name)

            counter += 1
            click = False

            if(question.get_attribute("name") == name):
                if((counter%5) == 4):
                    action = ActionChains(driver)
                    driver.execute_script("arguments[0].scrollIntoView();", question)
                    time.sleep(1)
                    action.move_to_element(question).perform()
                    try:
                        question.click()
                    except:
                        time.sleep(0.1)
                    time.sleep(0.5)
                if((counter%5)==0):
                    counter = 0
            else:
                counter = 1

            time.sleep(0.2)

        time.sleep(1)

        html = driver.find_element(By.TAG_NAME, "html")
        html.send_keys(Keys.END)

        try:
            submit = driver.find_element(By.XPATH,'/html/body/form/div[4]/div[2]/div/div[1]/div/div/div[3]/div/div[2]/div[1]/div/button')
            driver.execute_script("arguments[0].scrollIntoView();", submit)
            time.sleep(1)
            submit.click()
        except Exception as e:
            print("err", e)

        try:
            #submit = driver.find_element(By.CLASS_NAME,"btn ni-button btn-primary")
            submit = driver.find_element("xpath", "//div[@class = 'right']//button").click()
            driver.execute_script("arguments[0].scrollIntoView();", submit)
            time.sleep(1)
            submit.click()
        except Exception as e:
            print("err", e)

        # action = ActionChains(driver)
        # action.move_to_element(submit).perform()
        time.sleep(20)
        # submit.click()

    driver.quit()

if __name__ == "__main__":
    main()
