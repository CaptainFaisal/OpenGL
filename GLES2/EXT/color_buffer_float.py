'''OpenGL extension EXT.color_buffer_float

This module customises the behaviour of the 
OpenGL.raw.GLES2.EXT.color_buffer_float to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension allows a variety of floating point formats to be
	rendered to via framebuffer objects.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/color_buffer_float.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.EXT.color_buffer_float import *
from OpenGL.raw.GLES2.EXT.color_buffer_float import _EXTENSION_NAME

def glInitColorBufferFloatEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION