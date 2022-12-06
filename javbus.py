from util import *

username = sys.argv[1] # 登录账号
password = sys.argv[2] # 登录密码
img_path = os.getcwd() + "/1.png"

@retry(stop_max_attempt_number=5)
def check_in_javbus():
    try:
        driver = get_web_driver()
        driver.get("https://www.javbus.com/forum/member.php?mod=logging&action=login")
        driver.find_element_by_xpath("//*[@name='username']").send_keys(username)
        driver.find_element_by_xpath("//*[@name='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@type='submit']").click()
        print('javbus签到成功')
    except:
        raise
    finally:
        driver.quit()

if __name__ == '__main__':
    check_in_javbus()
