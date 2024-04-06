// NOTE: Put a test.tga file and create textures" folder near the exe file

#include <iostream>
#include <ostream>
#include <string>

#include "hsv.hpp"

int main() {
  sf::Clock clock;

  sf::Texture tex;
  tex.loadFromFile("test.tga");

  sf::Image img = tex.copyToImage();
  int width = img.getSize().x;
  int height = img.getSize().y;

  int frame = 1;

  float dt;
  float rot = 36.f;
  float hue = 0.f;

  while (hue < 360.f) {
    std::cout << "frame: "<< frame << '\r' << std::flush;
    sf::Color col = HSV(hue);

    for (int i = 0; i < height; i++) {
      for (int j = 0; j < width; j++) {
        sf::Color p = img.getPixel(j, i);
        if (p.r >= 50 || p.g >= 50 || p.b >= 50)
          img.setPixel(j, i, col);
      }
    }

    std::string fileName = "textures/";
    fileName += std::to_string(frame);
    fileName += ".png";
    img.saveToFile(fileName);

    dt = clock.restart().asSeconds();
    hue += rot * dt;
    frame++;
  }

  std::cout << "\nDone\n";

	return 0;
}

