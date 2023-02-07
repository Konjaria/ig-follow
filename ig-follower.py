"""
Author: Saba Konjaria
Created at: 06-Feb-2023
"""
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# significant libraries


# constants
main_endpoint = "https://www.instagram.com/"
username = "your-facebook-username"
password = "your-facebook-password"


# class definition
class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):

        self.driver.get(url="https://www.instagram.com/accounts/login/")
        time.sleep(3)
        # log in with Facebook
        self.driver.find_element(By.XPATH, "//*[@id=\"loginForm\"]/div/div[5]/button/span[2]").click()
        # delay a bit in order to letSelenium to find appropriate things out
        time.sleep(5)
        # after a while put in the values like username or password
        username_field = self.driver.find_element(By.ID, "email")
        username_field.send_keys(username)

        password_field = self.driver.find_element(By.ID, "pass")
        password_field.send_keys(password)

        # Hit Enter
        password_field.send_keys(Keys.ENTER)

        # for now, we are already into our account
        time.sleep(5)
        print("Successfully Logged in ✅")


    def find_followers(self):
        # # Approach 1:  Go to the follower's page  from the initial account's page which is so complicated
        # time.sleep(15)
        #
        # # first look through the ig account  to deal with
        # self.driver.get(url="https://www.instagram.com/cristiano")
        #
        #
        # # tap follower's button
        # time.sleep(5)
        # followers_button = self.driver.find_element(By.XPATH, "//*[@id=\"mount_0_0_FY\"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a")
        # followers_button.click()

        # Approach 2: On the way to the follower's page directly
        time.sleep(10)
        self.driver.get(url="https://www.instagram.com/cristiano/followers/")


    def follow(self):
        time.sleep(10)
        list_of_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button')
        for item in list_of_buttons:
            try:
                if item.text == "Follow":
                    item.click()
                    time.sleep(5)
                    print("Followed ")
    
            except ElementClickInterceptedException as e:
                print("Exception handled {}".format(e))
                continue




# driver method
def main():
    my_account = InstaFollower()
    my_account.login()
    my_account.find_followers()
    my_account.follow()


# calling the main method
if __name__ == "__main__":
    main()
