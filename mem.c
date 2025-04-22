// https://learn.microsoft.com/en-us/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex

#include <windows.h>
#include <stdio.h>

static const char* const units[4] = {"K", "KB", "MB", "GB"};

int main() {
  MEMORYSTATUSEX statex;
  statex.dwLength = sizeof(statex);
  GlobalMemoryStatusEx(&statex);

  float physInUse = statex.ullTotalPhys - statex.ullAvailPhys;

  int i;
  for (i = 0; i < 4 && physInUse >= 1000; i++)
    physInUse /= 1024;

  printf("%.2f %s", physInUse, units[i]);

  return 0;
}

