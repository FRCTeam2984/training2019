# Conventions

- These are the conventions that must be followed when editing this repository

## File Structure
- Basic file structure of the repository. Folders can be added as needed to improve organization.
```
.
├── CONVENTIONS.md
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── autonomous
    │   └── autonomous.py
    ├── components
    │   └── chassis.py
    ├── physics.p4y
    ├── robot.py
    ├── sim
    │   ├── config.json
    │   └── field.png
    ├── tests
    │   └── pyfrc_test.py
    └── utils
        └── geometry.py
```

## Formatting
- `format` script in source folder
- [autoflake](https://github.com/myint/autoflake) for removing unused imports
    - Install with `pip install autoflake`
- [black](https://github.com/ambv/black) for formatting
    - Install with `pip install black`

## Naming
- Snake case for variables
    - `drive_motor_left = TalonSRX(0)`
    - `veloicty_right = 10.0`
- Lower camel case for class methods and functions
    - `def setVelocity(self, velocity_left: float, velocity_right: float) -> None:`
    - `def boundRadians(theta: float) -> float:`
- Upper camel case for class names
    - `class Robot(magicbot.MagicRobot):`
    - `class Chassis:`

## Typing
- Parameters and function outputs should be typed (if possible)
- See [naming](#Naming) for examples

## Units
- Time: `seconds` (some native function use `ms`)
- Length: `meters` (some native functions use `feet`)
- Angle: `radians` (some native functions use `degrees`; the `config.json` file uses degrees; paths are saved with `degrees` but are converted to `radians` when imported)
- Weight: `kilograms`
- Coordinates
    - allo-centric (top down view with the long side horizontal)
        - x: `left/right starting from 0 on the left`
        - y: `bottom/top with 0 in the middle and positive on the top`
        - theta: `counterclockwise starting from 0 facing to the right`
    - ego-centric
        - x: `left/right`
        - y: `backwards/forwards`
        - theta: `counterclockwise starting from 0 facing forwards`