from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def check_in_sijishe():
    try:
        driver = get_web_driver()
        driver.get("https://sijisheb.com/k_misign-sign.html")
        driver.find_element_by_xpath("//*[@class='btn J_chkitot']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@name='password']").send_keys(password)
        time.sleep(3)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(3)
        driver.get("https://sijisheb.com/k_misign-sign.html")
        if driver.find_element_by_xpath("//*[@class='btn J_chkitot']"):
        driver.find_element_by_xpath("//*[@class='btn J_chkitot']").click()
        print('司机社签到')
        if driver.find_element_by_xpath("//*[@class='btn btnvisted']"):
        print('今日已签到')  
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    check_in_sijishe()
