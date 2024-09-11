import bpy

def get_char_from_color(color):
    r, g, b, _ = color
    ascii_val = int(r * 255) + (int(g * 255) << 8) + (int(b * 255) << 16)
    return chr(ascii_val)

def export_cubes_to_text(output_file):
    decrypted_data = ''

    # キューブを名前でソートして、順序を守って処理
    cubes = [obj for obj in bpy.data.objects if obj.name.startswith('TextCube_')]
    cubes.sort(key=lambda x: int(x.name.split('_')[1]))

    for obj in cubes:
        for mat_slot in obj.material_slots:
            if mat_slot.material:
                color = mat_slot.material.diffuse_color
                try:
                    char = get_char_from_color(color)
                    decrypted_data += char
                except Exception as e:
                    print(f"Error processing color {color}: {e}")

    try:
        if decrypted_data.strip():
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(decrypted_data)
            print(f"Data successfully written to {output_file}")
        else:
            print("No data to write.")
    except Exception as e:
        print(f"An error occurred: {e}")

export_cubes_to_text('C:/Users/Owner/Desktop/txt4b3d/decrypted.txt')
