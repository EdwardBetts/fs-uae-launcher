import fsboot
import fsui
from launcher.option import Option
from launcher.res import gettext
from launcher.launcher_settings import LauncherSettings
from launcher.ui.settings.settings_page import SettingsPage


class LauncherSettingsPage(SettingsPage):

    def __init__(self, parent):
        super().__init__(parent)
        icon = fsui.Icon("settings", "pkg:workspace")
        self.add_header(icon, "FS-UAE Launcher")

        if fsboot.get("fws") == "1":
            # We omit the appearance settings, since they have no effect
            # when running under the workspace environment.
            pass
        else:
            self.add_option("launcher_theme")
            self.add_option("launcher_font_size")

        self.add_section(gettext("Experimental Features"))
        # self.add_option(Option.NETPLAY_FEATURE)
        self.add_option(Option.LAUNCHER_CONFIG_FEATURE)
