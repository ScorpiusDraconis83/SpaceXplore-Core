# API Reference for SpaceXplore-Core

## Introduction
This document provides an overview of the APIs available in the SpaceXplore-Core system. Each API endpoint is described with its purpose, request parameters, and response format.

## Base URL

[http://localhost:5000/api/v1](http://localhost:5000/api/v1)


## Endpoints

### 1. Propulsion API

#### Get Propulsion Status
- **Endpoint**: `/propulsion/status`
- **Method**: `GET`
- **Description**: Retrieves the current status of the propulsion system.
- **Response**:
  ```json
  1 {
  2   "status": "active",
  3   "thrust": 1500,
  4   "fuel_level": 75
  5 }
  ```

#### Set Propulsion Parameters
- **Endpoint**: /propulsion/set
- **Method**: POST
- **Description**: Sets the parameters for the propulsion system.
- **Request Body**:
   ```json
   1 {
   2   "thrust": 1500,
   3   "duration": 3600
   4 }
   ```
- **Response**:
   ```json
   1 {
   2   "message": "Propulsion parameters set successfully."
   3 
   4 }
   ```
### 2. Robotics API

#### Get Robotic Probe Status
- **Endpoint**: `/robotics/probe/status`
- **Method**: `GET`
- **Description**: Retrieves the current status of the robotic probe.
- **Response**:
   ```json
   1 {
   2   "status": "active",
   3   "position": {
   4     "x": 10.5,
   5     "y": 20.7,
   6     "z": 30.9
   7   }
   8 }
   ```
#### Send Command to Robotic Probe**
- **Endpoint**: /robotics/probe/command
- **Method**: POST
- **Description**: Sends a command to the robotic probe.
- **Request Body**:
   ```json
   1 {
   2   "thrust": 1500,
   3   "duration": 3600
   4 }
   ```
- **Response**:
   ```json
   1 {
   2   "message": "Propulsion parameters set successfully."
   3 }
   ```

### 3. Communication API
- **Get Communication Status**
- **Endpoint**: /communication/status
- **Method**: GET
- **Description**: Retrieves the current status of the communication system.
- **Response**:
   ```json
   1 {
   2   "status": "active",
   3   "signal_strength": 80
   4 }
   ```

#### Send Data via Communication System
- **Endpoint**: /communication/send
- **Method**: POST
- **Description**: Sends data through the communication system.
- **Request Body**:
   ```json
   1 {
   2   "data": "Hello, World!"
   3 }
   ```
- **Response**:
   ```json
   1 {
   2   "message": "Data sent successfully."
   3 }
   ```
# Conclusion
This API reference provides a comprehensive overview of the available endpoints in the SpaceXplore-Core system. For further assistance, please refer to the user manual or contact support.



