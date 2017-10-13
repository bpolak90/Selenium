#klasa glowna
from selenium.webdriver.common.action_chains import ActionChains

class Page():
	
	def __init__(self,driver,URL='http://automationpractice.com/index.php'):
		self.driver=driver
		self.URL=URL
		self.driver.maximize_window()
	
	def get_url(self):
		return self.driver.getCurrentURL()
	
	def get_title(self):
		return self.driver.getTitle()
	
	def open_URL(self):
		self.driver.get(self.URL)
	
	#zamyka wszystko i wylacza webdrivera
	def quit(self):
		self.driver.quit()
	
	#zamyka biezace okno i jak jest jedyne to wylacza webdrivera
	def close(self):
		self.driver.close()
		
	def find_element(self,*loc):
		return self.driver.find_element(*loc)
	
	def hover(self,loc):
		ActionChains(self.driver).move_to_element(loc).perform()
	
	def click(self,loc):
		loc.click()

def rgba2hex(rgba):
	temp=rgba[5:-1]
	temp=eval(temp)
	RGB='#{0:02x}{1:02x}{2:02x}'.format(temp[0], temp[1], temp[2])
	return RGB

def assertion(el1, el2, msg):
	try:
		assert el1 in el2
	except AssertionError:
		print(msg)
	except TypeError:
		print('Zly typ argumentu')
	
if __name__=='__main__':
	rgba2hex('rgba(0, 33, 12, 1)')
		