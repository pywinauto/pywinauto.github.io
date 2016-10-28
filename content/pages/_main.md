Title: Pywinauto
Slug: pywinauto-GUI-automation-tool
Summary: Windows GUI automation with python
URL:
Save_as: index.html

**pywinauto** is a set of python modules to automate the Microsoft Windows GUI. At its simplest it allows you to send mouse and keyboard actions to windows dialogs and controls, but it also supports more complex actions.

#### [pywinauto 0.5.4 released](https://github.com/pywinauto/pywinauto/releases/tag/0.5.4) (October, 30, 2016)  

> Fix bugs and inconsistencies  
> Partial MFC Menu Bar support  
> Python 3.5 is supported
[Download pywinauto-0.5.4.zip](https://github.com/pywinauto/pywinauto/releases/download/0.5.4/pywinauto-0.5.4.zip)  



![logo](images/walter_cat.jpg) _New [team](https://github.com/pywinauto) icon_. Thanks, [_Anna_](https://www.behance.net/anna9111990), who painted the icon for the team, cat Walter.  
Logo for the pywinauto library [is still wanted](https://github.com/pywinauto/pywinauto/issues/76).


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



## [](#setup)Setup

*   Just run `pip install pywinauto` (Py2.7+)

or

*   Install [pyWin32 extensions](http://sourceforge.net/projects/pywin32/files/pywin32/) (no need for Active Python except 3.4 64-bit)
*   Download [the latest version](https://github.com/pywinauto/pywinauto/releases/download/0.5.4/pywinauto-0.5.4.zip)
*   Just unpack and run `python setup.py install`

## [](#supported-controls)Supported controls

*   Native Windows controls (full support through Win32 API)
*   .NET Windows Forms (partial support through Win32 API, some basic controls only)


---  
## [](#demo)Demo

Here is a short screencast with Pywinauto in action:

![Notepad.exe automation example](images/notepad-simple2-ir.gif)
