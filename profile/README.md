<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="logo-dark.png">
    <img src="logo-light.png" alt="Studio Sanka" width="320">
  </picture>
</p>

# Studio Sanka

**Ordinary parts. Extraordinary machines.**

We design robots that anyone can build from hardware-store parts, and give the designs away.
**Not-for-profit. Not a company. Free, forever.**

Our website, with who we are, what we believe, who built what and how to build the robot, is **coming soon**.

## Our first robot: SixEyes

A robot arm you can build yourself: 3D-printed gearboxes, ordinary stepper motors and a circuit board you can solder by hand. The goal is about S$250 for the whole arm.

> **Work in progress.** The board design and firmware are written; nobody has built a complete arm yet. The website has the current status, so you know what is real before you buy anything.

## Where things are

| Repository | What is in it |
|---|---|
| [sixeyes](https://github.com/studiosanka/sixeyes) | **The arm itself:** circuit board, firmware, printable parts and the build guides. Start here to build |
| [website](https://github.com/studiosanka/website) | The code of our website (the site itself is coming soon) |
| [sixeyes-drive](https://github.com/studiosanka/sixeyes-drive) | **Drive the arm with your phone** (Android and Chrome): move the phone, the arm follows. Record and replay movements |
| [sixeyes-host](https://github.com/studiosanka/sixeyes-host) | Talk to the arm from a computer over USB, in Python. Has a pretend arm, so you can try things without hardware |
| [lerobot-sixeyes](https://github.com/studiosanka/lerobot-sixeyes) | Record training data and let an AI policy drive the arm, with [LeRobot](https://github.com/huggingface/lerobot) |
| [sixeyes_description](https://github.com/studiosanka/sixeyes_description) | The arm's shape and joint limits, for ROS 2 and for the phone controller |
| [sixeyes_ros2](https://github.com/studiosanka/sixeyes_ros2) | Control the arm with ROS 2 and MoveIt, in a pretend arm, in Gazebo, or on the real arm. *Written but not tested yet* |

New to all this? Begin with the [sixeyes](https://github.com/studiosanka/sixeyes) repository and its build guides.

## Licences

Everything is open. If you sell something made from our designs, you must credit Studio Sanka.

| What | Licence |
|---|---|
| Firmware and software | Apache 2.0 |
| Hardware designs | CERN-OHL-S-2.0 |
| Documentation | CC-BY-4.0 |

## Questions, bugs and ideas

Open an issue in the repository it is about. Our repositories are maintained by Studio Sanka members and do not take pull requests for now; see [how we work](https://github.com/studiosanka/.github/blob/main/CONTRIBUTING.md) and our [code of conduct](https://github.com/studiosanka/.github/blob/main/CODE_OF_CONDUCT.md).

---

*Developed with AI assistance from [Claude](https://www.anthropic.com/claude) (Anthropic) and GitHub Copilot. The designs, decisions and review are by the Studio Sanka team.*
