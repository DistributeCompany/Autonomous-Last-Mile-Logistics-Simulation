# Autonomous Last-Mile Logistics Simulation

This repository contains a base model implemented in Plant Simulation 16.1 for a Challenge-Based Learning course on discrete-event simulation. This model was used for the graduate course *Simulation* at the University of Twente in Fall 2024. It provides a framework for students to execute a simulation study focused on autonomous last-mile logistics systems.

## Video Demonstration

[![Benchmark Scenario Video](.videos/benchmark_scenario.png)](https://www.youtube.com/watch?v=Bb3ENU9rbBU)

> Click the image above to watch a video demonstration of the **Benchmark Scenario** (250x speed).


## Table of Contents
- [Introduction](#introduction)
- [Simulation Goal](#simulation-goal)
- [The Base Model](#the-base-model)
- [Base Model Details](#base-model-details)
  - [Frames and Objects](#frames-and-objects)
  - [Autonomous Vehicles](#autonomous-vehicles)
  - [Simulation Rules](#simulation-rules)
- [General Remarks](#general-remarks)
- [Contact Information](#contact-information)

## Introduction

This repository provides the base model for conducting a simulation study of autonomous last-mile logistics systems. Instructors can use this model as part of a final assignment. For access to the 'teacher' version of the base model, please contact:

- **Berry Gerrits** - [b.gerrits@utwente.nl](mailto:b.gerrits@utwente.nl)
- **Martijn Mes** - [m.r.k.mes@utwente.nl](mailto:m.r.k.mes@utwente.nl)

## Simulation Goal

The study aims to explore the design and impact of an autonomous last-mile logistics system on the University of Twente's campus. The focus is on e-commerce parcel delivery via a base model that simulates two delivery scenarios:
1. **BenchmarkScenario**: Traditional one-by-one delivery by vans.
2. **DecouplingScenario**: Delivery vans drop parcels at a centralized decoupling point, and autonomous vehicles handle the last-mile delivery.

## The Base Model

The base model is built in **Plant Simulation 16.1** and simulates the University of Twente campus. Features include:
- Visualized delivery destinations (grey cubes).
- A decoupling point at the Central Reception for autonomous vehicle deliveries.
- Two pre-defined scenarios (BenchmarkScenario and DecouplingScenario).

The base model lacks scheduling/dispatching logic, which must be implemented as part of the assignment.

## Base Model Details

### Frames and Objects

The model is structured into several frames and objects, including:

#### Frames
- **Campus**: Main physical layout of the campus with the event controller.
- **Inputs**: Input parameters and experimental factors.
- **Outputs**: Simulation outputs with placeholder tables.
- **Methods**: Centralized methods for simulation logic.
- **DecouplingPoint**: Models the decoupling point.
- **Destination**: Represents delivery destinations on campus (i.e., customers).
- **Model**: Empty frame for customization.

#### Objects
- **RoadMarker**: Defines vehicle paths. That is, vehicles drive from Marker to Marker. 
- **Parcel**: Represents e-commerce parcels with attributes like delivery status and time windows.
- **DeliveryModePool**: Origin of vehicles, with separate pools for specific autonomous vehicles.

### Autonomous Vehicles

The following autonomous vehicles are available for last-mile delivery:
- **MobileParcelLocker**: Unmanned Ground Vehicle. Carries up to 24 parcels.
- **StreetRobot**: Unmanned Ground Vehicle. Carries one parcel.
- **QuadcopterNoHoist**: Unmanned Aerial Vehicle. Carries one parcel. Had to land for delivery.
- **QuadcopterWithHoist**: Unmanned Aerial Vehicle. Carries one parcel, and is equipped with a hoist system for delivery while hovering.

### Simulation Rules

- Each simulation represents one day (09:00 to midnight).
- Parcels have specific delivery windows.
- Basic battery management is included, but may result in depletion of the battery during delivery!

## General Remarks

- The scale of the map is approximately 1:14 (1 meter in the model equals 14 meters in reality).
- Adjustments to methods should be made in the `.Models.Methods` frame.

## Contact Information

For additional details see the Word document in this repository. For further inquiries:
- **Berry Gerrits**: [b.gerrits@utwente.nl](mailto:b.gerrits@utwente.nl)
- **Martijn Mes**: [m.r.k.mes@utwente.nl](mailto:m.r.k.mes@utwente.nl)
