# Project Aegis: Dual-Axis FOC EOTS Gimbal

An elite, high-precision Electro-Optical Targeting System built from scratch. This system utilizes Field Oriented Control (FOC) for continuous, high-torque stabilization and features a dual-camera sensor payload for thermal tracking and optical zoom.

- [Project Aegis: Dual-Axis FOC EOTS Gimbal](#project-aegis-dual-axis-foc-eots-gimbal)
- [Core System Architecture](#core-system-architecture)
  - [Embedded Control & Power Distribution](#embedded-control--power-distribution)
  - [Mechatronics & Actuation](#mechatronics--actuation)
  - [Optical Payload](#optical-payload)
- [Hardware Manifesto (BOM)](#hardware-manifesto-bom)

---

# Core System Architecture

The custom 4-layer control board isolates high-frequency digital lines from high-current motor return paths to preserve analog signal integrity. 

## Embedded Control & Power Distribution
* **Microcontroller:** STM32F405RGT6 running custom embedded FOC loops.
* **Gate Drivers:** Dual DRV8313 triple half-bridge drivers managing motor phase currents.
* **Interconnects:** 6-pin JST-XH vertical locking headers (B6B-XH-A) route encoder inputs directly into the MCU timers.
* **Power Delivery:** Main system power is distributed via a high-amperage XT60 connector.

## Mechatronics & Actuation
The mechanical assembly routes power and signals through continuous rotational axes without tangling internal wiring.
* **Actuators:** Dual 2804 100KV brushless motors hard-mounted directly to the structural yoke arms.
* **Sensor Fusion:** An MPU9250 IMU tracks high-speed orientation dynamics in real-time.
* **Feedback Loop:** AS5048A magnetic rotary encoders paired with shaft-mounted diametric neodymium magnets handle absolute angular tracking down to 14-bit resolution.
* **Slip Ring Integration:** A 12-channel MSC-22-12 high-speed capsule slip ring passes continuous USB-C video data through the rotating non-motor pivot arm.

## Optical Payload
The sealed sphere housing protects a dual-sensor array running image processing loops back to a central hub.
* **Primary Optical:** IMX-series high-resolution camera module for target detection and optical zoom tracking.
* **Thermal Matrix:** AMG8833 8x8 infrared thermopile array for long-wave thermal signature targeting.
* **Processing Unit:** Raspberry Pi Zero 2 W handles localized video streaming, telemetry generation, and targeting overlays.

---

# Hardware Manifesto (BOM)

| Component Category | Description / Specifications | Cost (DH) |
| :--- | :--- | :--- |
| **Actuators** | 2x 2804 100KV Brushless Motors | 200 dh |
| **Control Electronics** | Custom 4-Layer PCBA (STM32F405 / Dual DRV8313) | 1500 dh |
| **Feedback Sensors** | 2x AS5048A 14-Bit Magnetic Encoders (Magnets Included) | 175.82 dh |
| **Inertial Measurement** | MPU9250 IMU | Owned |
| **Vision Payload** | IMX Camera Module + AMG8833 Thermal Array | 400 dh |
| **Compute Core** | Raspberry Pi Zero 2 W | 300 dh |
| **Rotary Interface** | 12-Channel High-Speed Capsule Slip Ring (12w) | 160 dh |
| **Structural Frame** | Custom Chassis + 3D Printing Filament | 350 dh |
| **Fasteners** | M2/M2.5/M3 Socket Head Cap Screws Kit (625pcs) | 218 dh |
| **Interconnects** | 6-Pin JST-XH Pre-Crimped Wire Harnesses | 53.30 dh |
