import datetime
import rumps
from brew import BrewManager
from scraper import Scraper

class App(rumps.App):

    def __init__(self):
        super(App, self).__init__("🍺") 
        self.menu.add(rumps.MenuItem(title='Version: 1.0'))
        self.menu.add(rumps.MenuItem(title='Updated:'))
        self.menu.add(rumps.MenuItem(title='Install Program'))
        self.menu.add(rumps.MenuItem(title='Update All'))
        self.menu.add(rumps.separator)
        self.menu.add(rumps.MenuItem(title='Info'))
        self.bm = BrewManager()
        self.scraper = Scraper()
        self.get_last_refresh()
        # rumps.debug_mode(True)

    def get_last_refresh(self):
        t = "test"
        with open("updated.txt", "r") as file:
            t = file.readline()
        self.menu['Updated:'].title = (
                f"Updated: "
                f"{t}"
            )

    def refresh_status(self):
            d = datetime.datetime.now().strftime('%m-%d %H:%M:%S')
            self.menu['Updated:'].title = (
                f"Updated: "
                f"{d}"
            )
            with open("updated.txt", "w+") as file:
                file.write(d)

    @rumps.clicked("Install Program")
    def area_setting(self, sender):
        """ clicked "Change Area button." """
        install_window = rumps.Window(
            message='What program do you want to install?',
            title='Install',
            default_text="",
            ok="Search",
            cancel=None,
            dimensions=(150, 20)
        )

        resp = install_window.run()
        if resp.clicked:
            arg = self.scraper.search(resp.text)
            self.scraper.close_driver()
            print(arg)
            self.bm.install_software(arg)

    @rumps.clicked("Update All")
    def update_all(self, sender):
        self.bm.update_software()
        self.refresh_status()
        rumps.alert("All brewbar installed software updated!")

    @rumps.clicked("Info")
    def show_area(self, _):
        rumps.alert("A smal statusbar application for installing all kinds of software faster")
