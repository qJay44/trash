
set LIBS=C:/Users/q44/Documents/Libs
set PROJ_ROOT=%LIBS%/proj-9.6.1/build/install
set TIFF_ROOT=%LIBS%/tiff-4.7.0/build/install
set SQLite3_ROOT=%LIBS%/sqlite-amalgamation-3500000
set CURL_ROOT=%LIBS%/curl-8.14.0_1-win64-mingw
set ZLIB_ROOT=%LIBS%/zlib-1.3.1/build/install
set PNG_ROOT=%LIBS%/lpng1648/build/install

if not exist build mkdir build
cd build

cmake .. ^
-DCMAKE_BUILD_TYPE=Release ^
-DCMAKE_INSTALL_PREFIX=install ^
-DCMAKE_PREFIX_PATH=%PROJ_ROOT%;%TIFF_ROOT%;%SQLite3_ROOT%;%CURL_ROOT% ^
-DPROJ_INCLUDE_DIR=%PROJ_ROOT%/include ^
-DPROJ_LIBRARY_RELEASE=%PROJ_ROOT%/lib/libproj.dll.a ^
-DGDAL_USE_TIFF=ON ^
-DTIFF_INCLUDE_DIR=%TIFF_ROOT%/include ^
-DTIFF_LIBRARY_RELEASE=%TIFF_ROOT%/lib/tiff.lib ^
-DGDAL_USE_SQLITE3=ON ^
-DSQLite3_INCLUDE_DIR=%SQLite3_ROOT% ^
-DSQLite3_LIBRARY=%SQLite3_ROOT%/libsqlite3.a ^
-DGDAL_USE_CURL=ON ^
-DCURL_INCLUDE_DIR=%CURL_ROOT%/include ^
-DCURL_LIBRARY=%CURL_ROOT%/lib/libcurl.dll.a ^
-DGDAL_USE_ZLIB=ON ^
-DZLIB_INCLUDE_DIR=%ZLIB_ROOT%/include ^
-DZLIB_LIBRARY_RELEASE=%ZLIB_ROOT%/lib/libzlib.dll.a ^
-DGDAL_USE_PNG=ON ^
-DPNG_INCLUDE_DIR=%PNG_ROOT%/include ^
-DPNG_LIBRARY_RELEASE=%PNG_ROOT%/lib/libpng16.dll.a ^

rem cmake --build . --target install

REM echo n | copy /-y %CURL_ROOT%/bin/libcurl-x64.dll install/bin
REM echo n | copy /-y %PROJ_ROOT%/bin/libproj_9.dll install/bin
REM echo n | copy /-y %TIFF_ROOT%/bin/libtiff.dll install/bin
REM echo n | copy /-y %ZLIB_ROOT%/bin/libzlib.dll install/bin
REM echo n | copy /-y %PNG_ROOT%/lib/libpng16.dll install/bin

cd ..
pause
