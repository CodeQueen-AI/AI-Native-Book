# Physical AI Course Requirements

This document outlines the hardware and software requirements for the Physical AI course.

## Workstation Requirements

- **Why**: Physics calculations (Rigid Body Dynamics) in Gazebo/Isaac are CPU-intensive.
- **RAM**: 64 GB DDR5 (32 GB is the absolute minimum, but will crash during complex scene rendering).
- **OS**: Ubuntu 22.04 LTS.
- **Note**: While Isaac Sim runs on Windows, ROS 2 (Humble/Iron) is native to Linux. Dual-booting or dedicated Linux machines are mandatory for a friction-free experience.

## The "Physical AI" Edge Kit

Since a full humanoid robot is expensive, students learn "Physical AI" by setting up the nervous system on a desk before deploying it to a robot. This kit covers Module 3 (Isaac ROS) and Module 4 (VLA).

- **The Brain**: NVIDIA Jetson Orin Nano (8GB) or Orin NX (16GB).
  - **Role**: This is the industry standard for embodied AI. Students will deploy their ROS 2 nodes here to understand resource constraints vs. their powerful workstations.
- **The Eyes (Vision)**: Intel RealSense D435i or D455.
  - **Role**: Provides RGB (Color) and Depth (Distance) data. Essential for the VSLAM and Perception modules.
- **The Inner Ear (Balance)**: Generic USB IMU (BNO055) (Often built into the RealSense D435i or Jetson boards, but a separate module helps teach IMU calibration).
- **Voice Interface**: A simple USB Microphone/Speaker array (e.g., ReSpeaker) for the "Voice-to-Action" Whisper integration.

## The Robot Lab

For the "Physical" part of the course, you have three tiers of options.

### Option 2 High OpEx: The "Ether" Lab
