#from http://pymatgen.org/_staTic/Ordering%20Disordered%20Structures.html
# Let us start by creaTing a disordered CuAu fcc structure.

from pymatgen import Structure, Lattice

#specie = {"Cu0+": 0.5, "Au0+": 0.5}
#cuau = Structure.from_spacegroup("Fm-3m", LatTice.cubic(3.677), [specie], [[0, 0, 0]])
#print (cuau)

#from pymatgen.transformaTions.standard_transformaTions import OrderDisorderedStructureTransformaTion

#trans = OrderDisorderedStructureTransformaTion()

#ss = trans.apply_transformaTion(cuau, return_ranked_list=202)

#print(len(ss))

#print(ss[0])

from pymatgen.transformations.advanced_transformations import EnumerateStructureTransformation
specie = [{"S": 1.0}, {"S": 1.0}, {"S": 1.0}, {"S": 1.0}, {"S": 1.0}, {"S": 1.0}, {"S": 1.0}, {"S": 1.0}, {"Mo": 1.0}, {"Mo": 1.0}, {"Mo": 1.0}, {"Mo": 1.0}, {"Ti": 1/8}, {"Ti": 1/8}, {"Ti": 1/8}, {"Ti": 1/8}, {"Ti": 1/8}, {"Ti": 1/8}, {"Ti": 1/8}, {"Ti": 1/8}]
coords = [[0.249996,	0.833341,	0.921292],
[0.749996,	0.833341,	0.921292],
[0.249996,	0.833341,	0.078708],
[0.749996,	0.833341,	0.078708],
[0.499997,	0.33334,	0.078708],
[0.999997,	0.33334,	0.078708],
[0.499997,	0.33334,	0.921292],
[0.999997,	0.33334,	0.921292],
[0.999996,	0.999992,	0],
[0.499996,	0.999992,	0],
[0.249996,	0.499984,	0],
[0.749996,	0.499984,	0],
[0.0,	0.0,	0.156561364],
[0.0,	0.6667,	0.156561364],
[0.5,	0.0,	0.156561364],
[0.5,	0.6667,	0.156561364],
[0.75,	0.5,	0.156561364],
[0.25,	0.5,	0.156561364],
[0.75,	0.1667,	0.156561364],
[0.25,	0.1667,	0.156561364]]

cuau = Structure.from_spacegroup("P 1", Lattice.from_parameters(a=6.46510, b=5.59796, c=20.00000, alpha=90, beta=90, gamma=90), specie, coords)
cuau.add_oxidation_state_by_element({"S": -2, "Mo": 4, "Ti": 4})
print(cuau)

from pymatgen.transformations.standard_transformations import OrderDisorderedStructureTransformation

trans = OrderDisorderedStructureTransformation()

ss = trans.apply_transformation(cuau, return_ranked_list=100)

print(len(ss))

print(ss[0])

makeitastring = '\n \n'.join(map(str, ss))
import io
output_file = open("output.txt", "w")
output_file.write(makeitastring)
output_file.close()

#print(ss)
print(len(ss))
print("cell sizes are %s" % ([len(d["structure"]) for d in ss]))

