import bpy

def char_to_color(char):
    ascii_val = ord(char)
    r = (ascii_val & 0xFF) / 255.0
    g = ((ascii_val >> 8) & 0xFF) / 255.0
    b = ((ascii_val >> 16) & 0xFF) / 255.0
    return (r, g, b, 1.0)

def import_text_to_cubes(input_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        text_data = file.read()

    # 既存のキューブオブジェクトを削除
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()  

    # キューブの追加
    for i, char in enumerate(text_data):
        bpy.ops.mesh.primitive_cube_add()
        cube = bpy.context.object
        cube.name = f'TextCube_{i}'

        # マテリアルを作成し、色を設定
        material = bpy.data.materials.new(name=f'TextMaterial_{i}')
        material.use_nodes = False
        material.diffuse_color = char_to_color(char)

        if not cube.data.materials:
            cube.data.materials.append(material)
        else:
            cube.data.materials[0] = material

import_text_to_cubes('C:/Users/Owner/Documents/input.txt')
