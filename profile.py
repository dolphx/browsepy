from werkzeug.contrib.profiler import ProfilerMiddleware
from browsepy import app

app.wsgi_app = ProfilerMiddleware(app.wsgi_app)

app.config['directory_start']='/mnt/UNISDR'
app.config['directory_base']='/mnt/UNISDR'
app.config['directory_ignore'] = ['MedellinCompleto', 'Meta']
app.config["use_binary_multiples"] = False
app.config['title'] = 'UNISDR Global Assessment Report Download Portal'

app.run(debug=True, host='0.0.0.0')
