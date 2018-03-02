paths =
  main: 'main'
  dep: {}
  py: {}
  temp: {}

paths.temp.root = 'temp'
paths.temp.storage = "#{paths.temp.root}/storage"
paths.temp.venv = "#{paths.temp.root}/venv"

paths.dep.py = "#{paths.temp.root}/venv"
paths.dep.py_guard = "#{paths.temp.root}/pip.guard"

paths.py.lib = "#{paths.main}/lib"
paths.py.lib_file = "#{paths.py.lib}.zip"

module.exports = paths
