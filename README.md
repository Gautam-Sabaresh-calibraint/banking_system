# Banking app

## Overview
This application simulates a basic functionalities of banking system following the Clean Architecture principles


### Prerequisites
- Python 3.0 or higher

### To run the application
```
python3 main.py
```

### Structure
The application is organized as follows:
```
src/
├── application/{modules}             # Contains Abstracted classes of the repositories and can be extended
├── domain/{modules}                  # Contains business entities and domain logic.
├── infrastructure/{modules}          # Data persistence and infrastructure services.
├── use_case/                         # Application use cases encapsulating business rules.
└── main.py                           # Entry point for the application flow.
```
