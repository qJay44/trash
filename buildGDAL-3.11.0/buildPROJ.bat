@echo off

set LIBS="C:/Users/q44/Documents/Libs"

if not exist build mkdir build
cd build
if not exist install mkdir install

cmake .. ^
-DCMAKE_INSTALL_PREFIX="install" ^
-DCMAKE_PREFIX_PATH="%LIBS%/sqlite-amalgamation-3500000" ^
-DTIFF_INCLUDE_DIR="%LIBS%/tiff-4.7.0/install/include" ^
-DTIFF_LIBRARY_RELEASE="%LIBS%/tiff-4.7.0/install/lib/tiff.lib" ^
-DCURL_INCLUDE_DIR="%LIBS%/curl-8.14.0_1-win64-mingw/include" ^
-DCURL_LIBRARY="%LIBS%/curl-8.14.0_1-win64-mingw/lib/libcurl.dll.a"

cmake --build . --target install

cd ..
pause
