import glob
import json

presets = []

for preset_category_idx, preset_category_path in enumerate(
        glob.glob('presets/*')):
    preset_category_name = preset_category_path.split('/')[1]
    preset_category_data = {
        'idx': preset_category_idx,
        'name': preset_category_name,
        'subcategories': [],
    }

    for subcategory_preset_idx, subcategory_preset_path in enumerate(
            glob.glob(preset_category_path + '/*.txt')):
        preset_subcategory = subcategory_preset_path.split('/')[2].split(
            '.')[0]
        preset_subcategory_data = {
            'id': subcategory_preset_idx,
            'name': preset_subcategory,
            'presets': []
        }

        with open(subcategory_preset_path, 'r') as subcategory_preset_file:
            subcategory_presets = subcategory_preset_file.read().splitlines()
            for subcategory_idx, subcategory_preset in enumerate(
                    subcategory_presets):
                subcategory_preset_data = {
                    'id': subcategory_idx,
                    'name': subcategory_preset
                }
                preset_subcategory_data['presets'].append(
                    subcategory_preset_data)

        preset_category_data['subcategories'].append(preset_subcategory_data)

    presets.append(preset_category_data, )

with open("presets.json", "w") as presets_file:
    json.dump(presets, presets_file)
