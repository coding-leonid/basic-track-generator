# Basic Formula Student Style Track Generator

## Getting Started

To get started, pull the repo by running

```bash
git clone git@github.com:coding-leonid/basic-track-generator.git
```

To run the program, make sure you are in the `basic-track-generator` folder and then run

```bash
python3 main.py <mode>
```

where `<mode>`is either `click` or `list`. See usage guide for more info on the modes.

## Usage Guide

The modes differ in how the track is generated, but the result is the same. When the track is generated, cones marked with `*` will be displayed, yellow on the right side with respect to the direction of motion and blue on the left side, as per Formula Student Driverless rules. The edges of the track are additionally outlined by dashed lines. The first waypoint is defined as the start of the track, which is marked by a pair of orange cones on each side. A solid black centerline is also drawn, which can be toggled by pressing `h`.

### Click Mode

In click mode, the user clicks on the canvas to add waypoints for the track. By waypoints, we mean points that lie on the centerline of the track. If the user wishes to remove the latest waypoint, they can press `x`. When the desired number of waypoints have been added, the user can click `t` to generate the track.

The user can save the track, i.e. the coordinates of the cones and their color into a `.csv` file by pressing `d` when the track has been generated. The file is saved in the `generated_files` folder as `track_XXX.csv` with the smallest unused three-digit number for `XXX`.

### List Mode

In list mode, the variable `settings.TRACK_POINTS` is used as waypoints for the centerline of the track. Again, the user can save the generated cones as `.csv` if desired.
