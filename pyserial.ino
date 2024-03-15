#include "IRremote.h"
IRrecv irrecv(2);
decode_results results;
void setup(){
    Serial.begin(9600);
    irrecv.enableIRIn();
  }
void loop()
{
  if (irrecv.decode(&results)) { 
    int control_code = results.value;
    Serial.println(control_code); //сообщить значение приема в монитор
   irrecv.resume(); //возобновление работы ИК приемника
  }
}
