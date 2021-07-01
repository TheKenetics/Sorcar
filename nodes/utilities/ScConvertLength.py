import bpy

from bpy.props import EnumProperty, FloatProperty
from bpy.types import Node
from .._base.node_base import ScNode

# Constants
CONVERSION_AMOUNT = {
	"INCHES" : 0.0254,
	"FEET" : 0.3048,
	"CENTIMETERS" : 0.01,
	"MILLIMETERS" : 0.001
}

class ScConvertLength(Node, ScNode):
	bl_idname = "ScConvertLength"
	bl_label = "Convert Length"

	in_length: FloatProperty(update=ScNode.update_value)
	in_type: EnumProperty(name="Type", items=[("INCHES", "Inches", ""), ("FEET", "Feet", ""), ("CENTIMETERS", "Centimeters", ""), ("MILLIMETERS", "Millimeters", "")], update=ScNode.update_value)

	def init(self, context):
		super().init(context)
		self.inputs.new("ScNodeSocketNumber", "Length").init("in_length", True)
		self.inputs.new("ScNodeSocketString", "Type").init("in_type", True)
		self.outputs.new("ScNodeSocketNumber", "Value")
	
	def error_condition(self):
		return not self.inputs["Type"].default_value in {"INCHES", "FEET", "CENTIMETERS", "MILLIMETERS"}

	def post_execute(self):
		return {"Value" : self.inputs["Length"].default_value * CONVERSION_AMOUNT[self.inputs["Type"].default_value]}