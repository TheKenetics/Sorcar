import bpy

from bpy.props import FloatProperty, BoolProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScEditOperatorNode
from ...helper import get_override

class ScShrinkFatten(Node, ScEditOperatorNode):
	bl_idname = "ScShrinkFatten"
	bl_label = "ShrinkFatten"
	
	in_offset: FloatProperty(default=1.0, update=ScNode.update_value)
	in_use_even_offset: BoolProperty(update=ScNode.update_value)
	in_mirror: BoolProperty(update=ScNode.update_value)

	def init(self, context):
		super().init(context)
		self.inputs.new("ScNodeSocketNumber", "Offset").init("in_offset", True)
		self.inputs.new("ScNodeSocketBool", "Use Even Offset").init("in_use_even_offset")
		self.inputs.new("ScNodeSocketBool", "Mirror").init("in_mirror")
	
	def functionality(self):
		bpy.ops.transform.shrink_fatten(
			get_override(self.inputs["Object"].default_value, True),
			value = self.inputs["Offset"].default_value,
			use_even_offset = self.inputs["Use Even Offset"].default_value,
			mirror = self.inputs["Mirror"].default_value,
			use_proportional_edit = bpy.context.scene.tool_settings.use_proportional_edit,
			proportional_edit_falloff = bpy.context.scene.tool_settings.proportional_edit_falloff,
			proportional_size = bpy.context.scene.tool_settings.proportional_size,
			use_proportional_connected = bpy.context.scene.tool_settings.use_proportional_connected,
			#use_proportional_projected = False,
			snap = bpy.context.scene.tool_settings.use_snap,
			snap_target = bpy.context.scene.tool_settings.snap_target,
			#snap_point = (0, 0, 0),
			snap_align = bpy.context.scene.tool_settings.use_snap_align_rotation,
			snap_normal = (0, 0, 0)
			#release_confirm=False,
			#use_accurate=False
		)