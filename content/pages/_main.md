Title: Pywinauto
Slug: pywinauto-GUI-automation-tool
Summary: Windows GUI Automation with Python
URL:
Save_as: index.html

**pywinauto** is a GUI automation library written in pure Python and well developed for Windows GUI.
At its simplest it allows you to send mouse and keyboard actions to dialogs and controls on both Windows and Linux,
while more complex text-based actions are supported on Windows only so far (Linux AT-SPI support is under development).

## [](#advantages)Advantages
* Text based GUI automation is the most reliable/portable way being resistant to changes in UI layout, screen resolution, theme, fonts etc.
* Flexible timings are automatically on (see [Waiting for Long Operations](https://pywinauto.readthedocs.io/en/latest/wait_long_operations.html) for more details).
* Multiple backends architecture.
* MS UI Automation API support is native (using COM library) and free from .NET layer bugs.
* Tend to be cross-platform in the mid-term. Linux support is coming at the H2 of 2018, macOS is currently targeted to 2019-2020.

## [](#example)Example
It is simple and the resulting scripts are very readable. How simple?

    #!python
    from pywinauto.application import Application
    # Run a target application
    app = Application().start("notepad.exe")
    # Select a menu item
    app.UntitledNotepad.menu_select("Help->About Notepad")
    # Click on a button
    app.AboutNotepad.OK.click()
    # Type a text string
    app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)



### [](#setup)Setup

*   Just run `pip install --upgrade pywinauto` (Py2.7+, Py3.3+)

or follow manual steps (if pip installation is not available due to your network restrictions):

* Install [pyWin32 extensions](http://sourceforge.net/projects/pywin32/files/pywin32/) (no need for ActivePython)
* Download [six](https://pypi.python.org/pypi/six) and install by `python setup.py install`
* Download [comtypes](https://github.com/enthought/comtypes/releases) and install by `python setup.py install`
* Download [the latest pywinauto](https://github.com/pywinauto/pywinauto/zipball/master/) and run `python setup.py install`

or install on Linux:

* [six](https://pypi.python.org/pypi/six)
* [python-xlib](https://github.com/python-xlib/python-xlib/releases)
* Run `python setup.py install` for every dependency and for pywinauto package

### [](#supported-controls)Supported controls

* Standard Win32 controls (through Win32 API): MFC, WTL, VB6 and some other legacy apps, partial support for WinForms
* All standard widgets under MS UI Automation: WinForms, WPF, Qt, all browsers, explorer.exe and more (pywinauto 0.6.0+)
* Chrome browser (all OSes) should enable accessibility on the web pages by running `chrome --force-renderer-accessibility`.


---  
### [](#demo)Demo

Here is a short screencast with Pywinauto in action:

![Notepad.exe automation example](images/notepad-simple2-ir.gif)


### A brand new team logo.
![logo](images/walter_cat.jpg) This is the new [team](https://github.com/pywinauto) icon. Thanks, [_Anna_](https://www.behance.net/anna9111990), who created the icon for the team, cat Walter.
PS: Logo for the pywinauto library [is still wanted](https://github.com/pywinauto/pywinauto/issues/76).
