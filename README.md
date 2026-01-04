<div align="center">

# 🎨 Roulette Curves

### *Beautiful Mathematical Curves Brought to Life with Python* ✨

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Turtle Graphics](https://img.shields.io/badge/Graphics-Turtle-green.svg)](https://docs.python.org/3/library/turtle.html)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Made with Love](https://img.shields.io/badge/Made%20with-❤️-red.svg)](https://github.com/willow788/Roulette-Curves)

*Explore the mesmerizing world of roulette curves - where mathematics meets art* 🎭

---

</div>

## 🌟 What Are Roulette Curves? 

Roulette curves are fascinating mathematical constructs created by tracing a point attached to a curve as it rolls along another curve. These elegant patterns have captivated mathematicians and artists for centuries, appearing in everything from gear design to architectural ornaments.

This repository brings these beautiful curves to life through animated Python visualizations with stunning rainbow color gradients!  🌈

## 🎯 Featured Curves

<table>
<tr>
<td width="50%">

### 🔵 Cycloid Curves
The path traced by a point on a circle rolling along a straight line. 
- Classic arch-like patterns
- Foundation of many mechanical designs

</td>
<td width="50%">

### ⭐ Epicycloid Curves
Created when a circle rolls around the **outside** of another circle.
- Stunning flower-like patterns
- Multiple petals based on radius ratios

</td>
</tr>
<tr>
<td width="50%">

### 🌸 Hypocycloid Curves
Formed when a circle rolls around the **inside** of another circle.
- Star-shaped patterns
- The famous spirograph effect! 

</td>
<td width="50%">

### 🎪 Epitrochoid & Curtate Trochoids
Variations with the tracing point at different distances from the center.
- More complex and organic patterns
- Even more spectacular designs

</td>
</tr>
</table>

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.x with turtle graphics (usually pre-installed)
python --version
```

### Installation

```bash
# Clone the repository
git clone https://github.com/willow788/Roulette-Curves.git

# Navigate to the directory
cd Roulette-Curves

# Choose a curve type and run! 
cd "Cycloid Curves"
python cycloid.py
```

## 📁 Repository Structure

```
Roulette-Curves/
│
├── 📂 Cycloid Curves/
│   └── cycloid.py
│
├── 📂 Epicycloid Curves/
│   ├── Simple version/
│   └── More visually pleasing version/
│
├── 📂 Hypocycloid Curves/
│   └── Python Code/
│
├── 📂 Epitrochoid Curves/
│
├── 📂 Curtate Trophoids/
│
└── README.md
```

## 🎨 Features

✨ **Rainbow Color Gradients** - Each curve uses HSV color cycling for beautiful, smooth color transitions

🎭 **Smooth Animations** - Watch the curves being drawn in real-time with optimized rendering

⚙️ **Customizable Parameters** - Easily adjust radius ratios, steps, and scaling factors

🖥️ **Auto-Scaling** - Curves automatically fit to your screen for optimal viewing

📐 **Mathematically Accurate** - Based on true parametric equations for each curve type

## 🧮 The Mathematics

Each curve type follows specific parametric equations:

### Cycloid
```
x(t) = r(t - sin(t))
y(t) = r(1 - cos(t))
```

### Epicycloid
```
x(θ) = (R + r)cos(θ) - r·cos((R + r)/r · θ)
y(θ) = (R + r)sin(θ) - r·sin((R + r)/r · θ)
```

### Hypocycloid
```
x(θ) = (R - r)cos(θ) + r·cos((R - r)/r · θ)
y(θ) = (R - r)sin(θ) - r·sin((R - r)/r · θ)
```

Where:
- `R` = radius of the fixed circle
- `r` = radius of the rolling circle
- `θ` or `t` = parameter (angle)

## 🎮 Customization Guide

Want to create your own unique patterns? Modify these parameters in any script:

```python
# Circle radii
R = 110  # Fixed circle radius
r = 37   # Rolling circle radius

# Animation quality
steps = 5000  # Higher = smoother but slower

# Color animation speed
hue += 0.0005  # Adjust for faster/slower color changes
```

**Pro Tip:** Try different R/r ratios for different petal counts! 
- R/r = 2 → 2-pointed star
- R/r = 3 → 3-petaled flower (deltoid)
- R/r = 4 → 4-pointed star (astroid)

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Turtle Graphics** - Built-in Python graphics library
- **colorsys** - HSV to RGB color conversions
- **math** - Trigonometric functions

## 💡 Use Cases

- 🎓 **Education** - Teaching parametric equations and mathematical curves
- 🎨 **Art** - Generating unique geometric art pieces
- 🧘 **Meditation** - Relaxing visualizations
- ⚙️ **Engineering** - Understanding gear profiles and cam designs
- 🎪 **Recreation** - Digital spirograph fun! 

## 🤝 Contributing

Contributions are welcome! Feel free to: 

- Add new curve types
- Improve animations
- Optimize code
- Add interactive controls
- Create documentation

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## 🌟 Show Your Support

If you find this project interesting, please consider:

- ⭐ Starring the repository
- 🍴 Forking and creating your own variations
- 🐛 Reporting bugs or suggesting features
- 📢 Sharing with others who love mathematics and art! 

---

<div align="center">

### *"Mathematics is the art of giving the same name to different things"* - Henri Poincaré

Made with 💙 by [willow788](https://github.com/willow788)

**Happy Curve Drawing! 🎨✨**

</div>
