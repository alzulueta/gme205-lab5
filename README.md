# GmE 205 Lab 4 Polymorphism in Spatial Object Systems
# How to set up the virtual environment
1. Open the VS Code Terminal
2. Create the virtual environment: python3 -m venv .venv
3. Activate the environment: source .venv/bin/activate
4. Install packages: pip install pandas matplotlib shapely
5. Saved installed packages: pip freeze > requirements.txt
# How to run Python scripts
Make sure the virtual environment is activated ((.venv) shows in the terminal)

## Conceptual Reflection
- Polymorphism appears in the system in the way the Parcel, Building, and Road classes each implement their own version of the effective_area() method. Despite having different calculations for area, the program treats all objects the same in the loop and simply calls f.effective_area() for each object, without needing to know its type.
- Polymorphism removes conditional logic from analysis.py (or run_lab5.py) because there is no if or elif checking whether an object is a parcel, building, or road. Each object knows how to compute its own area, so the program can loop over all features and call effective_area() directly.
- The OOP pillar that allows multiple spatial classes to share a method name is polymorphism, which is closely related to inheritance. Parcel, Building, and Road all inherit from SpatialObject, which defines the effective_area() interface.
- It is better for objects to compute their own area rather than using conditional logic because it follows the principle of encapsulation where each object handles its own data and behavior. This makes the system easier to maintain and extend, and reduces the risk of errors from repeated type checks in the program logic.
- If a new class, such as River, is added tomorrow, the changes required in spatial.py would be minimal. I would create a new River class that inherits from SpatialObject and implements its own effective_area() method. No changes would be needed in run_lab5.py to accommodate it as it would automatically be included in the polymorphic loop.