 # viewcloud.py
 #
 # open3D examepl to view a point cloud
 #
 # Paulo Dias

import numpy as np
import open3d as o3d


calibration_params = np.load("3d_coordinates.npz")
points_3D = calibration_params['points']

p = points_3D.reshape(-1, 3)
fp = []

for i in range(p.shape[0]):
    if np.all(~np.isinf(p[i])) and np.all(~np.isnan(p[i])):
        fp.append(p[i])

# Converter lista filtrada para array numpy
fp = np.array(fp)

pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(fp)
#pcl.paint_uniform_color([0.0, 0.0, 0.0])

# Cropping the mesh using its bouding box to remove positive Z-axis between 0.1 and 5
bbox = pcl.get_axis_aligned_bounding_box()
bbox_points = np.asarray(bbox.get_box_points())
bbox_points[:, 2] = np.clip(bbox_points[:, 2], a_min=0.1, a_max=5)
bbox_cropped = o3d.geometry.AxisAlignedBoundingBox.create_from_points(o3d.utility.Vector3dVector(bbox_points))
mesh_cropped = pcl.crop(bbox_cropped)

# Create axes mesh
Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(1)

# shome meshes in view
o3d.visualization.draw_geometries([pcl , Axes])


""" import numpy as np
import open3d as o3d

# Carregar os pontos 3D do arquivo .npz
data = np.load("3d_coordinates.npz")
points_3D = data["points"]  # Substituir pelo nome da variável armazenada no arquivo

# Processar os pontos para criar a nuvem de pontos
p = points_3D.reshape(-1, 3)
fp = []

# Filtrar pontos válidos (sem NaN ou infinitos)
for i in range(p.shape[0]):
    if np.all(~np.isinf(p[i])) and np.all(~np.isnan(p[i])):
        fp.append(p[i])

# Converter lista filtrada para array numpy
fp = np.array(fp)

# Filtrar pontos com z entre 0.1 e 5
fp = fp[(fp[:, 2] >= 0.1) & (fp[:, 2] <= 5)]

# Criar a nuvem de pontos
pcl = o3d.geometry.PointCloud()
pcl.points = o3d.utility.Vector3dVector(fp)

# Adicionar cor (opcional, para melhorar a visualização)
colors = np.random.rand(fp.shape[0], 3)  # Gerar cores aleatórias
pcl.colors = o3d.utility.Vector3dVector(colors)

# Criar eixos para visualização
Axes = o3d.geometry.TriangleMesh.create_coordinate_frame(size=1.0)

# Visualizar a nuvem de pontos
o3d.visualization.draw_geometries([pcl, Axes])

# Cropping usando o bounding box (opcional, mais controle)
bbox = pcl.get_axis_aligned_bounding_box()
bbox_points = np.asarray(bbox.get_box_points())
bbox_points[:, 2] = np.clip(bbox_points[:, 2], a_min=0.1, a_max=5)
bbox_cropped = o3d.geometry.AxisAlignedBoundingBox.create_from_points(
    o3d.utility.Vector3dVector(bbox_points)
)
pcl_cropped = pcl.crop(bbox_cropped)

# Visualizar a nuvem de pontos cortada
o3d.visualization.draw_geometries([pcl_cropped, Axes]) """