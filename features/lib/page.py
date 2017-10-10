#klasa glowna
from selenium.webdriver.common.action_chains import ActionChains

class Page():
	
	def __init__(self,driver,URL='http://automationpractice.com/index.php'):
		self.driver=driver
		self.URL=URL
	
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
		
	def find_element(self,loc):
		return self.driver.find_element(loc)
	
	def hover(self,loc):
		ActionChains(self.driver).move_to_element(loc).perform()
	
	def click(self,loc):
		self.driver.click(loc)
	
		