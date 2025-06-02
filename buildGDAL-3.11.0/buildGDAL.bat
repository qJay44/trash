
set LIBS="C:/Users/q44/Documents/Libs"

if not exist build mkdir build
cd build
if not exist install mkdir install

cmake .. ^
-DCMAKE_INSTALL_PREFIX="install" ^
-DCMAKE_PREFIX_PATH="%LIBS%/proj-9.6.0/build/install" ^
-DPROJ_INCLUDE_DIR="%LIBS%/proj-9.6.0/build/install/include" ^
-DPROJ_LIBRARY_RELEASE="%LIBS%/proj-9.6.0/build/install/lib/libproj.dll.a" ^
-DTIFF_INCLUDE_DIR="%LIBS%/tiff-4.7.0/install/include" ^
-DTIFF_LIBRARY_RELEASE="%LIBS%/tiff-4.7.0/install/lib/tiff.lib" ^
-DGDAL_USE_SQLITE3=ON ^
-DSQLite3_INCLUDE_DIR="%LIBS%/sqlite-amalgamation-3500000" ^
-DSQLite3_LIBRARY="%LIBS%/sqlite-amalgamation-3500000/libsqlite3.a" ^
-DCURL_INCLUDE_DIR="%LIBS%/curl-8.14.0_1-win64-mingw/include" ^
-DCURL_LIBRARY="%LIBS%/curl-8.14.0_1-win64-mingw/lib/libcurl.dll.a"

cmake --build . --target install

cd ..
pause
