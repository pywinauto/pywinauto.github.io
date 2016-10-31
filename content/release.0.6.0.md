Title: Pywinauto 0.6.0 
Date: 30/10/2016 10:20
Modified: 31/10/2016 09:00
Slug: pywinauto_0_6_is_released
Category: News
Summary: [pywinauto 0.6.0 is in the master branch](https://github.com/pywinauto/pywinauto/zipball/master/) (October, 30, 2016).  We are on the stabilization path now. This big release introduces MS UI Automation (UIA) support, just start from ``app = Application(backend='uia').start('your_app.exe')``

#### [pywinauto 0.6.0 is in the master branch](https://github.com/pywinauto/pywinauto/zipball/master/) (October, 30, 2016)  
- This big release introduces MS UI Automation (UIA) support. Just start from:  
    `app = Application(backend='uia').start('your_app.exe')`.  
    Supported controls:  
    *Menu*, *Button*/*CheckBox*/*RadioButton*, *ComboBox*, *Edit*, *Tab control*, *List* (*ListView*), *DataGrid*, *Tree*, *Toolbar*, *Tooltip*, *Slider*.

- Documentation is built continuously now on [ReadTheDocs](https://pywinauto.readthedocs.io/en/latest/).
  See also our improved [Getting Started Guide](https://pywinauto.readthedocs.io/en/latest/getting_started.html)

- Modules `keyboard` and `mouse` can be used out of any window context now. And they work on Linux as well!

- New multi-backend architecture makes implementation of new platforms support
  easier in the future. The minimal set for new backend includes its name and
  two classes inherited from
  [ElementInfo](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.element_info.html?highlight=ElementInfo#pywinauto.element_info.ElementInfo)
  and from
  [BaseWrapper](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.base_wrapper.html#pywinauto.base_wrapper.BaseWrapper) classes.
  New backend must be registered by a call to
  [backend.register()](http://pywinauto.readthedocs.io/en/latest/code/pywinauto.backend.html?highlight=backend.register#pywinauto.backend.register).

- Code style is much closer to PEP8: i.e. `click_input` should be used
  instead of `ClickInput`. Though `backend='win32'` is
  ~80% backward compatible with pywinauto 0.5.4.

- Initial implementation of the *hooks* module. Keyboard and mouse event
  handlers can be registered in the system. It was inspired by *pyHook*, *pyhk*,
  *pyhooked* and similar modules, but re-written from scratch. Thanks for
  Max Samokhvalov! The fork of the *hooks* module is used in *pyhooked 0.8*
  by Ethan Smith.

- A lot of small improvements are not counted here.
