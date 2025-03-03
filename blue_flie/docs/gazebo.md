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


[sim-2025-03-02-otpupk](https://kamangir-public.s3.ca-central-1.amazonaws.com/sim-2025-03-02-otpupk.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/blue-flie/gazebo.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/sim-2025-03-02-otpupk/sim-2025-03-02-otpupk.gif?raw=true) |

🔥
