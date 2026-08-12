/*
  XonFrame Firmware — ESP32-S3FH4R2
  ----------------------------------
  - Streams OV5640 camera frames + IMU/battery telemetry over a WebSocket
    server at ws://<device-ip>:81/ws (matches the XonFrame Console protocol:
    binary frames = JPEG, text frames = JSON telemetry)
  - Serves OTA firmware updates at http://<device-ip>/update
  - Drives the Waveshare 0.49" SSD1306 OLED dashboard (battery/wifi/date/temp)

  Libraries needed (Library Manager):
    - WebSockets by Links2004 (arduinoWebSockets)
    - Adafruit SSD1306 + Adafruit GFX
    - ESP32 board package (gives esp_camera.h, WebServer.h, Update.h)

  NOTE: image_Weather_bitmap_pixels and image_border_pixels referenced by the
  dashboard layout were not included in your Lopaka export — re-export those
  two bitmaps from Lopaka and paste them into display_assets.h, or the
  weather icon / border will silently not draw (everything else will still
  render).
*/

#include <WiFi.h>
#include <WebServer.h>
#include <WebSocketsServer.h>
#include <Update.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "esp_camera.h"
#include "display_assets.h"   // Lopaka-exported bitmap arrays (dashboard)

// ── WiFi credentials ──
const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASS = "YOUR_WIFI_PASSWORD";

// ── OV5640 camera pin mapping (from your hardware notes) ──
#define PWDN_GPIO_NUM   46
#define RESET_GPIO_NUM  45
#define SIOD_GPIO_NUM   4   // SDA
#define SIOC_GPIO_NUM   5   // SCL
// NOTE: fill in your actual D0-D7 / XCLK / VSYNC / HREF / PCLK pins below —
// these depend on your PCB routing and were not specified in the BOM notes.
#define Y2_GPIO_NUM     -1
#define Y3_GPIO_NUM     -1
#define Y4_GPIO_NUM     -1
#define Y5_GPIO_NUM     -1
#define Y6_GPIO_NUM     -1
#define Y7_GPIO_NUM     -1
#define Y8_GPIO_NUM     -1
#define Y9_GPIO_NUM     -1
#define XCLK_GPIO_NUM   -1
#define PCLK_GPIO_NUM   -1
#define VSYNC_GPIO_NUM  -1
#define HREF_GPIO_NUM   -1

// ── SSD1306 (shares I2C bus with BMI270) ──
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

// ── Servers ──
WebServer httpServer(80);
WebSocketsServer webSocket(81);

// ── Telemetry state (fill these in from your real BMI270/battery reads) ──
float batteryPercent = 87.0;
float batteryVoltage = 3.85;
int   tapCount = 0;
unsigned long lastFrameMillis = 0;
unsigned long lastTelemetryMillis = 0;

// ---------------------------------------------------------------
// Camera init
// ---------------------------------------------------------------
bool initCamera() {
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer   = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_QVGA;   // 320x240 — bump up once bandwidth is proven out
  config.jpeg_quality = 12;
  config.fb_count = 2;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed: 0x%x\n", err);
    return false;
  }
  return true;
}

// ---------------------------------------------------------------
// WebSocket event handler
// ---------------------------------------------------------------
void onWsEvent(uint8_t clientId, WStype_t type, uint8_t* payload, size_t length) {
  switch (type) {
    case WStype_CONNECTED:
      Serial.printf("Console connected (client %u)\n", clientId);
      break;
    case WStype_DISCONNECTED:
      Serial.printf("Console disconnected (client %u)\n", clientId);
      break;
    default:
      break; // we only push data out; console doesn't send us commands yet
  }
}

// ---------------------------------------------------------------
// Push one camera frame as a binary WebSocket message
// ---------------------------------------------------------------
void sendCameraFrame() {
  camera_fb_t* fb = esp_camera_fb_get();
  if (!fb) return;
  webSocket.broadcastBIN(fb->buf, fb->len);
  esp_camera_fb_return(fb);
}

// ---------------------------------------------------------------
// Push telemetry as a JSON text WebSocket message
// ---------------------------------------------------------------
void sendTelemetry() {
  String json = "{";
  json += "\"battery\":" + String((int)batteryPercent) + ",";
  json += "\"voltage\":" + String(batteryVoltage, 2) + ",";
  json += "\"rssi\":" + String(WiFi.RSSI()) + ",";
  json += "\"ssid\":\"" + WiFi.SSID() + "\",";
  json += "\"taps\":" + String(tapCount) + ",";
  json += "\"fps\":\"30\"";
  json += "}";
  webSocket.broadcastTXT(json);
}

// ---------------------------------------------------------------
// OTA /update endpoint (matches console's flashFirmware() POST target)
// ---------------------------------------------------------------
void setupOTA() {
  httpServer.on("/update", HTTP_POST, []() {
    httpServer.sendHeader("Connection", "close");
    httpServer.send(200, "text/plain", Update.hasError() ? "FAIL" : "OK");
    delay(500);
    ESP.restart();
  }, []() {
    HTTPUpload& upload = httpServer.upload();
    if (upload.status == UPLOAD_FILE_START) {
      Serial.printf("OTA start: %s\n", upload.filename.c_str());
      if (!Update.begin(UPDATE_SIZE_UNKNOWN)) Update.printError(Serial);
    } else if (upload.status == UPLOAD_FILE_WRITE) {
      if (Update.write(upload.buf, upload.currentSize) != upload.currentSize) Update.printError(Serial);
    } else if (upload.status == UPLOAD_FILE_END) {
      if (Update.end(true)) Serial.printf("OTA success: %u bytes\n", upload.totalSize);
      else Update.printError(Serial);
    }
  });
}

// ---------------------------------------------------------------
// SSD1306 dashboard render (from your Lopaka export)
// ---------------------------------------------------------------
void drawDashboard() {
  display.clearDisplay();
  display.drawBitmap(110, 2, image_Battery_indicator_bits, 15, 7, 1);
  display.drawBitmap(3, 2, image_BT_indicator_bits, 7, 7, 1);
  display.drawBitmap(14, 2, image_Wifi_indicator_bits, 8, 7, 1);
  display.drawBitmap(84, 15, image_Loc_province_bits, 17, 5, 1);
  display.drawBitmap(105, 15, image_Nation_bits, 17, 5, 1);
  display.drawBitmap(103, 31, image_Rain_indicator_bits, 17, 7, 1);
  // display.drawBitmap(84, 26, image_Weather_bitmap_pixels, 16, 15, 1); // TODO: paste this array in from Lopaka
  display.drawBitmap(103, 47, image_Humidity_indicator_bits, 17, 7, 1);
  display.drawBitmap(84, 43, image_Temp_bitmap_bits, 16, 15, 1);
  display.drawBitmap(6, 27, image_segment_1_bits, 15, 29, 1);
  display.drawBitmap(23, 27, image_segment_2_bits, 15, 29, 1);
  display.drawBitmap(46, 27, image_segment_3_bits, 15, 29, 1);
  display.drawBitmap(75, 28, image_segment_4_bits, 3, 27, 1);
  display.drawBitmap(40, 31, image_colon_bits, 4, 21, 1);
  display.drawBitmap(59, 17, image_current_days_bits, 17, 5, 1);
  display.drawBitmap(8, 17, image_Date_Month_bits, 17, 5, 1);
  display.drawBitmap(37, 17, image_Date_day_bits, 11, 5, 1);
  // display.drawBitmap(2, 11, image_border_pixels, 124, 51, 1); // TODO: paste this array in from Lopaka
  display.display();
}

// ---------------------------------------------------------------
void setup() {
  Serial.begin(115200);

  WiFi.begin(WIFI_SSID, WIFI_PASS);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(400);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected. IP: ");
  Serial.println(WiFi.localIP());   // <-- this is what goes into the console's "device-ip" field

  if (!initCamera()) {
    Serial.println("Continuing without camera — fix the D0-D7/XCLK/VSYNC/HREF/PCLK pins above.");
  }

  Wire.begin(SIOD_GPIO_NUM, SIOC_GPIO_NUM); // shared I2C bus: SSD1306 + BMI270
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("SSD1306 init failed");
  }

  webSocket.begin();
  webSocket.onEvent(onWsEvent);

  setupOTA();
  httpServer.begin();

  Serial.println("XonFrame ready. Console: http://<this-ip>/  WebSocket: ws://<this-ip>:81/ws");
}

void loop() {
  webSocket.loop();
  httpServer.handleClient();

  unsigned long now = millis();
  if (now - lastFrameMillis > 100) {       // ~10 fps to start; raise once stable
    sendCameraFrame();
    lastFrameMillis = now;
  }
  if (now - lastTelemetryMillis > 1000) {  // telemetry once a second
    sendTelemetry();
    drawDashboard();
    lastTelemetryMillis = now;
  }
}
