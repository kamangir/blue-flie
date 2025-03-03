# Swarm Simulation

ℹ️ Simulating harm/cost for swarms of AI IEDs (D==Drone) with [Gazebo](https://gazebosim.org/home).

```
@gazebo ingest list
```

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

set:::object_name sim-actor-2025-03-02-0u09ml

object:::get:::object_name

| | |
|-|-|
| assets:::blue-flie/gazebo-actor.png | assets:::get:::object_name/get:::object_name.gif |

🔥

---

- [round 1](./gazebo-01.md)
