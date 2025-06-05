@echo off
setlocal enabledelayedexpansion

rem Get the escape character
for /f "delims=" %%A in ('echo prompt $E^| cmd') do set "ESC=%%A"

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
-DCMAKE_PREFIX_PATH=%PROJ_ROOT%;%TIFF_ROOT%;%SQLite3_ROOT%;%CURL_ROOT%;%ZLIB_ROOT%;%PNG_ROOT% ^
-DGDAL_USE_TIFF=ON ^
-DGDAL_USE_SQLITE3=ON ^
-DGDAL_USE_CURL=ON ^
-DGDAL_USE_ZLIB=ON ^
-DGDAL_USE_PNG=ON

if %ERRORLEVEL% neq 0 (
	rem Print bright red text
	echo !ESC![91mCMake configuration failed !ESC!
	rem Reset formatting explicitly at end of script
	echo !ESC![0m
    exit /b %ERRORLEVEL%
)

cmake --build . --target install

if %ERRORLEVEL% neq 0 (
	rem Print bright red text
	echo !ESC![91mCMake configuration failed !ESC!
	rem Reset formatting explicitly at end of script
	echo !ESC![0m
    exit /b %ERRORLEVEL%
)

echo n | copy /-y %CURL_ROOT%/bin/libcurl-x64.dll install/bin
echo n | copy /-y %PROJ_ROOT%/bin/libproj_9.dll install/bin
echo n | copy /-y %TIFF_ROOT%/bin/libtiff.dll install/bin
echo n | copy /-y %ZLIB_ROOT%/bin/libzlib.dll install/bin
echo n | copy /-y %PNG_ROOT%/lib/libpng16.dll install/bin

cd ..
endlocal
pause

