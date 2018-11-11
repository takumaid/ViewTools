import bpy

class HID_PT_UI(bpy.types.Panel):
    bl_label = "ViewTool"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    
    bpy.types.Scene.HID_OnOffModName = bpy.props.StringProperty(name='partial')
    
    def draw(self,context):
        
        layout = self.layout
        row = layout.row(align=False)
        box = row.box()
        box.label(text =  'Modifier switch')
        box.prop(context.scene, "HID_OnOffModName")
        brow = box.row(align=True)
        brow.alignment = 'EXPAND'
        brow.operator("hid.subsonoff", text='OFF',icon='MESH_ICOSPHERE').subs = False
        brow.operator("hid.subsonoff", text='ON', icon='MOD_SUBSURF').subs = True
        
        row = layout.row(align=False)
        box = row.box()
        box.label(text =  'Armature switch')
        brow = box.row(align=True)
        brow.operator("hid.armatureonoff", text='Pose',icon='OUTLINER_DATA_POSE').subs = 'POSE'
        brow.operator("hid.armatureonoff", text='Rest', icon='OUTLINER_DATA_ARMATURE').subs = 'REST'
        
        
class HID_OT_SubSurf(bpy.types.Operator):
    bl_idname = "hid.subsonoff"
    bl_label = "Button"
    subs : bpy.props.BoolProperty()

    def execute(self, context):
        modname = bpy.context.scene["HID_OnOffModName"]
        print(modname)
        if bpy.context.selected_objects == []:
            for obj in bpy.data.objects:
                for mod in obj.modifiers:
                    if modname in mod.name:
                        mod.show_viewport = self.subs
        else:
            for obj in bpy.context.selected_objects:
                for mod in obj.modifiers:
                    if modname in mod.name:
                        mod.show_viewport = self.subs
        return{'FINISHED'}

class HID_OT_Armature(bpy.types.Operator):
    bl_idname = "hid.armatureonoff"
    bl_label = "Button"
    subs : bpy.props.StringProperty()

    def execute(self, context):
        if bpy.context.selected_objects == []:
            for dat in bpy.data.objects:
                try:
                    dat.data.pose_position = self.subs
                except:
                    pass
        else:
            for dat in bpy.context.selected_objects:
                try:
                    dat.data.pose_position = self.subs
                except:
                    pass

        return{'FINISHED'}

classes = (
    HID_PT_UI,
    HID_OT_SubSurf,
    HID_OT_Armature
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()