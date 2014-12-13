'''OpenGL extension NV.vertex_program4

This module customises the behaviour of the 
OpenGL.raw.GL.NV.vertex_program4 to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension builds on the common assembly instruction set
	infrastructure provided by NV_gpu_program4, adding vertex program-specific
	features.
	
	This extension provides the ability to specify integer vertex attributes
	that are passed to vertex programs using integer data types, rather than
	being converted to floating-point values as in existing vertex attribute
	functions.  The set of input and output bindings provided includes all
	bindings supported by ARB_vertex_program.  This extension provides
	additional input bindings identifying the index of the vertex when vertex
	arrays are used ("vertex.id") and the instance number when instanced
	arrays are used ("vertex.instance", requires EXT_draw_instanced).  It
	also provides output bindings allowing vertex programs to directly specify
	clip distances (for user clipping) plus a set of generic attributes that
	allow programs to pass a greater number of attributes to subsequent
	pipeline stages than is possible using only the pre-defined fixed-function
	vertex outputs.
	
	By and large, programs written to ARB_vertex_program can be ported
	directly by simply changing the program header from "!!ARBvp1.0" to
	"!!NVvp4.0", and then modifying instructions to take advantage of the
	expanded feature set.  There are a small number of areas where this
	extension is not a functional superset of previous vertex program
	extensions, which are documented in the NV_gpu_program4 specification.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/vertex_program4.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.NV.vertex_program4 import *
from OpenGL.raw.GL.NV.vertex_program4 import _EXTENSION_NAME

def glInitVertexProgram4NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION