Title: Pywinauto
Slug: pywinauto-GUI-automation-tool
Summary: Windows GUI automation with python
URL:
Save_as: index.html

**pywinauto** is a set of python modules to automate the Microsoft Windows GUI. At its simplest it allows you to send mouse and keyboard actions to windows dialogs and controls, but it also supports more complex actions.

### [pywinauto 0.6.0 is in the master branch](https://github.com/pywinauto/pywinauto/releases/tag/0.6.0) (October, 30, 2016)  
- This big release introduces MS UI Automation (UIA) support.
- Documentation is built continuously now on [ReadTheDocs](https://pywinauto.readthedocs.io/en/latest/).
  See also our improved [Getting Started Guide](https://pywinauto.readthedocs.io/en/latest/getting_started.html)
- Modules `keyboard` and `mouse` can be used out of any window context now. And they work on Linux as well!
- Multi-backend architecture allows to add new platforms support. Just implement two classes and register your backend!
- Code style is much closer to PEP8: `ClickInput` -> `click_input`. Though `backend='win32'` is
  ~80% backward compatible with pywinauto 0.5.4.
- Initial implementation of the *win32_hooks* module. Keyboard and mouse event
  handlers can be registered in the system.


### A brand new team logo.
![logo](images/walter_cat.jpg) This is the new [team](https://github.com/pywinauto) icon. Thanks, [_Anna_](https://www.behance.net/anna9111990), who created the icon for the team, cat Walter.  
PS: Logo for the pywinauto library [is still wanted](https://github.com/pywinauto/pywinauto/issues/76).


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

*   Just run `pip install pywinauto` (Py2.7+, Py3.3+)

or

*   Install [pyWin32 extensions](http://sourceforge.net/projects/pywin32/files/pywin32/) (no need for Active Python except 3.4 64-bit)
*   Download [the latest version](https://github.com/pywinauto/pywinauto/zipball/master/)
*   Just unpack and run `python setup.py install`

### [](#supported-controls)Supported controls

*   Native Windows controls (full support through Win32 API)
*   .NET Windows Forms (full support through MS UI Automation starting with pywinauto 0.6.0)


---  
### [](#demo)Demo

Here is a short screencast with Pywinauto in action:

![Notepad.exe automation example](images/notepad-simple2-ir.gif)
