import bpy

from bpy.props import FloatProperty, BoolProperty, EnumProperty
from bpy.types import Node
from .._base.node_base import ScNode
from .._base.node_operator import ScEditOperatorNode
from ...helper import get_override

class ScShear(Node, ScEditOperatorNode):
	bl_idname = "ScShear"
	bl_label = "Shear"
	
	in_offset: FloatProperty(default=1.0, update=ScNode.update_value)
	in_axis: EnumProperty(items=[('X', 'X', ''), ('Y', 'Y', ''), ('Z', 'Z', '')], default='Z', update=ScNode.update_value)
	in_mirror: BoolProperty(update=ScNode.update_value)

	def init(self, context):
		super().init(context)
		self.inputs.new("ScNodeSocketNumber", "Offset").init("in_offset", True)
		self.inputs.new("ScNodeSocketString", "Axis").init("in_axis")
		self.inputs.new("ScNodeSocketBool", "Mirror").init("in_mirror")
	
	def functionality(self):
		bpy.ops.transform.shear(
			get_override(self.inputs["Object"].default_value, True),
			value = self.inputs["Offset"].default_value,
			orient_axis = self.inputs["Axis"].default_value,
			#orient_axis_ortho = 'X',
			#orient_type = 'GLOBAL',
			#orient_matrix = ((0, 0, 0), (0, 0, 0), (0, 0, 0)),
			#orient_matrix_type = 'GLOBAL',
			mirror = self.inputs["Mirror"].default_value,
			use_proportional_edit = bpy.context.scene.tool_settings.use_proportional_edit,
			proportional_edit_falloff = bpy.context.scene.tool_settings.proportional_edit_falloff,
			proportional_size = bpy.context.scene.tool_settings.proportional_size,
			use_proportional_connected = bpy.context.scene.tool_settings.use_proportional_connected,
			#use_proportional_projected = False,
			snap = bpy.context.scene.tool_settings.use_snap,
			snap_target = bpy.context.scene.tool_settings.snap_target,
			#snap_point = (0, 0, 0),
			snap_align = bpy.context.scene.tool_settings.use_snap_align_rotation
			#snap_normal = (0, 0, 0),
			#gpencil_strokes = False,
			#release_confirm = False,
			#use_accurate = False
		)