char dataString[50] = {0};
int a =0; 

void setup() {
Serial.begin(9600);              //Seri iletişim 9600 bps ile başlatıldı.
  
void loop() {
  a++;                          // a her döngüde bir değer artar
  sprintf(dataString,"%02X",a); // Bu degeri hexa'ya dönüştür. 
  Serial.println(dataString);   // Data gönderme
  delay(1000);                  // Döngüyü 1000 ms beklet
}
