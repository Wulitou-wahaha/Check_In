from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def check_in_south_plus():
    try:
        driver = get_web_driver()
        driver.get("https://www.south-plus.net/plugin.php?H_name-tasks.html")
        driver.find_element_by_xpath("//input[@name='pwuser']").send_keys(username)
        driver.find_element_by_xpath("//input[@name='pwpwd']").send_keys(password)
        driver.find_element_by_xpath("id("main")//input[@name="gdcode"]").click()
        propertery=WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.ID, "id("ckcode")")))
        valid = Ocr_Captcha(driver, propertery, img_path)
        driver.find_element_by_xpath("id("main")//input[@name="gdcode"]").send_keys(valid)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        try:
            driver.find_element_by_id("id("p_15")/a").click()
            print('签到成功')
        except:
            print('已签到')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    check_in_south_plus()
