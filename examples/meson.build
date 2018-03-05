resources = []

if (host_machine.system() == 'windows')
  resources += ['resources.rc']
endif

controlgallery = executable('controlgallery', ['controlgallery/main.c'] + resources,
                            dependencies: libui_dep,
                            gui_app: false,
                            install: false)

histogram = executable('histogram', ['histogram/main.c'] + resources,
                       dependencies: libui_dep,
                       gui_app: false,
                       install: false)

threads = dependency('threads')
cpp_multithread = executable('cpp-multithread', ['cpp-multithread/main.cpp'] + resources,
                             dependencies: [libui_dep, threads],
                             gui_app: false,
                             install: false)
