# 🦋 blue-flie

🌀 `@flie` is an [`abcli`](https://github.com/kamangir/awesome-bash-cli) plugin for drone simulation and non-ROS robot control. See [blue-rover](https://github.com/kamangir/blue-rover) for ROS robots.

```bash
pip install blue-flie
```

```mermaid
graph LR
    gazebo_browse["@gazebo browse~~- <object-name> gui|server"]

    gazebo_ingest_list["@gazebo ingest list"]

    gazebo_ingest["@gazebo ingest~~- <example-name> <object-name> browse"]

    examples["examples"]:::folder
    object["📁 object"]:::folder
    UI["🖥️ UI"]:::folder

    object --> gazebo_browse
    gazebo_browse --> object
    gazebo_browse --> UI

    gazebo_ingest_list --> examples 

    examples --> gazebo_ingest
    gazebo_ingest --> object
    gazebo_ingest --> gazebo_browse

    classDef folder fill:#999,stroke:#333,stroke-width:2px;
```

--table--

---

--signature--