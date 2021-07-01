import bpy

from bpy.props import FloatProperty, BoolProperty, EnumProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScEditOperatorNode
from ...helper import get_override

class ScEdgeCrease(Node, ScEditOperatorNode):
	bl_idname = "ScEdgeCrease"
	bl_label = "Edge Crease"
	
	in_crease: FloatProperty(default=1.0, min=-1.0, max=1.0, update=ScNode.update_value)

	def init(self, context):
		super().init(context)
		self.inputs.new("ScNodeSocketNumber", "Crease").init("in_crease", True)
	
	def error_condition(self):
		return (
			super().error_condition()
			or (self.inputs["Crease"].default_value < -1.0 or self.inputs["Crease"].default_value > 1.0)
		)
	
	def functionality(self):
		bpy.ops.transform.edge_crease(
			get_override(self.inputs["Object"].default_value, True),
			value = self.inputs["Crease"].default_value
		)