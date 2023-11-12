# Junction2023_smec
Repo for Junction 2023 

# Sample Data Breakdown

This data appears to be from a wearable device or similar monitoring system, capturing a variety of physiological and environmental metrics.

## Eye Data (`afe`)

- **Left Eye (Index 0) & Right Eye (Index 1)**:
  - `i`: 
    - Ticktime (ms since device boot)
    - TimeStamp (synchronized time in microseconds)
    - Status (0 = OK, 1 = error)
    - Counter
  - `m`: 
    - Measurements for different signals (first 6 values are of interest)
    - Indices 6 and 7 are unusable signals
  - `t`: Type of the eye (L for left, R for right)

## Heart Rate Data (`heart`)

- `hr`: Current heart rate
- `intervals`: Heart rate intervals (reported only once)

## GPS Data (`gps`)

- Latitude and Longitude: Current GPS location

## Battery Information (`battery`)

- Voltage and Percentage remaining

## Auxiliary Sensors (`auxSensors`)

1. **Light Ambient (`lightAmbient`)**:
   - UV, Ambient Light, and IR sensor values
   - Status (0 = OK, 1 = Saturated or error)
2. **Temperature (`tempEt`)**:
   - Temperature readings for left and right eye sensors
   - Status (0 = OK, 1 = error)

## Labels (`labels`)

- Provides context about the conditions during data capture (e.g., "Running", "Dark")

