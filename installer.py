from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, SelectionList, Label, Button, Markdown, Select, Static, Switch

### JSON Exporter ###

def savejson(json):
    with open('options.json', 'w') as f:
        f.write(str(json).replace("'", '"').replace("True", "true").replace("False", "false"))

#####################

Head="""
# DesktopOnCodespaces Installer

> DesktopOnCodespaces Allow you to run grapical linux and windows apps in your codespace for free.

It Actually Have
* Windows App Support (using wine)
* Audio Support
* Root Access
* Support File Persistance
* Entierly in web browser
* Bypass School Network
* Fast VMs Using KVM (Windows and Linux)

"""
InstallHead="""
# DesktopOnCodespaces Installer
"""     

LINES = ["KDE Plasma (Heavy)", "XFCE4 (Lightweight)", "I3 (Very Lightweight)"]

class InstallScreen(Screen):
    CSS_PATH = "installer.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Markdown(InstallHead)
        yield Horizontal (
        Vertical (
         Label("Default Apps (you should keep them)"),
         SelectionList[int]( 
            ("Wine", 0, True),
            ("Brave", 1, True),
            ("Xarchiver", 2, True),
            id="defaultapps"
        ),),
        Vertical (
         Label("Programming"),
         SelectionList[int]( 
            ("OpenJDK 8 (jre)", 0),
            ("OpenJDK 17 (jre)", 1),
            ("VSCodium", 2),
            id="programming"
        ),),
        Vertical (
         Label("Apps"),
         SelectionList[int]( 
            ("VLC", 0),
            ("LibreOffice", 1),
            ("Synaptic", 2),
            ("AQemu (VMs)", 3),
            ("Discord", 4),
            id="apps"
        ),),
        )

        yield Vertical (
         Horizontal(
            Label("\nDesktop Environement :"),
            Select(id="de", value="KDE Plasma (Heavy)", options=((line, line) for line in LINES)),
        ),)
        yield Horizontal (
            Button.error("Back", id="back"),
            Button.warning("Install NOW", id="in"),
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            app.pop_screen()
        if event.button.id == "in":
            data = {"defaultapps": self.query_one("#defaultapps").selected, "programming": self.query_one("#programming").selected, "apps": self.query_one("#apps").selected, "enablekvm": True, "DE": self.query_one("#de").value}
            savejson(data)
            app.exit()

class InstallApp(App):
    CSS_PATH = "installer.tcss"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Markdown(Head)
        
        yield Vertical (
            Button.success("Install", id="install"),
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "cancel":
            print("")
        if event.button.id == "install":
            self.push_screen(InstallScreen())
            
if __name__ == "__main__":
    app = InstallApp()
    app.run()

