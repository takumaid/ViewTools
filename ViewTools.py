import bpy

bl_info = {
    "name": "View tools", # アドオン一覧に表示される名前
    "author": "takuma",  # 作者
    "version": (1, 0), # アドオンのバージョン
    "blender": (2, 80, 0), # 対応するBlenderのバージョン
    "location": "",
    "description": "Tiny tools for viewport", # アドオンの説明
    "warning": "",
    "support": "TESTING", # アドオンの分類
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View" # カテゴリー
}

class HID_PT_UI(bpy.types.Panel):
    bl_label = "ViewTools"
    bl_category = "ViewTools"
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
        brow.operator("hid.subsonoff", text='ON', icon='MOD_SUBSURF').subs = True
        brow.operator("hid.subsonoff", text='OFF',icon='MESH_ICOSPHERE').subs = False
        
        row = layout.row(align=False)
        box = row.box()
        box.label(text =  'Armature switch')
        brow = box.row(align=True)
        brow.operator("hid.armatureonoff", text='Pose', icon='MESH_CIRCLE').subs = 'POSE'
        brow.operator("hid.armatureonoff", text='Rest', icon='X').subs = 'REST'
        
        row = layout.row(align=False)
        box = row.box()
        box.label(text =  'Wire switch')
        brow = box.row(align=True)
        brow.operator("hid.wireonoff", text='+WIRE', icon='SHADING_WIRE').subs = True
        brow.operator("hid.wireonoff", text='SOLID', icon='SHADING_SOLID').subs = False
       
        
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

class HID_OT_Wire(bpy.types.Operator):
    bl_idname = "hid.wireonoff"
    bl_label = "Button"
    subs : bpy.props.BoolProperty()
    
    def execute(self, context):
        if bpy.context.selected_objects == []:
            for dat in bpy.data.objects:
                try:
                    dat.show_wire = self.subs
                except:
                    pass
        else:
            for dat in bpy.context.selected_objects:
                try:
                    dat.show_wire = self.subs
                except:
                    pass

        return{'FINISHED'}

classes = (
    HID_PT_UI,
    HID_OT_SubSurf,
    HID_OT_Armature,
    HID_OT_Wire
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()