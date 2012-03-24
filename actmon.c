/*
This file is part of actmon.

actmon is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

actmon is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with actmon.  If not, see <http://www.gnu.org/licenses/>.
*/

// Dependencies: X11 libxss python2.7
// Compiling: python2 setup.py build
// Packaging: python2 setup.py sdist
// Installing: python2 setup.py install

#include <python2.7/Python.h>

#include <time.h>
#include <stdio.h>
#include <unistd.h>

#include <X11/Xlib.h>
#include <X11/Xutil.h>
#include <X11/extensions/scrnsaver.h>



static PyObject * actmon_get_idle_time(PyObject *self, PyObject *args) {
  /* Returns idle time for the present display in milliseconds */
  time_t idle_time;
  static XScreenSaverInfo *mit_info;
  Display *display;
  int screen;
  mit_info = XScreenSaverAllocInfo();
  if((display=XOpenDisplay(NULL)) == NULL) { 
    PyErr_SetString(PyExc_IOError,
		    "The display cound not be open. Are you in X11?");
    return NULL; 
  }
  screen = DefaultScreen(display);
  XScreenSaverQueryInfo(display, RootWindow(display,screen), mit_info);
  idle_time = (mit_info->idle);
  XFree(mit_info);
  XCloseDisplay(display); 
  return Py_BuildValue("k", (unsigned long)idle_time); // k stands for unsigned long
}

static PyMethodDef actmon_methods[] = {
    {"get_idle_time",  actmon_get_idle_time, METH_NOARGS,
     "Returns idle time for the present display in milliseconds."},
    {NULL}        /* Sentinel */
};

PyMODINIT_FUNC
initactmon(void)
{
    (void)Py_InitModule("actmon", actmon_methods);
}
