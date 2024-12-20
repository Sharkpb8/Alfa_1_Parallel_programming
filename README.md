# Train Simulation Application

## Author
**Name:** Adam Hlaváčik  
**Contact:** hlavacik@spsejecna.cz
**Date of Completion:** 20.12.2024  
**Institution:** Střední průmyslová škola elektrotechnická, Praha 2, Ječná 30  

---

## Project Overview
This Train Simulation Application is a Python program simulating asynchronic movement of trains betwean stations and passenger traveling betwean these stations.

---

## User Requirements
- The application allows users to add trains, delete trains, manage stations, and simulate train operations.
- It logs train activities, including movement, refueling, and delays.
- Configurations are handled through a `config.json` file.

---

## Application Architecture
The application uses a modular structure:
- **Main Program (`main.py`)**: Manages user interactions and calls simulation functions.
- **Simulation Module (`simulation.py`)**: Handles train simulations, including delays, passenger management, and fuel refills.
- **Doubly Linked List (`DoublyLinkedList.py`)**: Implements linked list functionality for station management.

---

## Imports
### Imported Files
- `config.json`: Contains configuration parameters.
- `trains.json`: Contains preconfigured train and station data.

### Exported Files
- Log files (`/logs/`): Each train has a dedicated log file documenting its operations.

### Required/Optional Fields
- **Train JSON**:
  - Required: `type`, `train_number`, `speed`, `capacity`, `fuel`, `consumption`.
  - Optional: `stations`.
  - If `stations` is included it is required to include `jmeno` and `vzdalenost`

---

## Configuration Options
Configurations are set in `config.json`:
- `allowedtypes`: List of allowed types of trains.
- simulation
  - `mimimum-delay` and `maximum-delay`: Minimum and maximum delay of train.
  - `delay-chance`: Probability of a delay of train.
  - `min-fill` and `max-fill`: Minimum and maximum passangers that can be loaded.
  - `geton-time`: Time in S to load on passangers.
  - `getoff-time`: Time in S to load off passangers.
  - `fuel-time`: Time taken for refueling.
  - `max-refuel`: Maximum addicional ammount of fuel in % to be added to train when refueling

Refer to `config.json` for valid configurations.

---

## Installation and Execution
### Prerequisites
- Python 3.x installed.

### Steps
1. Clone or download the repository.
2. Navigate to the project directory.
3. Run `main.py`:


