from flask import Flask, render_template, request, send_file, redirect, url_for
import io
import os

# Import conversion logic and character maps
from default_gen import (
    convert_from_chosen_map,
    char_map2, char_map3, char_map4, char_map5,
    char_map6, char_map7, char_map8, char_map9, char_map10
)

app = Flask(__name__)

# Build a list of all available signs from default_gen.py
ALL_SIGNS = []
for cm in (
    char_map2, char_map3, char_map4, char_map5,
    char_map6, char_map7, char_map8, char_map9, char_map10
):
    ALL_SIGNS.extend(cm.keys())
# Remove duplicates and sort by length descending then alphabetically
ALL_SIGNS = sorted(set(ALL_SIGNS), key=lambda s: (-len(s), s))


@app.route('/')
def index():
    return redirect(url_for('select_signs'))


@app.route('/select-signs', methods=['GET'])
def select_signs():
    """
    Render a page with file upload and checkboxes for each available sign.
    """
    return render_template('select_signs.html', signs=ALL_SIGNS)


@app.route('/convert-with-chosen', methods=['POST'])
def convert_with_chosen():
    """
    Handle form submission: read uploaded text, apply chosen signs, and return output file.
    """
    # 1. Read the uploaded .txt file
    uploaded = request.files.get('input_file')
    if not uploaded or uploaded.filename == '':
        return redirect(url_for('select_signs'))

    text_bytes = uploaded.read()
    try:
        text = text_bytes.decode('utf-8')
    except UnicodeDecodeError:
        text = text_bytes.decode('utf-8', errors='ignore')

    # 2. Build chosen_map from selected checkboxes
    chosen_keys = request.form.getlist('signs')
    chosen_map = {}
    # For each chosen key, find its value in char_maps
    for key in chosen_keys:
        for cm in (
            char_map2, char_map3, char_map4, char_map5,
            char_map6, char_map7, char_map8, char_map9, char_map10
        ):
            if key in cm:
                chosen_map[key] = cm[key]
                break

    # 3. Generate paragraphs using the conversion logic
    paragraphs = convert_from_chosen_map(text, chosen_map)

    # 4. Create in-memory text file for download
    output_stream = io.StringIO()
    for idx, para in enumerate(paragraphs, 1):
        output_stream.write(f"--- Paragraph {idx} ---\n")
        output_stream.write(para + "\n\n")
    output_stream.seek(0)

    return send_file(
        io.BytesIO(output_stream.read().encode('utf-8-sig')),
        as_attachment=True,
        download_name='output_chosen.txt',
        mimetype='text/plain'
    )


if __name__ == '__main__':
    app.run(debug=True)
