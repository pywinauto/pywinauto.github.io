Title: Pywinauto
Slug: pywinauto-GUI-automation-tool
Summary: Windows GUI automation with python
URL:
Save_as: index.html

**pywinauto** is a GUI automation library written in pure Python and well developed for Windows GUI.
At its simplest it allows you to send mouse and keyboard actions to dialogs and controls on both Windows and Linux,
while more complex text-based actions are supported on Windows only so far (Linux AT-SPI support is under development).

### [Pywinauto 0.6.0](https://github.com/pywinauto/pywinauto/releases/tag/0.6.0) (Oct, 31) and [0.6.1](https://github.com/pywinauto/pywinauto/releases/tag/0.6.1) (Feb, 08)
- This big release introduces MS UI Automation (UIA) support (WinForms, WPF, Qt, browsers, Store apps and more).
- Documentation is built continuously now on [ReadTheDocs](https://pywinauto.readthedocs.io/en/latest/).
  See also our improved [Getting Started Guide](https://pywinauto.readthedocs.io/en/latest/getting_started.html)
- Modules [keyboard](https://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html) and [mouse](https://pywinauto.readthedocs.io/en/latest/code/pywinauto.mouse.html) can be used out of any window context now. And they work on Linux as well!
- Multi-backend architecture allows to add new platforms support. Just implement two classes and register your backend!
- Code style is much closer to PEP8: `ClickInput` -> `click_input`. Though `backend='win32'` is
  ~80% backward compatible with pywinauto 0.5.4.
- Initial implementation of the *win32_hooks* module. Keyboard events (a.k.a hotkeys) and mouse actions
  handlers can be registered in the system. Example: [hook_and_listen.py](https://github.com/pywinauto/pywinauto/blob/master/examples/hook_and_listen.py).


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


---  
### [](#demo)Demo

Here is a short screencast with Pywinauto in action:

![Notepad.exe automation example](images/notepad-simple2-ir.gif)


### A brand new team logo.
![logo](images/walter_cat.jpg) This is the new [team](https://github.com/pywinauto) icon. Thanks, [_Anna_](https://www.behance.net/anna9111990), who created the icon for the team, cat Walter.
PS: Logo for the pywinauto library [is still wanted](https://github.com/pywinauto/pywinauto/issues/76).
