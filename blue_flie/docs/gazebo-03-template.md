# Swarm Simulation - round 3

ℹ️ Simulating harm/cost for drone swarms with [Gazebo](https://gazebosim.org/home).

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

```bash
runme() {
    local example_name=${1:-actor}

    local object_name=sim-$example_name-$(@@timestamp)

    @gazebo \
        ingest - \
        $example_name \
        $object_name \
        browse

    # simulate and capture
    # Crtl+C

    @assets publish \
        extensions=gif,push \
        $object_name
}

runme wind
```

set:::object_name sim-wind-2025-03-03-de0n62

object:::get:::object_name

| | |
|-|-|
| assets:::blue-flie/gazebo-wind.png | assets:::get:::object_name/get:::object_name.gif |

---

- [round 1](./gazebo-01.md)
- [round 2](./gazebo-02.md)