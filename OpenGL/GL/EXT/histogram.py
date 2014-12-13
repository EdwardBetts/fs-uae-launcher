'''OpenGL extension EXT.histogram

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.histogram to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension defines pixel operations that count occurences of
	specific color component values (histogram) and that track the minimum
	and maximum color component values (minmax).  An optional mode allows
	pixel data to be discarded after the histogram and/or minmax operations
	are completed.  Otherwise the pixel data continue on to the next
	operation unaffected.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/histogram.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.EXT.histogram import *
from OpenGL.raw.GL.EXT.histogram import _EXTENSION_NAME

def glInitHistogramEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION

glGetHistogramParameterfvEXT = wrapper.wrapper(glGetHistogramParameterfvEXT).setOutput(
    "params",(1,), orPassIn=True
)
glGetHistogramParameterivEXT = wrapper.wrapper(glGetHistogramParameterivEXT).setOutput(
    "params",(1,), orPassIn=True
)