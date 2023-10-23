'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_MESA_window_pos'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_MESA_window_pos',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble)
def glWindowPos2dMESA(x,y):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glWindowPos2dvMESA(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat)
def glWindowPos2fMESA(x,y):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glWindowPos2fvMESA(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint)
def glWindowPos2iMESA(x,y):pass
@_f
@_p.types(None,arrays.GLintArray)
def glWindowPos2ivMESA(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort)
def glWindowPos2sMESA(x,y):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glWindowPos2svMESA(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glWindowPos3dMESA(x,y,z):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glWindowPos3dvMESA(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glWindowPos3fMESA(x,y,z):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glWindowPos3fvMESA(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint)
def glWindowPos3iMESA(x,y,z):pass
@_f
@_p.types(None,arrays.GLintArray)
def glWindowPos3ivMESA(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glWindowPos3sMESA(x,y,z):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glWindowPos3svMESA(v):pass
@_f
@_p.types(None,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glWindowPos4dMESA(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLdoubleArray)
def glWindowPos4dvMESA(v):pass
@_f
@_p.types(None,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat,_cs.GLfloat)
def glWindowPos4fMESA(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLfloatArray)
def glWindowPos4fvMESA(v):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint)
def glWindowPos4iMESA(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLintArray)
def glWindowPos4ivMESA(v):pass
@_f
@_p.types(None,_cs.GLshort,_cs.GLshort,_cs.GLshort,_cs.GLshort)
def glWindowPos4sMESA(x,y,z,w):pass
@_f
@_p.types(None,arrays.GLshortArray)
def glWindowPos4svMESA(v):pass