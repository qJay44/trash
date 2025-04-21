#include <windows.h>
#include <stdio.h>

static const char* const units[4] = {"K", "KB", "MB", "GB"};

int main() {
  MEMORYSTATUSEX statex;
  statex.dwLength = sizeof(statex);
  GlobalMemoryStatusEx(&statex);

  float physInUse = statex.ullTotalPhys - statex.ullAvailPhys;

  int i;
  for (i = 0; i < 4; i++)
    if (physInUse >= 1000)
      physInUse /= 1024;
    else
      break;

  printf("%.2f %s", physInUse, units[i]);

  return 0;
}

