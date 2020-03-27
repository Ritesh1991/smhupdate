from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
	o = OTAUpdater('https://github.com/Ritesh1991/smhupdate')
	o.download_and_install_update_if_available('Ritesh', '9824168814')


def start():
	import os
	while True:
		print("hello")
	# from main.x import YourProject
	# project = YourProject()
	# ...


def boot():
	download_and_install_update_if_available()
	start()

boot()

