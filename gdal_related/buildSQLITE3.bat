gcc -DSQLITE_ENABLE_RTREE -o sqlite3.o sqlite3.c shell.c
ar rcs libsqlite3.a sqlite3.o
gcc -DSQLITE_ENABLE_RTREE -o sqlite3.exe sqlite3.c shell.c
gcc -DSQLITE_ENABLE_RTREE -shared -o libsqlite3.dll sqlite3.c -Wl,--out-implib,libsqlite3.a
pause