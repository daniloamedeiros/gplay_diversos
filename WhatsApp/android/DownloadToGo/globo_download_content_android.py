
from time import sleep
import os
import mysql.connector
import socket
import time
import unittest
import logging
import datetime
import sys
import random
from random import seed
from random import randint
from appium import webdriver


class Globo_Download_Content_Test(unittest.TestCase):
	
	def setUp(self):
		self.reference= str(int(round(time.time() * 1000)))
		self.package = "com.globo.globotv"
		#device id as 1st argument
		self.udid = sys.argv[1]
		self.os = 'Android'
		#desired caps for the app
		desired_caps = {}
		desired_caps['platformName'] = self.os
		desired_caps['udid'] = self.udid
		desired_caps['deviceName'] = self.udid
		desired_caps['appPackage'] = self.package
		desired_caps['appActivity'] = "com.globo.globotv.splash.SplashActivity"
		desired_caps['noReset'] = True
		desired_caps['automationName'] = "uiautomator2"
		desired_caps['newCommandTimeout'] =600
		desired_caps['no-reset'] = True
		appium_input= sys.argv[2]
		if appium_input.isdigit():
			self.url= ('http://127.0.0.1:' + appium_input + '/wd/hub')
		else:
			self.url= appium_input
		#launching app
		self.driver = webdriver.Remote(self.url, desired_caps)
		self.start_app = int(round(time.time() * 1000))
		#initialising variables
		self.status = "Fail_launch"
		self.app_launch_time= 0
		self.status_dic = {}
		self.kpi_dic= {}
		self.app_launch_time= 0
		self.home_pg_load_time = 0
		self.video_load_time = 0
		self.download_time = 0 
		self.title_check = False
		self.test_name = "Globo_Download_Content"
		self.kpi_count = 5
		self.pass_count = 0
		self.fail_count = 0

		self.title_name = ""
	
	def tearDown(self):		
		#incrementing kpi count
		print ("Pass count is %s") %self.pass_count
		if self.pass_count!=self.kpi_count:
			self.fail_count = self.kpi_count - self.pass_count
		else:
			self.fail_count = 0
		print ("Fail count is %s ") %self.fail_count
		
		#Upload to database
		cnx = mysql.connector.connect(user="globo_user",password="Lm6qmDTv-Ft@", host="appiumdb.headspin.io",database="headspin_mobile_tests")
		city ="Sao Paulo"
		network=None
		host_name= socket.gethostname()
		cursor = cnx.cursor()
		
		cursor.execute('''INSERT INTO globo_kpi_metrics (globo_launch_time,globo_post_login_home_load_time,globo_video_load_time,globo_download_time,globo_title_check, machine, udid,status_of_run,city,reference,os_type,pass_count,fail_count,globo_test_name,network_type ) VALUES (%s,%s,%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s, %s)''', (self.app_launch_time,self.home_pg_load_time,self.video_load_time,self.download_time,self.title_check,str(host_name),str(self.udid),str(self.status),str(city),str(self.reference),str(self.os),str(self.pass_count),str(self.fail_count),str(self.test_name),str(network)))
		
		cnx.commit()
		cursor.close()
		cnx.close()
		
		self.driver.quit()
	
	def videoplay_check(self, sec):
		self.driver.implicitly_wait(5)
		t_end = time.time() + sec
		while time.time() < t_end:
			try:
				screen_size = self.driver.get_window_size()
				width = screen_size['width']
				height = screen_size['height']
				tap_x = width*0.5
				tap_y=height*0.23
				self.driver.tap([(tap_x,tap_y)])
				player_control = self.driver.find_element_by_id("com.globo.globotv:id/media_control")
				sleep(5)
			except:
				spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
				print ("Video Interrupted")
				self.video_play()		
	
	def video_play(self):
		self.driver.implicitly_wait(1)
		t_end = time.time() + 10
		while time.time() < t_end:
			try:
				spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
				print ("Spinner!!")
			except:
				break		
	
	def delete_download(self):
		self.driver.implicitly_wait(6)
		try:
			downloads_tab = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Downloads")')
			downloads_tab.click()

			sleep(5)
			edit_button = self.driver.find_element_by_id("com.globo.globotv:id/menu_downloads_item_edit")
			edit_button.click()

			check_box = self.driver.find_element_by_id("com.globo.globotv:id/view_holder_download_title_check_box_selected")
			check_box.click()
	
			conf_del = self.driver.find_element_by_id("com.globo.globotv:id/snackbar_action")
			conf_del.click()
		except:
			pass
	
	#Select a random novela and check if it's downloadable. Else, searches and selects another random Novela
	def search_random_novela(self):
		screen_size = self.driver.get_window_size()
		width = screen_size['width']
		height = screen_size['height']
		swipe_start_x = width/2
		swipe_start_y = height*0.6
		swipe_end_x = width/2
		swipe_end_y = height*0.2
		while True:
			sleep(4)
			categories = self.driver.find_element_by_android_uiautomator('new UiSelector().description("Categorias")')
			categories.click()
			
			novelas = self.driver.find_element_by_android_uiautomator('new UiSelector().text("Novelas")')
			novelas.click()
			sleep(3)

			random.seed(time.time())
			n=0
			#Random number of swipes on novela screen
			while n<random.randint(0,6):
				self.driver.swipe(swipe_start_x,swipe_start_y,swipe_end_x,swipe_end_y,1000)
				n+=1
			random.seed(time.time())
			#Picks random novela from those currently on screen
			title_button = self.driver.find_elements_by_id("com.globo.globotv:id/view_holder_custom_view_grid_custom_view_title")[random.randint(0,5)]
			title_button.click()
			
			sleep(2)

			self.title_name = self.driver.find_element_by_id("com.globo.globotv:id/title").text
			self.title_name = self.title_name.lower()

			print (self.title_name)
			thumb_button = self.driver.find_element_by_id("com.globo.globotv:id/thumb")
			sleep(2)
			thumb_button.click()
			#Check if download button exists for the selected novela, else continues while loop
			try:
				self.driver.find_element_by_id("com.globo.globotv:id/activity_video_custom_view_download")
				break
			except:
				continue

	def video_metrics_control(self):
		#Starting video and monitoring it's metrics
		self.status="Fail_video_Play"	
		video_start = int(round(time.time() * 1000))
		self.driver.implicitly_wait(1)
		t_end = time.time() +60
		while time.time() < t_end:
			try:
				spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
				print ("Spinner!!")
			except:
				print ("Not displayed")
				break
			
		self.driver.implicitly_wait(1)
		t_end = time.time() +60
		while time.time() < t_end:
			try:
				spinner = self.driver.find_element_by_id('com.globo.globotv:id/progress_bar')
				print ("Spinner!!")
			except:
				video_end = int(round(time.time() * 1000))
				print ("Not displayed")
				break
			
		self.video_load_time = video_end- video_start
		print ("Video load time ", self.video_load_time)
		self.pass_count +=1
		d = {'globo_video_load_time': self.video_load_time}
		self.kpi_dic.update(d)
			
		#Watch the Video for 1 minute	
		self.videoplay_check(30)
		self.driver.implicitly_wait(50)
	
	def test_login(self):
		self.driver.implicitly_wait(60)
		#Launching app
		agora_tab = self.driver.find_element_by_android_uiautomator('new UiSelector().description("Agora")')
		launched_app = int(round(time.time() * 1000))

		#calcualting launch time
		self.app_launch_time = launched_app - self.start_app
		print ("App Launch Time is %s ms" %self.app_launch_time)
		d = {'globo_launch_time': self.app_launch_time}
		self.kpi_dic.update(d)
		#incrementing pass count
		self.pass_count +=1

		self.delete_download()
		self.driver.implicitly_wait(60)

		home_tab = self.driver.find_element_by_id("com.globo.globotv:id/menu_bottom_navigation_view_item_home")
		home_tab.click()
		self.status="Fail_login"
		user_icon = self.driver.find_element_by_id("com.globo.globotv:id/menu_profile_custom_view_profile")
		user_icon.click()

		#Log out
		try:
			self.driver.implicitly_wait(5)
			logout =  self.driver.find_element_by_android_uiautomator('new UiSelector().text("Sair")')
			logout.click()
			#Confirm log out
			yes_btn = self.driver.find_element_by_id('android:id/button1')
			yes_btn.click()
			#Click on te account button
			self.driver.implicitly_wait(10)
			user_icon = self.driver.find_element_by_id("com.globo.globotv:id/menu_profile_custom_view_profile")
			user_icon.click()
		except:
			pass
		self.driver.implicitly_wait(60)
		entrar = self.driver.find_element_by_id('com.globo.globotv:id/activity_profile_text_view_get_int')
		entrar.click()
		self.driver.implicitly_wait(10)
		try:
			none_of_the_above = self.driver.find_element_by_id("com.google.android.gms:id/cancel")
			none_of_the_above.click()
		except:
			pass
		sleep(5)
		self.driver.implicitly_wait(60)
		email_id_tf = self.driver.find_element_by_class_name('android.widget.EditText')
		email_id_tf.set_value('laurent_headspin')
		#password
		password_tf = self.driver.find_elements_by_class_name('android.widget.EditText')[1]
		password_tf.set_value('Globo@321')

		sleep(5)
		buttons= self.driver.find_elements_by_class_name("android.widget.Button")
		for button in buttons:
			entrar = button.text
			if entrar =="ENTRAR":
				button.click()
				break

		self.status = "Fail_page_load_post_login"
		back_btn = self.driver.find_element_by_android_uiautomator('new UiSelector().description("Navigate up")')
		back_btn.click()
		home_page_load_start = int(round(time.time() * 1000))
		self.driver.implicitly_wait(0.5)
		t_end = time.time()+60
		while time.time() < t_end:
			try:
				self.driver.find_element_by_class_name('android.widget.ProgressBar')
			except:
				break

		self.driver.implicitly_wait(60)
		home_page = self.driver.find_element_by_id("com.globo.globotv:id/custom_view_premium_highlights_image_view_background")
		home_page_load_end = int(round(time.time() * 1000))
		self.home_pg_load_time = home_page_load_end- home_page_load_start
		d = {'globo_post_login_home_load_time': self.home_pg_load_time}
		self.kpi_dic.update(d)
		self.pass_count +=1
		print ("Home page loading time ", self.home_pg_load_time)
		while True:
			self.search_random_novela()
			self.video_metrics_control()
			#*********Download content**********#
			download_button = self.driver.find_element_by_id("com.globo.globotv:id/activity_video_custom_view_download")
			download_button.click()
			try:
				start_download = int(round(time.time() * 1000))
				download_progress = self.driver.find_element_by_id("com.globo.globotv:id/custom_view_download_status_status_progress_bar")
				break
			except:
				download_limit = self.driver.find_element_by_class_name("android.widget.Button")
				download_limit.click()
				navigate_up = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Navigate up")')
				navigate_up.click()
				navigate_up = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Navigate up")')
				navigate_up.click()
				continue
		sleep(2)
		navigate_up = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Navigate up")')
		navigate_up.click()

		navigate_up = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Navigate up")')
		navigate_up.click()

		downloads_tab = self.driver.find_element_by_android_uiautomator('new UiSelector().descriptionContains("Downloads")')
		downloads_tab.click()

		download_title_name = self.driver.find_element_by_id("com.globo.globotv:id/view_holder_download_text_view_title").text
		download_title_name = download_title_name.lower()
		print (download_title_name)
		if download_title_name == self.title_name:
			print ("Title Added to list")
			self.title_check = True
			self.pass_count = self.pass_count+1

		options_menu = self.driver.find_element_by_id("com.globo.globotv:id/view_holder_download_title_image_view_arrow")
		options_menu.click()

		sleep(4)
		self.driver.implicitly_wait(5)

		#Waits for download to finish
		self.status="Download_error"
		while True:
			try:
				self.driver.find_element_by_id("com.globo.globotv:id/custom_view_download_status_status_progress_bar")
				continue
			except:
				self.driver.find_element_by_id("com.globo.globotv:id/custom_view_download_status_image_view_icon")
				end_download = int(round(time.time() * 1000))
				self.download_time = end_download - start_download
				print ("Download time:  "), self.download_time
				self.pass_count = self.pass_count+1
				d = {'globo_launch_time': self.app_launch_time}
				self.kpi_dic.update(d)
				break

		self.driver.implicitly_wait(50)
		self.delete_download()
		sleep(5)

		if self.title_check ==False:
			self.status="Fail_title_check"
		else:
			self.status = "Pass"

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(Globo_Download_Content_Test)
	unittest.TextTestRunner(verbosity=2).run(suite)





