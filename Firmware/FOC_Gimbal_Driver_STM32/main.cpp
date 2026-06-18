#include <SimpleFOC.h>

#define PAN_CS_PIN  PA4
#define TILT_CS_PIN PA3

SPIClass SPI_1(PB5, PB4, PB3);

MagneticSensorSPI sensorPan  = MagneticSensorSPI(PAN_CS_PIN, 14, 0x3FFF);
MagneticSensorSPI sensorTilt = MagneticSensorSPI(TILT_CS_PIN, 14, 0x3FFF);

BLDCMotor motorPan  = BLDCMotor(7); 
BLDCMotor motorTilt = BLDCMotor(7);

BLDCDriver3PWM driverPan  = BLDCDriver3PWM(PA8, PA9, PA10, PC13);
BLDCDriver3PWM driverTilt = BLDCDriver3PWM(PB6, PB7, PB8,  PC14);

float targetAnglePan  = 0.0f;
float targetAngleTilt = 0.0f;

void serialCommunicationCheck();

void setup() {
    Serial.begin(115200);
    SimpleFOCDebug::enable(&Serial);

    SPI_1.begin();

    sensorPan.init(&SPI_1);
    sensorTilt.init(&SPI_1);
    
    motorPan.linkSensor(&sensorPan);
    motorTilt.linkSensor(&sensorTilt);

    driverPan.voltage_power_supply  = 12.0f;
    driverTilt.voltage_power_supply = 12.0f;
    driverPan.init();
    driverTilt.init();

    motorPan.linkDriver(&driverPan);
    motorTilt.linkDriver(&driverTilt);

    motorPan.foc_modulation  = FOCModulationType::SpaceVectorPWM;
    motorTilt.foc_modulation = FOCModulationType::SpaceVectorPWM;

    motorPan.controller  = MotionControlType::angle;
    motorTilt.controller = MotionControlType::angle;

    motorPan.PID_velocity.P = 0.15f;
    motorPan.PID_velocity.I = 15.0f;
    motorPan.P_angle.P      = 25.0f;
    motorPan.voltage_limit  = 6.0f;
    motorPan.velocity_limit = 35.0f;

    motorTilt.PID_velocity.P = 0.12f;
    motorTilt.PID_velocity.I = 12.0f;
    motorTilt.P_angle.P      = 20.0f;
    motorTilt.voltage_limit  = 5.0f;
    motorTilt.velocity_limit = 30.0f;

    motorPan.init();
    motorPan.initFOC();

    motorTilt.init();
    motorTilt.initFOC();

    _delay(500);
}

void loop() {
    motorPan.loopFOC();
    motorTilt.loopFOC();

    motorPan.move(targetAnglePan);
    motorTilt.move(targetAngleTilt);

    serialCommunicationCheck();
}

void serialCommunicationCheck() {
    if (Serial.available() > 0) {
        String inputBuffer = Serial.readStringUntil('\n');
        inputBuffer.trim();

        if (inputBuffer.startsWith("P:") && inputBuffer.contains(",T:")) {
            int splitIndex = inputBuffer.indexOf(",T:");
            
            String panSubstring  = inputBuffer.substring(2, splitIndex);
            String tiltSubstring = inputBuffer.substring(splitIndex + 3);

            targetAnglePan  = panSubstring.toFloat();
            targetAngleTilt = tiltSubstring.toFloat();
        }
    }
}