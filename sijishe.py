from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def check_in_sijishe():
    try:
        driver = get_web_driver()
        driver.get("https://sijisheb.com/k_misign-sign.html")
        driver.find_element_by_id("JD_sign").click()
        time.sleep(3)
        driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        time.sleep(3)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        driver.get("https://sijisheb.com/k_misign-sign.html")
        driver.find_element_by_id("JD_sign").click()
        print('司机社签到')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    check_in_sijishe()
