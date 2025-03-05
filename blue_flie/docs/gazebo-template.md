# Swarm Simulation

ℹ️ Simulating harm/cost for drone swarms with [Gazebo](https://gazebosim.org/home).

## ingesting an example

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
ingest_example() {
    local example_name=${1:-actor}

    local object_name=sim-$example_name-$(@@timestamp)

    @gazebo \
        ingest - \
        example=$example_name \
        $object_name \
        browse

    # simulate and capture
    # Crtl+C

    @assets publish \
        extensions=gif,push \
        $object_name
}

ingest_example trajectory_follower
```

set:::example_object_name sim-trajectory_follower-2025-03-04-qqdshf

object:::get:::example_object_name

| | |
|-|-|
| assets:::blue-flie/gazebo-trajectory_follower.png | assets:::get:::example_object_name/get:::example_object_name.gif |

## ingesting a fuel

🔥

```bash
ingest_fuel() {
    local fuel_name=${1:-tugbot_depot}

    local object_name=sim-$fuel_name-$(@@timestamp)

    @gazebo \
        ingest - \
        fuel=$fuel_name \
        $object_name \
        browse

    # simulate and capture
    # Crtl+C

    @assets publish \
        extensions=gif,push \
        $object_name
}

ingest_fuel tugbot_depot
```

set:::fuel_object_name gazebo-sim-tugbot_depot-2025-03-04-txe45k

object:::get:::fuel_object_name

| | |
|-|-|
| assets:::blue-flie/gazebo-tugbot_depot.png | assets:::get:::fuel_object_name/get:::fuel_object_name-2X.gif |

---

- [round 1](./gazebo-01.md)
- [round 2](./gazebo-02.md)
- [round 3](./gazebo-03.md)