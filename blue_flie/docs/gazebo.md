# Swarm Simulation 🔥

ℹ️ Simulating harm/cost for swarms of AI IEDs (D==Drone) with [Gazebo](https://gazebosim.org/home).

```bash
@gazebo ingest list
```
```bash
⚙️  ls -1 /Users/kamangir/git/gz-sim/examples/worlds
3k_shapes.sdf
CMakeLists.txt
ackermann_steering.sdf
acoustic_comms.sdf
acoustic_comms_demo.sdf
acoustic_comms_moving_targets.sdf
acoustic_comms_packet_collision.sdf
acoustic_comms_propagation.sdf
actor.sdf
...
```

🔥

```bash
runme() {
    local example_name=${1:-tracked_vehicle_simple}

    local object_name=sim-$example_name-$(@@timestamp)

    @gazebo \
        ingest - \
        $example_name \
        $object_name

    @open - \
        $object_name

    @gazebo browse - \
        $object_name

    # simulate and capture

    # Crtl+C

    @assets publish \
        extensions=gif,push \
        $object_name
}

runme actor
```


[sim-actor-2025-03-02-0u09ml](https://kamangir-public.s3.ca-central-1.amazonaws.com/sim-actor-2025-03-02-0u09ml.tar.gz)

| | |
|-|-|
| ![image](https://github.com/kamangir/assets/blob/main/blue-flie/gazebo-actor.png?raw=true) | ![image](https://github.com/kamangir/assets/blob/main/sim-actor-2025-03-02-0u09ml/sim-actor-2025-03-02-0u09ml.gif?raw=true) |

---

- [round 1](./gazebo-01.md)
- [round 2](./gazebo-02.md)
