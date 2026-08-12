// tft_music_screen.h  (OPTIONAL — not wired into xonframe.ino)
//
// This is your second Lopaka export, drawScreen_1(). It targets a
// TFT_eSPI-style color SPI display (tft.fillScreen, tft.pushImage — a
// 320x240 canvas), NOT the Waveshare 0.49" SSD1306 in your current BOM.
// The SSD1306 is a 128x64 monochrome I2C display; this code physically
// cannot run on it.
//
// Keeping this here in case you add a color TFT panel later (e.g. paired
// with the v2 Sony ECX336CN micro-OLED path, though note that panel is
// MIPI, not SPI TFT either — you'd need an actual SPI TFT module like an
// ILI9341 to use this as-is). Requires the TFT_eSPI library and a `tft`
// object configured for your panel before calling drawScreen_1().

#pragma once
#include <Arduino.h>
#include <pgmspace.h>
// #include <TFT_eSPI.h>  // uncomment once you have TFT_eSPI installed and configured
// extern TFT_eSPI tft;

// NOTE: image_images_pixels below is the large "images" bitmap (120x120,
// RGB565) from your Lopaka export — kept as-is from your paste.
static const uint16_t PROGMEM image_images_pixels[] = {
  // ... (full RGB565 pixel array from your Lopaka export — omitted here
  //      for brevity, copy it verbatim from your original paste into
  //      this array before compiling)
};

static const unsigned char PROGMEM image_music_next_bits[] = {0x00,0x00,0xe0,0x0f,0x90,0x09,0x8c,0x09,0x82,0x09,0x81,0x89,0x80,0x49,0x80,0x39,0x80,0x39,0x80,0x49,0x81,0x89,0x82,0x09,0x8c,0x09,0x90,0x09,0xe0,0x0f,0x00,0x00};
static const unsigned char PROGMEM image_music_next_copy_1_bits[] = {0x00,0x00,0xf0,0x07,0x90,0x09,0x90,0x31,0x90,0x41,0x91,0x81,0x92,0x01,0x9c,0x01,0x9c,0x01,0x92,0x01,0x91,0x81,0x90,0x41,0x90,0x31,0x90,0x09,0xf0,0x07,0x00,0x00};
static const unsigned char PROGMEM image_music_pause_bits[] = {0xf9,0xf0,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0x89,0x10,0xf9,0xf0,0x00,0x00};
static const unsigned char PROGMEM image_wifi_full_bits[] = {0x01,0xf0,0x00,0x07,0xfc,0x00,0x1e,0x0f,0x00,0x39,0xf3,0x80,0x77,0xfd,0xc0,0xef,0x1e,0xe0,0x5c,0xe7,0x40,0x3b,0xfb,0x80,0x17,0x1d,0x00,0x0e,0xee,0x00,0x05,0xf4,0x00,0x03,0xb8,0x00,0x01,0x50,0x00,0x00,0xe0,0x00,0x00,0x40,0x00,0x00,0x00,0x00};

/*
void drawScreen_1(void) {
  tft.fillScreen(0x0);
  tft.setTextColor(0xFFFF);
  tft.setTextSize(2);
  tft.drawString("Happiness", 39, 86);
  tft.setTextSize(1);
  tft.drawString("The 1975", 67, 110);
  tft.pushImage(180, 70, 120, 120, image_images_pixels);
  tft.drawBitmap(85, 133, image_music_pause_bits, 12, 16, 0xFFFF);
  tft.drawBitmap(123, 132, image_music_next_bits, 16, 16, 0xFFFF);
  tft.drawBitmap(39, 133, image_music_next_copy_1_bits, 16, 16, 0xFFFF);
  tft.drawLine(0, 33, 318, 33, 0xFFFF);
  tft.drawLine(319, -2, 319, 243, 0xFFFF);
  tft.drawLine(0, -1, 0, 244, 0xFFFF);
  tft.drawLine(1, 0, 319, 0, 0xFFFF);
  tft.drawLine(4, 239, 322, 239, 0xFFFF);
  tft.drawBitmap(267, 9, image_wifi_full_bits, 19, 16, 0xFFFF);
  tft.setTextSize(2);
  tft.drawString("12:00 AM", 10, 11);
  tft.drawString("SUNDAY", 155, 11);
  tft.drawRect(35, 156, 108, 11, 0xFFFF);
  tft.fillRect(36, 157, 16, 10, 0xFFFF);
  tft.setTextSize(1);
  tft.drawString("0:30", 80, 173);
}
*/
