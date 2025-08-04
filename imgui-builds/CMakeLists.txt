include(./.env.cmake OPTIONAL RESULT_VARIABLE LOCAL_ENV)
message(STATUS "Local .env.cmake: ${LOCAL_ENV}")

cmake_minimum_required(VERSION 3.21)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

message(STATUS ${CMAKE_BUILD_TYPE})

project(MyProject VERSION 1.0)

# Common source files
file(GLOB_RECURSE SOURCES ${PROJECT_SOURCE_DIR}/src/*.cpp)

# --------------- GLFW + ImGui --------------- #

add_library(GLFW_IMGUI SHARED ${SOURCES})

target_include_directories(GLFW_IMGUI PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include ${GLFW_PATH}/include)
target_link_directories(GLFW_IMGUI PRIVATE ${GLFW_PATH}/lib-mingw-w64)
target_link_libraries(GLFW_IMGUI PRIVATE glfw3)

# --------------- SFML + ImGui --------------- #

list(REMOVE_ITEM SOURCES ${PROJECT_SOURCE_DIR}/src/imgui_impl_glfw.cpp)
list(APPEND SOURCES ${IMGUI_SFML_PATH}/imgui-SFML.cpp)

add_library(SFML_IMGUI SHARED ${SOURCES} ${IMGUI_SFML_PATH}/imgui-SFML.cpp)

find_package(SFML 3 REQUIRED COMPONENTS System Window Graphics PATHS ${SFML_PATH})

target_include_directories(SFML_IMGUI PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(SFML_IMGUI PRIVATE SFML::System SFML::Window SFML::Graphics opengl32)

