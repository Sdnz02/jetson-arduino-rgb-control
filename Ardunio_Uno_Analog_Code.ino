const int analogPin = A0;  // Analog input pin
const int digitalPin1 = 2; // Digital output pin 1
const int digitalPin2 = 3; // Digital output pin 2

void setup() {
  pinMode(digitalPin1, OUTPUT);
  pinMode(digitalPin2, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Read analog input
  int analogValue = analogRead(analogPin);

  // Print the analog value for reference
  Serial.print("Analog Value: ");
  Serial.println(analogValue);

  // Check the analog value and set digital outputs accordingly
  if (analogValue < 200) {
    digitalWrite(digitalPin1, LOW);
    digitalWrite(digitalPin2, LOW);
  } else if (analogValue < 400) {
    digitalWrite(digitalPin1, HIGH);
    digitalWrite(digitalPin2, HIGH);
  } else {
    digitalWrite(digitalPin1, LOW);
    digitalWrite(digitalPin2, HIGH);
  }

  // Add a delay to avoid rapid changes
delay(1000);
}