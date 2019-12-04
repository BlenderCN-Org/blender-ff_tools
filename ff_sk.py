import bpy
from bpy import context as context
mapping = [
'browInnerUp', 'browDown_L', 'browDown_R', 'browOuterUp_L', 'browOuterUp_R',
'eyeLookUp_L', 'eyeLookUp_R', 'eyeLookDown_L', 'eyeLookDown_R', 'eyeLookIn_L', 'eyeLookIn_R', 'eyeLookOut_L', 'eyeLookOut_R',
'eyeBlink_L', 'eyeBlink_R', 'eyeSquint_L', 'eyeSquint_R', 'eyeWide_L', 'eyeWide_R',
'cheekPuff', 'cheekSquint_L', 'cheekSquint_R', 'noseSneer_L', 'noseSneer_R',
'jawOpen', 'jawForward', 'jawLeft', 'jawRight', 'mouthFunnel', 'mouthPucker', 'mouthLeft', 'mouthRight',
'mouthRollUpper', 'mouthRollLower', 'mouthShrugUpper', 'mouthShrugLower', 'mouthClose',
'mouthSmile_L', 'mouthSmile_R', 'mouthFrown_L', 'mouthFrown_R', 'mouthDimple_L', 'mouthDimple_R',
'mouthUpperUp_L', 'mouthUpperUp_R', 'mouthLowerDown_L', 'mouthLowerDown_R', 'mouthPress_L', 'mouthPress_R',
'mouthStretch_L', 'mouthStretch_R', 'tongueOut']
def addPropsInPbone():
    sk = obj.data.shape_keys
    skb = sk.key_blocks
    for i in range(1,len(skb)):
        print(skb[i])
        pbone[skb[i].name]=0.0


def addDriversToShapeKeys():
    sk = obj.data.shape_keys
    skb = sk.key_blocks
    for i in range(1,len(skb)):
        #print(skb[i])
        #pbone[skb[i].name]=0.0
        data_path = "key_blocks[\"" + skb[i].name + "\"].value"
        print (data_path)
        dr = obj.data.shape_keys.driver_add(data_path)
        dr.driver.type='SCRIPTED'

        var = dr.driver.variables.new()
        var.type = 'SINGLE_PROP'
        var.targets[0].id_type = 'OBJECT'
        var.targets[0].id = rig
        var.targets[0].data_path = "pose.bones[\""+pbone.name+"\"][\""+ skb[i].name +"\"]"
        print (var.targets[0].data_path)
        dr.driver.expression = "var"

#addPropsInPbone()
#addDriversToShapeKeys()
# def createShapeKeysFromList():
#     pass
# def removeAllShapeKeys():
#     pass
# def zeroOutAllShapeKeys():
#     pass
# def quickTestShapeKeys():
#     pass
# def getShapesByValue():
#     pass

class TestShapeKeyOperator(bpy.types.Operator):
    bl_idname = "ffsko.testshapekey"
    bl_label = "ffsko_TestShapeKey"

    def execute(self, context):
        print ("hi")
        return {'FINISHED'}


class FF_PT_ShapeKeys(bpy.types.Panel):
    bl_idname = "FF_PT_ShapeKeys"
    bl_label = "Shapekey Functions"
    bl_category = "FF_Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.operator ('ffsko.testshapekey', text="Print Shapekeys")