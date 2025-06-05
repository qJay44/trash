@echo off

set ZLIB_ROOT=C:/Users/q44/Documents/Libs/zlib-1.3.1/build/install

mkdir build
cd build

cmake .. ^
-DCMAKE_BUILD_TYPE=Release ^
-DCMAKE_INSTALL_PREFIX=install ^
-DZLIB_INCLUDE_DIR=%ZLIB_ROOT%/include ^
-DZLIB_LIBRARY=%ZLIB_ROOT%/lib/libzlib.dll.a

cmake --build . --target install

cd ..
pause
