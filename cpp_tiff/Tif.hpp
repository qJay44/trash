#pragma once

#include "tiffio.h"

class Tif {
public:
  Tif(const fspath& path);
  ~Tif();

  u32 width() const;
  u32 height() const;
  u32 tileWidth() const;
  u32 tileHeight() const;
  u32 samples() const;
  u32 strips() const;
  u32 stripSize() const;

  void printInfo() const;

  u32* getRGBA() const;
  byte* getGrayscale() const;
  byte* getRGBAbytes() const;

private:
  TIFF* tif;
};

