project('libui', ['c', 'cpp'],
        version: 'Alpha 3.5',
        license: 'MIT',
        default_options: ['warning_level=3', 'default_library=shared',
                          'c_std=c99', 'cpp_std=c++11', 'cpp_eh=sc'])


cc = meson.get_compiler('c')

# Various flags for msvc
if (cc.get_id() == 'msvc')
  add_project_arguments('/wd4100', '/RTC1', '/RTCs', '/RTCu', '/bigobj', language: ['c', 'cpp'])
  add_project_link_arguments('/LARGEADDRESSAWARE', '/INCREMENTAL:NO', 'MANIFEST:NO', language: ['c', 'cpp'])
endif

# Symbol visibility on *nix
if (cc.has_argument('-fvisibility=hidden'))
  add_project_arguments('-fvisibility=hidden', language: ['c', 'cpp', 'objc'])
  add_project_link_arguments('-fvisibility=hidden', language: ['c', 'cpp', 'objc'])
endif

# Disable some warnings
if (cc.has_argument('-Wno-unused-parameter'))
  add_project_arguments('-Wno-unused-parameter', language: ['c', 'cpp', 'objc'])
endif
if (cc.has_argument('-Wno-switch'))
  add_project_arguments('-Wno-switch', language: ['c', 'cpp', 'objc'])
endif

libui_src = []
libui_inc = [include_directories('.')]
libui_defs = []
libui_deps = []

install_headers('ui.h')

subdir('common')
if (host_machine.system() == 'darwin')
  install_headers('ui_darwin.h')
  subdir('darwin')
elif (host_machine.system() == 'windows')
  install_headers('ui_windows.h')
#  subdir('window')
else
  install_headers('ui_unix.h')
  subdir('unix')
endif

# TODO: Set soversion/version for shared libraries!
libui = library('ui', libui_src,
                dependencies: libui_deps,
                c_args: '-Dlibui_EXPORTS',
                objc_args: '-Dlibui_EXPORTS',
                install: true)
libui_dep = declare_dependency(link_with: libui,
                               include_directories: libui_inc,
                               compile_args: libui_defs,
                               dependencies: libui_deps,
                               version: meson.project_version())

subdir('test')
subdir('examples')
