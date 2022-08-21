import glob
import json

modifiers = []

for modifier_category_idx, modifier_category_path in enumerate(
        glob.glob('modifiers/*')):
    modifier_category_name = modifier_category_path.split('/')[1]
    modifier_category_data = {
        'id': modifier_category_idx + 1,
        'name': modifier_category_name,
        'subcategories': [],
    }

    for subcategory_modifier_idx, subcategory_modifier_path in enumerate(
            glob.glob(modifier_category_path + '/*.txt')):
        modifier_subcategory = subcategory_modifier_path.split('/')[2].split(
            '.')[0]
        modifier_subcategory_data = {
            'id': subcategory_modifier_idx + 1,
            'name': modifier_subcategory,
            'modifiers': []
        }

        with open(subcategory_modifier_path, 'r') as subcategory_modifier_file:
            subcategory_modifiers = subcategory_modifier_file.read(
            ).splitlines()
            for subcategory_idx, subcategory_modifier in enumerate(
                    subcategory_modifiers):
                subcategory_modifier_data = {
                    'id': subcategory_idx + 1,
                    'name': subcategory_modifier
                }
                modifier_subcategory_data['modifiers'].append(
                    subcategory_modifier_data)

        modifier_category_data['subcategories'].append(
            modifier_subcategory_data)

    modifiers.append(modifier_category_data, )

with open("modifiers.json", "w") as modifiers_file:
    json.dump(modifiers, modifiers_file)
