/*
  XonFrame 
*/
#include <WiFi.h>
#include <WebServer.h>
#include <WebSocketsServer.h>
#include <Update.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include "esp_camera.h"
#include "display_assets.h" 

const char* WIFI_SSID = "YOUR_WIFI_SSID";
const char* WIFI_PASS = "YOUR_WIFI_PASSWORD";
 
#define PWDN_GPIO_NUM   46
#define RESET_GPIO_NUM  45
#define SIOD_GPIO_NUM   4  
#define SIOC_GPIO_NUM   5  

#define Y2_GPIO_NUM     35  // D0
#define Y3_GPIO_NUM     36  // D1
#define Y4_GPIO_NUM     37  // D2
#define Y5_GPIO_NUM     38  // D3
#define Y6_GPIO_NUM     17  // D4
#define Y7_GPIO_NUM     18  // D5
#define Y8_GPIO_NUM     11  // D6
#define Y9_GPIO_NUM     10  // D7
#define XCLK_GPIO_NUM   21 
#define PCLK_GPIO_NUM   14
#define VSYNC_GPIO_NUM  33
#define HREF_GPIO_NUM   34

#define SCREEN_WIDTH 64
#define SCREEN_HEIGHT 34
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

WebServer httpServer(80);
WebSocketsServer webSocket(81);

float batteryPercent = 87.0;
float batteryVoltage = 3.85;
int   tapCount = 0;
unsigned long lastFrameMillis = 0;
unsigned long lastTelemetryMillis = 0;

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
  config.frame_size = FRAMESIZE_QVGA;  
  config.jpeg_quality = 12;
  config.fb_count = 2;

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed: 0x%x\n", err);
    return false;
  }
  return true;
}

void onWsEvent(uint8_t clientId, WStype_t type, uint8_t* payload, size_t length) {
  switch (type) {
    case WStype_CONNECTED:
      Serial.printf("Console connected (client %u)\n", clientId);
      break;
    case WStype_DISCONNECTED:
      Serial.printf("Console disconnected (client %u)\n", clientId);
      break;
    default:
      break;
}

void sendCameraFrame() {
  camera_fb_t* fb = esp_camera_fb_get();
  if (!fb) return;
  webSocket.broadcastBIN(fb->buf, fb->len);
  esp_camera_fb_return(fb);
}



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


void drawDashboard() {
  display.clearDisplay();
  display.drawBitmap(110, 2, image_Battery_indicator_bits, 15, 7, 1);
  display.drawBitmap(3, 2, image_BT_indicator_bits, 7, 7, 1);
  display.drawBitmap(14, 2, image_Wifi_indicator_bits, 8, 7, 1);
  display.drawBitmap(84, 15, image_Loc_province_bits, 17, 5, 1);
  display.drawBitmap(105, 15, image_Nation_bits, 17, 5, 1);
  display.drawBitmap(103, 31, image_Rain_indicator_bits, 17, 7, 1);
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
  display.display();
}


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
  Serial.println(WiFi.localIP());   

  if (!initCamera()) {
    Serial.println("Continuing without camera ");
  }

  Wire.begin(SIOD_GPIO_NUM, SIOC_GPIO_NUM); 
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
  if (now - lastFrameMillis > 100) {     
    sendCameraFrame();
    lastFrameMillis = now;
  }
  if (now - lastTelemetryMillis > 1000) {  
    sendTelemetry();
    drawDashboard();
    lastTelemetryMillis = now;
  }
}
