import os

original_dir = os.getcwd()
dir_name = 'plots'
os.chdir(dir_name)
image_paths = []
page = '<html><body>'
page += '<h1>Plots</h1>'
dirs = [d for d in os.listdir(".") if os.path.isdir(d)]
for d in sorted(dirs):
    page += f'<h2>{d}</h2>'
    files = os.listdir(d)
    for f in sorted(files):
        if f.endswith('.png'):
            page += f'<img src="{d}/{f}">'
page += '</body></html>'
with open(f'index.html', 'w') as f:
    f.write(page)
os.chdir(original_dir)
