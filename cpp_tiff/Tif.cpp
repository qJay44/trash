#include "Tif.hpp"

Tif::Tif(const fspath& path) {
  tif = TIFFOpen(path.string().c_str(), "r");
  if (!tif) {
    printf("Tiff can't open the file (%s)\n", path.string().c_str());
    exit(EXIT_FAILURE);
  }

  u32 tags = TIFFGetTagListCount(tif);
  printf("Tags: %d\n", tags);
  for (u32 i = 0; i < tags; i++) {
    printf("Tag %d: %d\n", i, TIFFGetTagListEntry(tif, i));
  }
}

Tif::~Tif() { TIFFClose(tif); }

u32 Tif::width() const {
  u32 r;
  TIFFGetField(tif, TIFFTAG_IMAGEWIDTH, &r);
  return r;
}

u32 Tif::height() const {
  u32 r;
  TIFFGetField(tif, TIFFTAG_IMAGELENGTH, &r);
  return r;
}

u32 Tif::tileWidth() const {
  u32 r;
  TIFFGetField(tif, TIFFTAG_TILEWIDTH, &r);
  return r;
}

u32 Tif::tileHeight() const {
  u32 r;
  TIFFGetField(tif, TIFFTAG_TILELENGTH, &r);
  return r;
}

u32 Tif::samples() const {
  u32 r;
  TIFFGetField(tif, TIFFTAG_SAMPLESPERPIXEL, &r);
  return r;
}

u32 Tif::strips() const { return TIFFNumberOfStrips(tif); }

u32 Tif::stripSize() const { return TIFFStripSize(tif); }

void Tif::printInfo() const {
  const char* msg = "w: %d, h: %d, tile width: %d, tile height: %d\n"
                    "samples: %d, strips: %d, srip size: %d\n";
  printf(msg, width(), height(), tileWidth(), tileHeight(), samples(), strips(), stripSize());
}

u32* Tif::getRGBA() const {
  u32 w = width();
  u32 h = height();
  size_t npixels = w * h;
  u32* raster = (u32*)_TIFFmalloc(npixels * sizeof(u32));

  if (raster) {
    if (!TIFFReadRGBAImage(tif, w, h, raster, 0)) {
      puts("(TIFFReadRGBAImage) error");
      exit(EXIT_FAILURE);
    }
  } else {
    puts("(_TIFFmalloc) error");
    exit(EXIT_FAILURE);
  }

  return raster;
}

byte* Tif::getGrayscale() const {
  u32 h = height();
  tsize_t scanline = TIFFScanlineSize(tif);
  byte* buf = (byte*)_TIFFmalloc(scanline);

  for (u32 row = 0; row < h; row++)
    TIFFReadScanline(tif, buf, row);

  return buf;
}

byte* Tif::getRGBAbytes() const {
  u32* raster = getRGBA();
  size_t size = width() * height();
  byte* buf = new byte[size * 4];
  for (u32 i = 0; i < size; i++) {
    u32 rgba = raster[i];
    u32 ii = i << 2;
    buf[ii + 0] = rgba >> 24;
    buf[ii + 1] = rgba >> 16 & 0x00'ff;
    buf[ii + 2] = rgba >> 8 & 0x00'00'ff;
    buf[ii + 3] = rgba & 0x00'00'00'ff;
  }

  _TIFFfree(raster);
  return buf;
}
