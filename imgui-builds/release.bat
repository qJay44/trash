@echo off
cls

Rem Build
cmake -S . -B Build\Release -G "MinGW Makefiles" -D CMAKE_BUILD_TYPE=Release
cmake --build Build\Release --config Release --target GLFW_IMGUI
cmake --build Build\Release --config Release --target SFML_IMGUI

