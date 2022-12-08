from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

def check_in_javbus():
    try:
        driver = get_web_driver()
        driver.get("https://www.javbus.com/forum/member.php?mod=logging&action=login")
        driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        propertery=WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='vm' and @width='100']")))
        valid = Ocr_Captcha(driver, propertery, img_path)
        driver.find_element_by_xpath("//input[@name='seccodeverify']").send_keys(valid)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        driver.get("https://www.javbus.com/forum/home.php?mod=spacecp&ac=credit")
        try:
        driver.find_element_by_xpath("//[@id="ct"]/div[1]/div/ul[2]/li[1]/text()")
        print('登录成功')
        except:
        print('登陆失败')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    check_in_javbus()
