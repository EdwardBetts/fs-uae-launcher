'''OpenGL extension ATI.map_object_buffer

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.map_object_buffer to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension provides a mechanism for an application to obtain
	the virtual address of an object buffer. This allows the
	application to directly update the contents of an object buffer
	and avoid any intermediate copies.
	

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ATI/map_object_buffer.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.ATI.map_object_buffer import *
from OpenGL.raw.GL.ATI.map_object_buffer import _EXTENSION_NAME

def glInitMapObjectBufferATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION