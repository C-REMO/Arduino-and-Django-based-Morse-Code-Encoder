String data="";
int led = 12;
void setup() {
  Serial.begin(9600);
  pinMode(led, OUTPUT);
  digitalWrite(13, LOW);  
}

void loop() {
  if(Serial.available() > 0) {
    data = Serial.readString();
    const char* source = data.c_str();
    int length = (int)strlen(source);
    for (int i = 0; i < length; i++) {
      if(source[i]=='.')
      {  
        digitalWrite(led, HIGH); 
        delay(300);       
        digitalWrite(led, LOW); 
        delay(300); 
      }
      else if (source[i]=='-')
      {
        digitalWrite(led, HIGH); 
        delay(900);       
        digitalWrite(led, LOW); 
        delay(300); 
      }
      else if(source[i]=='/')
      {
        delay(1800); 
      }
      else
      {
        delay(600);
      }
    }
  }
}
