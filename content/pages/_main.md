Title: Pywinauto
Slug: pywinauto-GUI-automation-tool
Summary: Windows GUI automation with python
URL:
Save_as: index.html

**pywinauto** is a set of python modules to automate the Microsoft Windows GUI. At its simplest it allows you to send mouse and keyboard actions to windows dialogs and controls, but it also supports more complex actions.

#### [pywinauto 0.6.0 is in the master branch](https://github.com/pywinauto/pywinauto/zipball/master/) (October, 30, 2016)  
> This big release introduces MS UI Automation (UIA) support. Just start from:  
    `app = Application(backend='uia').start('your_app.exe')`.  
    Supported controls:  
    *Menu*, *Button*/*CheckBox*/*RadioButton*, *ComboBox*, *Edit*, *Tab control*, *List* (*ListView*), *DataGrid*, *Tree*, *Toolbar*, *Tooltip*, *Slider*.

> Documentation is built continuously now on [ReadTheDocs](https://pywinauto.readthedocs.io/en/latest/).
  See also our improved [Getting Started Guide](https://pywinauto.readthedocs.io/en/latest/getting_started.html)

> New multi-backend architecture makes implementation of new platforms support
  easier in the future. The minimal set for new backend includes its name and
  two classes inherited from
  [ElementInfo](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.element_info.html?highlight=ElementInfo#pywinauto.element_info.ElementInfo)
  and from
  [BaseWrapper](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.base_wrapper.html#pywinauto.base_wrapper.BaseWrapper) classes.
  New backend must be registered by a call to
  [backend.register()](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.backend.html?highlight=backend.register#pywinauto.backend.register).

> Code style is much closer to PEP8: i.e. `click_input` should be used
  instead of `ClickInput`.

> Initial implementation of the *hooks* module. Keyboard and mouse event
  handlers can be registered in the system. It was inspired by *pyHook*, *pyhk*,
  *pyhooked* and similar modules, but re-written from scratch. Thanks for
  Max Samokhvalov! The fork of the *hooks* module is used in *pyhooked 0.8*
  by Ethan Smith.

> A lot of small improvements are not counted here.

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