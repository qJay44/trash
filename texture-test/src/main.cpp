// NOTE: Put a "tex.png" file near the exe file

#include <iostream>
#include <ostream>
#include <string>
#include <filesystem>

#include "hsv.hpp"

namespace fs = std::filesystem;

int main() {
  sf::Texture tex;
  tex.loadFromFile("tex.png");

  sf::Image img = tex.copyToImage();
  int width = img.getSize().x;
  int height = img.getSize().y;

  constexpr int maxFrames = 50;
  constexpr int minBrightness = 50;
  constexpr float rot = 360.f / maxFrames;

  float hue = 0.f;
  int frame = 1;

  if (!fs::exists("textures")) fs::create_directory("textures");

  while (hue < 360.f) {
    std::cout << "frame: "<< frame << "/" << maxFrames << '\r' << std::flush;
    sf::Color col = HSV(hue);

    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        sf::Color p = img.getPixel(j, i);
        if (p.r >= minBrightness || p.g >= minBrightness || p.b >= minBrightness) // Assuming alpha is always 255
          img.setPixel(j, i, col);
      }
    }

    std::string fileName = "textures/";
    fileName += std::to_string(frame);
    fileName += ".png";
    img.saveToFile(fileName);

    hue += rot;
    frame++;
  }

  std::cout << "\nDone\n";

	return 0;
}

