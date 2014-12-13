'''OpenGL extension SGI.color_matrix

This module customises the behaviour of the 
OpenGL.raw.GL.SGI.color_matrix to provide a more 
Python-friendly API

Overview (from the spec)
	
	    This extension adds a 4x4 matrix stack to the pixel transfer path.  The
	    matrix operates on RGBA pixel groups, using the equation
	
		C' = MC,
	
	    where
	
		    |R|
		C = |G|
		    |B|
		    |A|
	
	    and M is the 4x4 matrix on the top of the color matrix stack.  After
	    the matrix multiplication, each resulting color component is scaled
	    and biased by a programmed amount.  Color matrix multiplication follows
	    convolution (and the scale, and bias that are associated with
	    convolution.)
	
	    The color matrix can be used to reassign and duplicate color components.
	    It can also be used to implement simple color space conversions.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/SGI/color_matrix.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.SGI.color_matrix import *
from OpenGL.raw.GL.SGI.color_matrix import _EXTENSION_NAME

def glInitColorMatrixSGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION