from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivy.base import EventLoop
from kivymd.toast import toast
from pytube import exceptions
from pytube import YouTube
import ssl
import threading
import urllib
import json
ssl._create_default_https_context = ssl._create_stdlib_context


with open('Settings.json','r') as f:
	data = json.load(f)


KV = """
ScreenManager:
	Main:
	Download:
	End:
	_Settings:
	
<Main>:
	name: 'main'
	
	MDIconButton:
		icon: 'power-settings'
		pos_hint: {'center_x': 0.9, 'center_y': 0.95}
		on_release: 
			app.set_back()
	
	MDLabel:
		text: 'Yodo'
		bold: False
		font_size: '50sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_x': 0.77, 'center_y': 0.83}
		
	MDLabel:
		text: 'Download youtube videos'
		bold: False
		font_size: '10sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_x': 0.77, 'center_y': 0.75}
		
	MDTextField:
		id: get_url
		text: ''
		hint_text: 'Enter URL'
		pos_hint: {'center_x': 0.5, 'center_y': 0.57}
		size_hint: (0.8,0.1)
        
    MDSpinner:
        id: mdspin
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .3}
        active: check.active
        opacity:1

    MDCheckbox:
        id: check
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': 0.7, 'center_y': 0.45}
        active: False
        opacity: 1
        
	MDFillRoundFlatIconButton:
		id: download_video
		icon: 'video-wireless'
		text: 'video'
		pos_hint: {'center_x': 0.3, 'center_y': 0.45}
		width: 200
		on_release: app.download_media_thread('video')
			
	MDFillRoundFlatIconButton:
		id: download_audio
		icon: 'cast-audio'
		text: 'audio'
		pos_hint: {'center_x': 0.7, 'center_y': 0.45}
		width: 200
		on_release: app.download_media_thread('audio')
		
<Download>:
	name: 'download'
	
	
	
	MDLabel:
		text: 'Yodo'
		bold: False
		font_size: '50sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_x': 0.77, 'center_y': 0.83}
		
	MDLabel:
		text: 'Download youtube videos'
		bold: False
		font_size: '10sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_x': 0.77, 'center_y': 0.75}
	
	MDGridLayout:
		cols: 1
		padding: 20
		spacing: 80
		size_hint_y: 0.2
		pos_hint: {'center_x': 0.55, 'center_y': 0.55}
		MDLabel:
			id: name
			markup: True
			text: 'Name: How to make an app with kivymd python' 
			font_size: '15sp'
			font_name: 'lemonda.ttf'
		MDLabel:
			id: by
			markup: True
			text: 'By: Riju The Programmer'
			font_size: '15sp'
			font_name: 'lemonda.ttf'
		MDLabel:
			id: size
			markup: True
			text: ''
			font_size: '15sp'
			font_name: 'lemonda.ttf'
		
    MDFillRoundFlatIconButton:
        id: download_button
        icon: 'download'
        text: "Download"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_release: app.download()
        
<End>:
	name: 'end'
	
	
	
	MDLabel:
		text: 'Yodo'
		bold: False
		font_size: '50sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_x': 0.77, 'center_y': 0.83}
		
	MDLabel:
		text: 'Download youtube videos'
		bold: False
		font_size: '10sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_x': 0.77, 'center_y': 0.75}
		
	MDLabel:
		id: _size
		markup: True
		text: ''
		font_size: '13sp'
		font_name: 'lemonda.ttf'
		pos_hint: {'center_y': 0.65}
		halign:'center'
	
	MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True
		
	MDGridLayout:
	    padding: "40dp"
	    spacing: "20dp"
	    pos_hint: {"center_x": .5, "center_y": .3}
	    cols: 1
	    size_hint_y: 0.2
	
		MDLabel:
			text: 'Downloading...'
			bold: False
			font_size: '13sp'
			font_name: 'lemonda.ttf'
			halign: 'center'
			
<_Settings>:
	name: 'settings'
	MDBoxLayout:
	    orientation: "vertical"
	    MDToolbar:
	        title: "Settings"
	    	left_action_items: [["arrow-left", lambda x: app.backbutton()]]
	    ScrollView:
	    	MDList:
				OneLineListItem:
					text: 'Dark Theme'
					on_release: 
						switch.active = not(switch.active)
						app.theme_changer()
					MDCheckbox:
        				id: switch
        				size_hint: None, None
        				size: dp(48), dp(48)
     				   pos_hint: {'center_x': 0.9, 'center_y': 0.5}
     				   active: True if app.theme_cls.theme_style == 'Dark' else False
						
				OneLineListItem:
					text: 'Default Directory'
					on_release:  app.show_confirmation_dialog()
				
			
<Content>:
    name: 'content'
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "60dp"

    MDTextField:
        id: dialog_text
        hint_text: "Select Directory"
        text: app.PATH



"""
class End(Screen):
	pass
class Download(Screen):
	pass
class Main(Screen):
	pass
class _Settings(Screen):
	pass

class Content(BoxLayout):
	pass
	
sm = ScreenManager()
sm.add_widget(Main(name= 'main'))
sm.add_widget(Download(name= 'download'))
sm.add_widget(End(name='end'))
sm.add_widget(_Settings(name='settings'))

def bytsToMb(byts):
	mb = (float(byts)/1024)/1024
	if mb >=float(1024):
		gb=float(mb/1024)
		gb = "{:.2f}".format(gb)
		return str(gb)+"gb"
	mb = "{:.2f}".format(mb)
	return str(mb)+"mb"


class YodoApp(MDApp):
	dialog = None
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.kv = Builder.load_string(KV)
		self.url = ''
		self.to_be_downloaded = ''
		self.theme_cls.theme_style = data['theme']
		self.PATH = data['directory']
        
	def build(self):
		screen = Screen()
		screen.add_widget(self.kv)
		return screen
	
	def on_start(self):
		from android.permissions import request_permissions, Permission
		request_permissions([Permission.READ_EXTERNAL_STORAGE, 		Permission.WRITE_EXTERNAL_STORAGE])

	
	def hook_keyboard(self, window, key, *largs):
		if key == 27:
			self.kv.get_screen('main').manager.current = 'main'
			self.kv.get_screen('main').manager.transition.direction = 'right'
			return True
	
	def dialog_close(self,*args):
		self.dialog.dismiss(force=True)
	
	def dialog_ok(self,*args):
		self.PATH=self.dialog.content_cls.ids.dialog_text.text
		if self.PATH[(len(self.PATH)-1):] != '/':
			self.PATH = self.PATH + '/'
		if self.PATH[:20] !=  '/storage/emulated/0/':
			self.PATH= '/storage/emulated/0/'+self.PATH
		data['directory']= self.PATH
		with open('Settings.json','w') as f:
			json.dump(data,f)
		self.dialog_close()
		
	def set_back(self):
		self.kv.get_screen('end').manager.current = 'settings'
		self.kv.get_screen('end').manager.transition.direction = 'left'
		EventLoop.window.bind(on_keyboard=self.hook_keyboard)
	
	def show_confirmation_dialog(self):
		if not self.dialog:
			self.dialog = MDDialog(
                title="Directory:",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= self.dialog_close
                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release= self.dialog_ok
                    ),
                ],
            )
		self.dialog.open()
	def backbutton(self):
		self.kv.get_screen('main').manager.current = 'main'
		self.kv.get_screen('main').manager.transition.direction = 'right'
	
	def theme_changer(self):
		if self.theme_cls.theme_style=='Light':
			self.theme_cls.theme_style = 'Dark'
			data['theme']= "Dark"
		else:
			self.theme_cls.theme_style = 'Light'
			data['theme']= "Light"
		with open('Settings.json','w') as f:
			json.dump(data,f)
	
	def get_size(self):
		if self.to_be_downloaded == 'audio':
				self.kv.get_screen('end').ids._size.text = '[color=#2196f4]size: [/color]'+ bytsToMb(int(self.yt.streams.get_by_itag(140).filesize))
		else:
				self.kv.get_screen('end').ids._size.text = '[color=#2196f4]size: [/color]'+ bytsToMb(int(self.yt.streams.get_by_itag(18).filesize))
	
	def download_i(self):
		threading.Thread(target=self.get_size).start()
		destination= self.PATH
		try:
			if self.to_be_downloaded == 'audio':
				srm = self.yt.streams.get_by_itag(140)
				out_file = srm.download(output_path=destination)
				base, ext = os.path.splitext(out_file) 
				new_file = base + '.mp3'
				os.rename(out_file, new_file)
			else:
				srm = self.yt.streams.get_by_itag(18)
				srm.download(output_path=destination)
			self.kv.get_screen('end').ids._size.text = ''
			toast(f'Completed\nDownloaded at {self.PATH}',gravity=80)
		except:
			toast('Connection Error',gravity= 80)
		finally:
			self.kv.get_screen('main').manager.current= 'main'
			self.kv.get_screen('main').manager.transition.direction= 'right'
			self.kv.get_screen('main').ids.get_url.text= ' '
		
	def download(self):
		self.kv.get_screen('end').manager.current = 'end'
		self.kv.get_screen('end').manager.transition.direction = 'left'
		EventLoop.window.bind(on_keyboard=self.hook_keyboard)
		t4 = threading.Thread(target=(self.download_i))
		t4.start()
		
	def get_name(self):
		self.kv.get_screen('main').ids.mdspin.opacity= 1
		self.kv.get_screen('main').ids.check.active = True
		self.url = self.kv.get_screen('main').ids.get_url.text
		
		toast('loading !', gravity= 80)
		try:
			self.yt= YouTube(self.url)
			try:
				self.kv.get_screen('download').ids.name.text = '[color=#2196f4]Name: [/color]'+self.yt.title[:44]+'...'
			except:
					self.kv.get_screen('download').ids.name.text= '[color=#2196f4]Name: [/color]'+self.yt.title
			self.kv.get_screen('download').ids.by.text = '[color=#2196f4]by: [/color]'+self.yt.author
			
			if self.to_be_downloaded == 'audio':
				self.kv.get_screen('download').ids.size.text = '[color=#2196f4]type: [/color]Audio | 128kbps | .mp3'
#				self.kv.get_screen('download').ids.size.text = '[color=#2196f4]size: [/color]'+ bytsToMb(int(self.yt.streams.get_by_itag(140).filesize))
			else:
				self.kv.get_screen('download').ids.size.text = '[color=#2196f4]type: [/color]Video | 360p | .mp4'
#				self.kv.get_screen('download').ids.size.text = '[color=#2196f4]size: [/color]'+ bytsToMb(int(self.yt.streams.get_by_itag(18).filesize))
			
			
			self.kv.get_screen('download').manager.current = 'download'
			self.kv.get_screen('download').manager.transition.direction = 'left'
			EventLoop.window.bind(on_keyboard=self.hook_keyboard)
		except urllib.error.URLError:
			toast('Connection Error',gravity=80)
			
		except exceptions.RegexMatchError:
			toast('Invalid URL',gravity= 80)
			
		
		self.kv.get_screen('main').ids.mdspin.opacity= 0
		
	def download_media_thread(self,media):
		self.t1 =threading.Thread(target=self.download_media,args = (media,))
		self.t1.start()
		return

	def download_media(self,media):
		if media == 'audio':
			self.to_be_downloaded = 'audio'
		else:
			self.to_be_downloaded = 'video'
		self.get_name()
		

YodoApp().run()