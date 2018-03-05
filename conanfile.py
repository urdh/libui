from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "libui"
    version = "0.0.35a"
    license = "MIT"
    url = "https://github.com/andlabs/libui"
    description = "Simple and portable (but not inflexible) GUI library in C "\
        "that uses the native GUI technologies of each platform it supports."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports_sources = "CMakeLists.txt", "*.h",         \
        "common/*", "darwin/*", "unix/*", "windows/*", \
        "examples/*", "test/*",

    def build(self):
        cmake = CMake(self)
        cmake.configure(
            source_folder=self.source_folder,
            defs={
                'CMAKE_BUILD_TYPE': 'Release',
                'BUILD_SHARED_LIBS': self.options.shared
            }
        )
        cmake.build()

    def package(self):
        self.copy("ui.h", dst="include", src=self.source_folder)
        if tools.os_info.is_windows:
            self.copy("ui_windows.h", dst="include", src=self.source_folder)
        elif tools.os_info.is_macos:
            self.copy("ui_darwin.h", dst="include", src=self.source_folder)
        else:
            self.copy("ui_unix.h", dst="include", src=self.source_folder)
        self.copy("out/libui.*", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["ui"]
