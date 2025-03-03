# Swarm Simulation

ℹ️ Simulating harm/cost for swarms of AI IEDs (D==Drone) with [Gazebo](https://gazebosim.org/home).

```bash
@select sim-$(@@timestamp)
@open - .
cp -v ../2025-03-02-15-20-03-vb5bvs/world.sdf ./

@gazebo browse - . gui

# second terminal
@gazebo browse - . server

# simulate and capture

# Crtl+C

@assets publish extensions=gif,push .
```

set:::object_name sim-2025-03-02-otpupk

object:::get:::object_name

| | |
|-|-|
| assets:::blue-flie/gazebo.png | assets:::get:::object_name/get:::object_name.gif |