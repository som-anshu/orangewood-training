# Orangewood Industrial Training

Repository for tracking progress, tasks, and simulation developments during the Orangewood training program.

---

## Current Status: Branch Pivot

> [!IMPORTANT]
> Development on the `main` branch is currently **halted** due to configuration issues within the custom URDF files. Active development, debugging, and testing have been shifted to the **`v1`** branch.

---

## ROS 2 Simulation Setup (`main` Branch)

The work on the `main` branch focuses on establishing a robotics simulation environment using ROS 2. 

### System Specifications
- **OS:** Ubuntu 24.04 LTS
- **ROS 2 Distribution:** Jazzy Jalisco
- **Robot Platform:** TurtleBot3 Burger (installed via `apt`)

### World Configuration
A custom simulation world (`.sdf`) was designed with a specific obstacle layout to test robot navigation and mapping.

**Simulation World Layout:**
```text
+-----------------------------------+
|                                   |
|       [ box2 ]                    |
|                                   |
|                 [ box1 ]          |
|                                   |
|   [ box3 ]                        |
|                                   |
+-----------------------------------+
